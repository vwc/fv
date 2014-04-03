from plone.theme.interfaces import IDefaultPloneLayer
from zope.viewlet.interfaces import IViewletManager
from zope.interface import Interface

from AccessControl import Unauthorized

from zope.interface import implements
from zope import schema
from zope.component import getUtility
from zope.schema import ValidationError

from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.exceptions import EmailAddressInvalid
from Products.CMFDefault.formlib.schema import FileUpload
from Products.CMFPlone import PloneMessageFactory as _

from plone.app.users.userdataschema import checkEmailAddress

class IFischereiverband(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "Fischereiverband" theme, this interface must be its layer
       (in Fischereiverband/viewlets/configure.zcml).
    """

class IPortalSearch(IViewletManager):
    """ A viewlet manager that sits in column right
    """
class IMetaAction(IViewletManager):
    """ A viewlet manager that sits in right of global_sections
    """

class IFischereiverView(Interface):
    """ 
    """
    def getColumnsClass():
        """ Returns the CSS class based on columns presence. 
        """
    def getNameOfColumn():
        """
        """

class IUserDataSchema(Interface):
    """
    """

    fullname = schema.TextLine(
        title=_(u'label_full_name', default=u'Full Name'),
        description=u'',
        required=False)

    function = schema.TextLine(
        title=_(u'label_function', default=u'Function'),
        description=u'',
        required=False)

    residence = schema.TextLine(
        title=_(u'label_residence', default=u'Residence'),
        description=u'',
        required=False)

    day_of_bith = schema.Date(
        title=_(u'label_day_of_bith', default=u'Day of Bith'),
        description=u'mm/dd/yyyy',
        required=False)

    in_office_since = schema.Date(
        title=_(u'label_in_office_since', default=u'In office since'),
        description=u'mm/dd/yyyy',
        required=False)

    orther = schema.TextLine(
        title=_(u'label_orther', default=u'Orther'),
        description=u'',
        required=False)

    email = schema.ASCIILine(
        title=_(u'label_email', default=u'E-mail'),
        description=u'',
        required=True,
        constraint=checkEmailAddress)

    portrait = FileUpload(title=_(u'label_portrait', default=u'Portrait'),
        description=_(u'help_portrait',
                      default=u'To add or change the portrait: click the '
                      '"Browse" button; select a picture of yourself. '
                      'Recommended image size is 75 pixels wide by 100 '
                      'pixels tall.'),
        required=False)

    pdelete = schema.Bool(
        title=_(u'label_delete_portrait', default=u'Delete Portrait'),
        description=u'',
        required=False)
        
class IUploadingCapable(Interface):
    """Any container/object that is supported for uploading into.
    """
       
