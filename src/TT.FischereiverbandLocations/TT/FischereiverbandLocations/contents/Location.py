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

LocationSchema = ATFolderSchema.copy() + Schema((
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
                        label= _(u'label_location_map_image', default=u'Map Image'),
                        show_content_type = False,)
    ),

    LocationAreaField('locationArea',
        required = True,
        searchable = True,
        widget = LocationAreaWidget(
            description = '',
            label = _(u'label_location_area', default=u'Location Area'),
            size = 40)
        ),

    ), marshall=RFC822Marshaller()
)

finalizeATCTSchema(LocationSchema)

class Location(ATFolder):
    implements(ILocation)
    portal_type = "Location"
    archetype_name = ATFolder.archetype_name
    schema = LocationSchema

    security = ClassSecurityInfo()

    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('map').tag(self, **kwargs)

registerATCT(Location, PROJECTNAME)