from zope.interface import implements

from AccessControl import ClassSecurityInfo

from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import FloatField
from Products.Archetypes.atapi import DecimalWidget
from Products.Archetypes.atapi import RFC822Marshaller
from Products.Archetypes.atapi import AnnotationStorage

from Products.ATContentTypes.configuration import zconf
from Products.ATContentTypes.content.folder import ATFolder, ATFolderSchema
from Products.ATContentTypes.content.base import ATCTContent, registerATCT
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFCore.permissions import View

from Products.validation import V_REQUIRED

from interfaces import IMaterial
from ..config import PROJECTNAME

MaterialSchema = ATCTContent.schema.copy() + Schema((
    FloatField('price',
        required = True,
        searchable = True,
        default = 0.0,
        validators = ('isDecimal',),
        widget = DecimalWidget(
            description = '',
            label = _(u'', default=u'Price'),
            size = 40)
    ),
    ), marshall=RFC822Marshaller()
)

class Material(ATCTContent):
    implements(IMaterial)
    portal_type = "Material"
    archetype_name = ATCTContent.archetype_name
    schema = MaterialSchema


registerATCT(Material, PROJECTNAME)