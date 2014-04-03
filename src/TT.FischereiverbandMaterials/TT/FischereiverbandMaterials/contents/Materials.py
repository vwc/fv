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

from interfaces import IMaterials
from ..config import PROJECTNAME

MaterialSchema = ATFolderSchema.copy() + Schema((
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
  ), marshall=RFC822Marshaller()
)

finalizeATCTSchema(MaterialSchema)

class Materials(ATFolder):
    implements(IMaterials)
    portal_type = "Materials"
    archetype_name = ATFolder.archetype_name
    schema = MaterialSchema


registerATCT(Materials, PROJECTNAME)