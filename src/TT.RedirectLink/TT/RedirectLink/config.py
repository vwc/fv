# coding=utf-8
import os
from App.Common import package_home
from Products.CMFCore import permissions
from Products.CMFCore.permissions import setDefaultRoles

# MessageFactory
from zope.i18nmessageid import MessageFactory
_ = MessageFactory("RedirectLink")

PROJECTNAME = "TT. RedirectLink"
ADD_CONTENT_PERMISSION = "Add portal content"
