from zope.component import adapts
from zope.formlib import form
from zope.interface import implements
from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFDefault.formlib.widgets import FileUploadWidget

from plone.app.users.browser.personalpreferences import UserDataPanel as baseUserDataPanel
from plone.app.users.browser.personalpreferences import UserDataPanelAdapter as baseUserDataPanelAdapter

from plone.app.layout.navigation.interfaces import INavigationRoot

from Products.CMFDefault.formlib.schema import ProxyFieldProperty

from Products.CMFPlone import PloneMessageFactory as _

from interfaces import IUserDataSchema

class UserDataPanel(baseUserDataPanel):
    """ """
    label = _(u'title_personal_information_form', default=u'Personal Information')
    description = _(u'description_personal_information_form', default='Change your personal information')
    form_name = _(u'User Data Form')

    template = ViewPageTemplateFile('account-configlet.pt')

    def __init__(self, context, request):
        """ Load the UserDataSchema at view time. 
        
        (Because doing getUtility for IUserDataSchemaProvider fails at startup
        time.)
   
        """
        super(UserDataPanel, self).__init__(context, request)
        self.form_fields = form.FormFields(IUserDataSchema)
        self.form_fields['portrait'].custom_widget = FileUploadWidget
        

class UserDataPanelAdapter(baseUserDataPanelAdapter):
    """ """
    def __init__(self, context):
        super(UserDataPanelAdapter, self).__init__(context)
        pprop = getToolByName(context, 'portal_properties')
        self.encoding = pprop.site_properties.default_charset
        
    def getMemberByRequest(self):
        mtool = getToolByName(self.context, 'portal_membership')
        user_id = self.context.REQUEST.get('userid','')
        if not user_id:
            member = mtool.getAuthenticatedMember()
        member = mtool.getMemberById(user_id)
        return member
    
    def get_portrait(self):
        mtool = getToolByName(self.context, 'portal_membership')
        member = self.getMemberByRequest()
        portrait = mtool.getPersonalPortrait(member.id)
        return portrait

    def set_portrait(self, value):
        member = self.getMemberByRequest()
        member_id = member.id
        if value:
            context = aq_inner(self.context)
            context.portal_membership.changeMemberPortrait(value,member_id)
            
    portrait = property(get_portrait, set_portrait)

    function = ProxyFieldProperty(IUserDataSchema['function'])

    residence = ProxyFieldProperty(IUserDataSchema['residence'])
    
    day_of_bith = ProxyFieldProperty(IUserDataSchema['day_of_bith'])
    
    in_office_since = ProxyFieldProperty(IUserDataSchema['in_office_since'])
    
    orther = ProxyFieldProperty(IUserDataSchema['orther'])
