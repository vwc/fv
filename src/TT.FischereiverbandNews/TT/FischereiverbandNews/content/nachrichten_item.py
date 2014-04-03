# Zope imports
from AccessControl import ClassSecurityInfo
from zope.interface import implements

# CMFCore imports
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.permissions import View
# Archetypes imports
from Products.Archetypes.atapi import *

# CMFPlone imports
from Products.CMFPlone import PloneMessageFactory as _

# ATContentTypes imports
from Products.ATContentTypes.content.folder import ATFolder

# This Module imports
from TT.FischereiverbandNews.config import *
from TT.FischereiverbandNews.interfaces import INachrichtenItem
from TT.FischereiverbandNews.Fields import ImagesField
from TT.FischereiverbandNews.Widgets import ImagesWidget

schema = Schema((
    TextField(
        name='subTitle',
        widget=StringWidget(
            label= _(u'schema_sub_title', default=u'SubTitle'),
            description= _(u'schema_help_sub_title', default=u'A subtitle of the content'),
        )
    ),

    TextField(
        name='shortText',
        widget=TextAreaWidget(
            label= _(u'schema_help_short_text', default=u'Short Text'),
            description= _(u'schema_help_short_text', default=u'A short summary of the content'),
        )
    ),
    TextField(
        name='text',
        allowable_content_types=(
            'text/plain', 
            'text/structured',
            'text/html', 
            'application/msword',),
        default_output_type='text/html',            
        widget=RichWidget(
            label= _(u'This text is used within detailed news item view.', default=u'Text'),
            description= _(u'schema_text_description', default=u'This text is used within detailed news item view.'),
        ),
    ),
    ImageField(
        schemata="Images",
        required=False,
        name='images',
        sizes= {'large'   : (768, 768),
                'preview' : (400, 400),
                'mini'    : (200, 200),
                'thumb'   : (128, 128),
                'tile'    :  (64, 64),
                'icon'    :  (32, 32),
                'listing' :  (16, 16),
               },
        widget=ImageWidget(
            #visible = {"edit": "invisible", "view": "invisible"},
            description = _(u'schema_images_default_description', default=u'Upload preview images'),
            label= _(u'schema_images_default_label', default=u'Image'),
        ),
        storage=AttributeStorage()
    ),
    ImagesField(
        schemata="Images",
        required=False,
        name='ImageList',
        widget=ImagesWidget(
            label= _(u'schema_images_label', default=u'Images'),
            description = _(u'schema_images_description', default=u'Upload some the images'),            
        ),
    ),
    BooleanField(
        name = "forChildren",
        languageIndependent=True,
        widget = BooleanWidget(
            label= _(u'schema_for_children_label', default=u'For Children'),
            description = _(u'schema_for_children_description', default=u'If selected, the children can see this content'),            
        ),
    ),
    
))

schema = ATFolder.schema.copy() + schema
schema['description'].widget.visible = False;

# Dates
schema.changeSchemataForField('effectiveDate',  'Dates')
schema.changeSchemataForField('expirationDate', 'Dates')
schema.changeSchemataForField('creation_date', 'Dates')    
schema.changeSchemataForField('modification_date', 'Dates')

# Categorization
schema.changeSchemataForField('subject', 'plone')
schema.changeSchemataForField('relatedItems', 'plone')
schema.changeSchemataForField('location', 'plone')
schema.changeSchemataForField('language', 'plone')

# Ownership
schema.changeSchemataForField('creators', 'plone')
schema.changeSchemataForField('contributors', 'plone')
schema.changeSchemataForField('rights', 'plone')

# Settings
schema.changeSchemataForField('allowDiscussion', 'plone')
schema.changeSchemataForField('excludeFromNav', 'plone')
schema.changeSchemataForField('nextPreviousEnabled', 'plone')

class NachrichtenItem(ATFolder):
    """
    """
    implements(INachrichtenItem)    
    security = ClassSecurityInfo()
    schema = schema
    
    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('images').tag(self, **kwargs)
           
registerType(NachrichtenItem, PROJECTNAME)