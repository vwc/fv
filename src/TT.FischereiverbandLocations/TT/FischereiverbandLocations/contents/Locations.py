from zope.interface import implements

from AccessControl import ClassSecurityInfo

from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import ImageField, TextField, StringField
from Products.Archetypes.atapi import ImageWidget, RichWidget, StringWidget
from Products.Archetypes.atapi import RFC822Marshaller
from Products.Archetypes.atapi import AnnotationStorage

from Products.ATContentTypes.configuration import zconf
from Products.ATContentTypes.content.folder import ATFolder, ATFolderSchema
from Products.ATContentTypes.content.base import registerATCT
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFCore.permissions import View

from Products.validation import V_REQUIRED

from interfaces import ILocation, ILocations
from ..config import PROJECTNAME

from ..fields import LocationAreaField
from ..widgets import LocationAreaWidget

LocationsSchema = ATFolderSchema.copy() + Schema((
    StringField('header',
        required = False,
        searchable = True,
        widget = StringWidget(
            description = '',
            label = _(u'label_locations_header', default=u'Header'),
            size = 40)
    ),

    TextField('text',
              required=False,
              searchable=True,
              storage = AnnotationStorage(migrate=True),
              validators = ('isTidyHtmlWithCleanup',),
              default_output_type = 'text/x-html-safe',
              widget = RichWidget(
                        description = '',
                        label = _(u'label_locations_info', default=u'Infomation'),
                        rows = 25,
                        allow_file_upload = zconf.ATDocument.allow_document_upload),
    ),

    ImageField('map',
               required=True,
               primary=True,
               languageIndependent=True,
               storage = AnnotationStorage(migrate=True),
               swallowResizeExceptions = zconf.swallowImageResizeExceptions.enable,
               pil_quality = zconf.pil_config.quality,
               pil_resize_algo = zconf.pil_config.resize_algo,
               max_size = zconf.ATImage.max_image_dimension,
               sizes= {'large'   : (768, 768),
                       'preview' : (400, 400),
                       'mini'    : (200, 200),
                       'thumb'   : (128, 128),
                       'tile'    :  (64, 64),
                       'icon'    :  (32, 32),
                       'listing' :  (16, 16),
                      },
               validators = (('isNonEmptyFile', V_REQUIRED),
                             ('checkImageMaxSize', V_REQUIRED)),
               widget = ImageWidget(
                        description = '',
                        label= _(u'label_locations_map_image', default=u'Map Image'),
                        show_content_type = False,)
    ),

    ), marshall=RFC822Marshaller()
)

finalizeATCTSchema(LocationsSchema)

class Locations(ATFolder):
    implements(ILocations)
    portal_type = "Locations"
    archetype_name = ATFolder.archetype_name
    schema = LocationsSchema

    security = ClassSecurityInfo()

    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('map').tag(self, **kwargs)

    security.declareProtected(View, 'getSize')
    def getSize(self, scale=None):
        field = self.getField('map')
        return field.getSize(self, scale=scale)

    security.declareProtected(View, 'getWidth')
    def getWidth(self, scale=None):
        return self.getSize(scale)[0]

    security.declareProtected(View, 'getHeight')
    def getHeight(self, scale=None):
        return self.getSize(scale)[1]

registerATCT(Locations, PROJECTNAME)
