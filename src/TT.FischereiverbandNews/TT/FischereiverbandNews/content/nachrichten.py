# zope imports
from zope.interface import implements
from AccessControl import ClassSecurityInfo

# Archetypes imports
from Products.Archetypes.atapi import *

# CMFCore imports
from Products.CMFCore.utils import getToolByName

# CMFPlone imports
from Products.CMFPlone import PloneMessageFactory as _

# ATContentTypes imports
from Products.ATContentTypes.content.folder import ATFolder

# This Module imports
from TT.FischereiverbandNews.config import *
from TT.FischereiverbandNews.interfaces import INachrichten

schema = Schema((
    TextField(
        name='shortText',
        allowable_content_types=(
            'text/plain', 
            'text/structured',
            'text/html', 
            'application/msword',),
        default_output_type='text/html',            
        widget=RichWidget(
            label= _(u'schema_help_short_text', default=u'Short Text'),
            description= _(u'schema_help_short_text', default=u'A short summary of the content'),
        )
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
schema.changeSchemataForField('effectiveDate',  'plone')
schema.changeSchemataForField('expirationDate', 'plone')
schema.changeSchemataForField('creation_date', 'plone')    
schema.changeSchemataForField('modification_date', 'plone')    

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

class Nachrichten(ATFolder):
    """
    """
    implements(INachrichten)
    security = ClassSecurityInfo()
    schema = schema

            
registerType(Nachrichten, PROJECTNAME)