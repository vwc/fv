# zope imports
from zope.interface import implements
from AccessControl import ClassSecurityInfo

# Archetypes imports
from Products.Archetypes.atapi import *

# CMFPlone imports
from Products.CMFPlone import PloneMessageFactory as _

# CMFCore imports
from Products.CMFCore.utils import getToolByName

# ATContentTypes imports
from Products.ATContentTypes.content.link import ATLink

# This Module imports
from TT.RedirectLink.config import *
from TT.RedirectLink.config import _
from TT.RedirectLink.interfaces import IInternalRedirect
from TT.RedirectLink.fields import ListObjectsField
from TT.RedirectLink.widgets import ListObjectsWidget

schema = Schema((
    BooleanField(
        name = "setDefault",
        widget = BooleanWidget(
            label= _(u'schema_set_default_page_label', default=u'Set default page'),
            description = _(u'schema_set_default_page_description', default=u'If selected, this object will be displayed as the default page of this folder'),            
        ),
    ),
    ListObjectsField(
        name = "linkTo",
        required = True,
        widget = ListObjectsWidget(
            label= _(u'schema_link_to_label', default=u'Link To'),
            description = _(u'schema_link_to_description', default=u'Select the internal object to redirect when the object has selected'),            
        ),
    )
))

schema = ATLink.schema.copy() + schema
schema['title'].default = 'Redirect Link'
schema['description'].widget.visible = False;
schema['remoteUrl'].widget.visible = False;

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

class InternalRedirect(ATLink):
    """
    """
    implements(IInternalRedirect)
    security = ClassSecurityInfo()
    schema = schema
    
    def at_post_create_script(self):
        wftool = getToolByName(self, "portal_workflow")
        wftool.doActionFor(self, "publish")
        self.defaultPage()
        
    def at_post_edit_script(self):
        self.defaultPage()
        
    def defaultPage(self):
        parentObj = self.aq_inner.aq_parent
        if parentObj.meta_type == 'TempFolder':
            parentObj = self.aq_inner.aq_parent.aq_parent.aq_parent
        if self.setDefault:
            parentObj.setDefaultPage(self.id)
        else:
            parentObj.setDefaultPage(None)
            
registerType(InternalRedirect, PROJECTNAME)