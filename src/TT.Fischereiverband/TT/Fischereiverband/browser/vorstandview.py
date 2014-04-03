from zope.component import getMultiAdapter
from Acquisition import aq_inner
from Products.Five import BrowserView

from interfaces import IFischereiverView
from Products.CMFCore.utils import getToolByName 
from AccessControl.SecurityManagement import getSecurityManagerfrom AccessControl.SecurityManagement import newSecurityManagerfrom AccessControl.SecurityManagement import setSecurityManagerfrom AccessControl.User import UnrestrictedUser
import datetime

class VorstandView(BrowserView):
    """
    """
    def getAuthorInfo(self, author=''):
        mtool = self.context.portal_membership
        authorinfo = mtool.getMemberInfo(author)
        author_obj = mtool.getMemberById(author)
        fullname  = authorinfo.get('fullname','&nbsp;')
        function = author_obj.getProperty('function', '&nbsp;')
        residence = author_obj.getProperty('residence', '&nbsp;')
        day_of_birth = author_obj.getProperty('day_of_bith', '&nbsp;')
        if type(day_of_birth).__name__ != 'str':
            day_of_birth = day_of_birth.year
        in_office_since = author_obj.getProperty('in_office_since', '&nbsp;')
        if type(in_office_since).__name__ != 'str' :
            in_office_since = in_office_since.year
        other = author_obj.getProperty('orther', '&nbsp;')

        infos = {'fullname': fullname,
                 'function': function,
                 'residence': residence,
                 'day_of_birth': day_of_birth,
                 'in_office_since': in_office_since,
                 'other': other,
        }
        return infos
        
