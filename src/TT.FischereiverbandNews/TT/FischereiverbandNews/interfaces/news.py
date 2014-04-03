# zope imports
from zope import schema
from zope.interface import Interface
from zope.interface import Attribute

################################################################################
# Nachrichten        
################################################################################
        
class INachrichten(Interface):
    """Marker interface to mark news content objects. 
    """

################################################################################
# NachrichtenItem       
################################################################################
        
class INachrichtenItem(Interface):
    """Marker interface to mark news item content objects. 
    """
       
################################################################################
# Termine     
################################################################################
        
class ITermine(Interface):
    """Marker interface to mark termine content objects. 
    """
    
################################################################################
# TermineItem    
################################################################################
        
class ITermineItem(Interface):
    """Marker interface to mark termine item content objects. 
    """