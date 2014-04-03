from zope.interface import implements

from AccessControl import ClassSecurityInfo

from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import TextField
from Products.Archetypes.atapi import RichWidget
from Products.Archetypes.atapi import RFC822Marshaller
from Products.Archetypes.atapi import AnnotationStorage

from Products.ATContentTypes.configuration import zconf
from Products.ATContentTypes.content.folder import ATFolder, ATFolderSchema
from Products.ATContentTypes.content.base import ATCTContent, registerATCT
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from TT.Fischereiverband.Field import VorstandListField
from TT.Fischereiverband.Widget import VorstandSelectionWidget
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFCore.permissions import View

from Products.validation import V_REQUIRED

from interfaces import IOrganisation
from TT.Fischereiverband.config import PROJECTNAME

OrganisationSchema = ATCTContent.schema.copy() + Schema((
    TextField('shortText',
              required=False,
              searchable=True,
              storage = AnnotationStorage(migrate=True),
              validators = ('isTidyHtmlWithCleanup',),
              default_output_type = 'text/x-html-safe',
              widget = RichWidget(
                        description = '',
                        label = _(u'label_short_text', default=u'Short Text'),
                        rows = 25,
                        allow_file_upload = zconf.ATDocument.allow_document_upload),
    ),
    TextField('longText',
              required=False,
              searchable=True,
              storage = AnnotationStorage(migrate=True),
              validators = ('isTidyHtmlWithCleanup',),
              default_output_type = 'text/x-html-safe',
              widget = RichWidget(
                        description = '',
                        label = _(u'label_long_text', default=u'Long Text'),
                        rows = 25,
                        allow_file_upload = zconf.ATDocument.allow_document_upload),
    ),
    VorstandListField('listUserOfVorstand',
        required    = 1,
        widget = VorstandSelectionWidget(
            size                = 10,
            label               = 'List User Of Vorstand',
            label_msgid         = 'label_content_list_Vorstand',
            description         = 'Select the users in the board',
            description_msgid   = 'help_content_list_Vorstand',
            i18n_domain         = 'plone'
        ),
    ),

    ), marshall=RFC822Marshaller()
)

OrganisationSchema['description'].widget.visible = {'view' : 'invisible', 'edit' : 'invisible'}

class Organisation(ATCTContent):
    implements(IOrganisation)
    portal_type = "Organisation"
    archetype_name = ATCTContent.archetype_name
    schema = OrganisationSchema


registerATCT(Organisation, PROJECTNAME)