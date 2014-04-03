from zope.component import getMultiAdapter
from Acquisition import aq_inner
from Products.Five import BrowserView

from interfaces import IFischereiverView
from Products.CMFCore.utils import getToolByName 
from AccessControl.SecurityManagement import getSecurityManagerfrom AccessControl.SecurityManagement import newSecurityManagerfrom AccessControl.SecurityManagement import setSecurityManagerfrom AccessControl.User import UnrestrictedUser
import datetime

class OrganisationView(BrowserView):
    """
    """
    def getAuthorInfo(self, author=''):
        mtool = self.context.portal_membership
        if author:
            author_obj = mtool.getMemberById(author)
            function = author_obj.getProperty('function', '')
            return function
        return 
        
