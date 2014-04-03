# Zope imports
from AccessControl import ClassSecurityInfo
from zope.interface import implements

# CMFCore imports
from Products.CMFCore.utils import getToolByName

# Archetypes imports
from Products.Archetypes.atapi import *

# CMFPlone imports
from Products.CMFPlone import PloneMessageFactory as _

# ATContentTypes imports
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.event import ATEvent

# This Module imports
from TT.FischereiverbandNews.config import *
from TT.FischereiverbandNews.interfaces import ITermineItem



schema = Schema((
    TextField(
        name='shortText',
        widget=TextAreaWidget(
            label= _(u'schema_help_short_text', default=u'Short Text'),
            description= _(u'schema_help_short_text', default='A short summary of the content'),
        )
    ),
    TextField(
        name='linksText',
        allowable_content_types=(
            'text/plain', 
            'text/structured',
            'text/html', 
            'application/msword',),
        default_output_type='text/html',            
        widget=RichWidget(
            label= _(u'schema_link_text_label', default=u'Links Text'),
            description= _(u'schema_link_text_description ', default=u'This text is used show more links of event.'),
        ),
    ),
    ImageField(
        schemata="Image & Files",
        required=False,
        name='image',
        sizes= {'large'   : (768, 768),
                'preview' : (400, 400),
                'mini'    : (200, 200),
                'thumb'   : (128, 128),
                'tile'    :  (64, 64),
                'icon'    :  (32, 32),
                'listing' :  (16, 16),
               },
        widget=ImageWidget(
            label= _(u'schema_image_label', default=u'Image'),
        ),
        storage=AttributeStorage()
    ),
    FileField(
        schemata="Image & Files",
        required=False,
        name='firstFile',
        widget=FileWidget(
            label= _(u'schema_first_file_label', default=u'The first file upload (pdf)'),
        ),
    ),
    FileField(
        schemata="Image & Files",
        required=False,
        name='secondFile',
        widget=FileWidget(
            label= _(u'schema_second_file_label', default=u'The second file upload (word or pdf)'),
        ),
    ),
))

schema1 = Schema(( 
TextField(
        name='text',
        allowable_content_types=(
            'text/plain', 
            'text/structured',
            'text/html', 
            'application/msword',),
        default_output_type='text/html',            
        widget=RichWidget(
            rows = 15,
            label= _(u'schema_text_label', default=u'Text'),
            description= _(u'schema_text_description', default=u'This text is used within detailed event item view.'),
        ),
    ),
    BooleanField(
        name = "forChildren",
        languageIndependent=True,
        widget = BooleanWidget(
            label= _(u'schema_for_children_label', default=u'For Children'),
            description = _(u'schema_for_children_description', default=u'If selected, the children can see this content'),            
        ),
    )
))

schema = ATFolder.schema.copy() + schema + ATEvent.schema.copy() + schema1
schema['description'].widget.visible = False;



# Dates
schema.changeSchemataForField('startDate',  'Dates')
schema.changeSchemataForField('endDate',  'Dates')
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

# ATEvent Fields
schema.changeSchemataForField('location',  'plone')
schema.changeSchemataForField('attendees',  'plone')
schema.changeSchemataForField('eventUrl',  'plone')
schema.changeSchemataForField('contactName',  'plone')
schema.changeSchemataForField('contactEmail',  'plone')
schema.changeSchemataForField('contactPhone',  'plone')

class TermineItem(ATFolder, ATEvent):
    """
    """
    implements(ITermineItem)    
    security = ClassSecurityInfo()
    schema = schema
            
registerType(TermineItem, PROJECTNAME)