from AccessControl import ClassSecurityInfo
from Products.Archetypes.Field import Field
from Products.Archetypes.Field import ObjectField
from Products.Archetypes.Field import encode, decode

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Registry import registerField

from Products.CMFPlone import PloneMessageFactory as _

from TT.FischereiverbandNews.Widgets import ImagesWidget

class ImagesField(ObjectField):
    """Used for storing the image objects"""
    
    _properties = Field._properties.copy()
    _properties.update({
        'type'      : 'string',
        'default'   : '',
        'widget'    : ImagesWidget,
    })
    
    security = ClassSecurityInfo()
    
    security.declarePrivate('_setCustomImages')
    def _setCustomImages(self, instance, value, **kwargs):
        """ 
        """
        customImageCount = int(instance.REQUEST.get('customImageCount', 0))
        default = int(instance.REQUEST.get('defaultImage', 0))
        for i in range(customImageCount):
            func = instance.REQUEST.get('%s_%s_delete'%(self.getName(), i))
            id = instance.REQUEST.get('%s_%s_id'%(self.getName(), i))
            imageObj = instance.get(id)
            if func=='delete':
                #delete the image object
                obj_parent = imageObj.aq_inner.aq_parent
                obj_parent.manage_delObjects([imageObj.getId()])
                instance.plone_utils.addPortalMessage(_(u'Deleted custom image.'))
            elif func=='nochange':
                pass
            else:
#                #overwrite with new image if exists
                newImageObj = instance.REQUEST.get('%s_%s_image'% (self.getName(), i))
                if not newImageObj:
                    continue
                mt_tool = getToolByName(instance,'mimetypes_registry')
                mimetype = str(mt_tool.classify(newImageObj.read(1024)))
                newImageObj.seek(0)
                data = newImageObj.read()
                imageObj.setImage(newImageObj)
                newFileName = newImageObj.filename
                imageObj.setTitle(newFileName)
            if default == i :
                id = instance.REQUEST.get('%s_%s_id'%(self.getName(), i))
                ObjectField.set(self, instance, id, **kwargs)

            
    
    security.declarePrivate('set')
    def set(self, instance, value, **kwargs):
        #set the existing images
        self._setCustomImages(instance, value, **kwargs)
        default = int(instance.REQUEST.get('defaultImage', 0))
        customImageCount = int(instance.REQUEST.get('customImageCount', 0))
        if default >= customImageCount:
            newDefault = default - customImageCount
        for index,fileObj in enumerate(value):
            try:
                fileObj.seek(0)
            except:
                continue
            data = fileObj.read()
            if not data:
                continue
            id=instance.generateUniqueId('Image')
            new_id = instance.invokeFactory('Image', id=id)
            obj = getattr(instance, new_id)
            if not obj:
                raise "File could not be created"
            filename = fileObj.filename
            obj.unmarkCreationFlag()
            obj.setImage(fileObj)
            obj.setTitle(filename)
            obj.reindexObject()
            if index == newDefault:
                ObjectField.set(self, instance, new_id, **kwargs)
            

    security.declarePrivate('get')
    def get(self, instance, **kwargs):

        return ObjectField.get(self, instance, **kwargs) or ''

registerField(ImagesField,
              title='ImagesField',
              description=('Used for storing the image objects'))