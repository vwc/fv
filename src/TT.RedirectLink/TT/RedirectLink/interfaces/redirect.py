# zope imports
from zope import schema
from zope.interface import Interface
from zope.interface import Attribute

################################################################################
# InternalRedirect        
################################################################################
        
class IInternalRedirect(Interface):
    """Marker interface to mark internal redirect content objects. 
    """