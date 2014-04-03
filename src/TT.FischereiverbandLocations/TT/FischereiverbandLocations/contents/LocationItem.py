from zope.interface import implements

from AccessControl import ClassSecurityInfo

from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import ImageField, TextField, StringField
from Products.Archetypes.atapi import ImageWidget, RichWidget, StringWidget
from Products.Archetypes.atapi import RFC822Marshaller
from Products.Archetypes.atapi import AnnotationStorage

from Products.ATContentTypes.configuration import zconf
from Products.ATContentTypes.content.folder import ATFolder, ATFolderSchema
from Products.ATContentTypes.content.base import ATCTContent, registerATCT
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFCore.permissions import View

from Products.validation import V_REQUIRED

from interfaces import ILocationItem
from ..config import PROJECTNAME

LocationItemSchema = ATCTContent.schema.copy() + Schema((
    StringField('itemURL',
        required = False,
        searchable = True,
        validators = ('isURL',),
        widget = StringWidget(
            description = '',
            label = _(u'label_location_item_url', default=u'URL'),
            size = 40)
    ),
    StringField('email',
        required = False,
        searchable = True,
        validators = ('isEmail',),
        widget = StringWidget(
            description = '',
            label = _(u'label_location_item_email', default=u'email'),
            size = 40)
    ),
    ), marshall=RFC822Marshaller()
)

finalizeATCTSchema(LocationItemSchema)

class LocationItem(ATCTContent):
    implements(ILocationItem)
    portal_type = "LocationItem"
    archetype_name = ATCTContent.archetype_name
    schema = LocationItemSchema


registerATCT(LocationItem, PROJECTNAME)