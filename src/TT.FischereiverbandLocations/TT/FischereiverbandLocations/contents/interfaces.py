from zope.interface import Interface
from zope import schema

from Products.CMFPlone import PloneMessageFactory as _

class ILocationItem(Interface):
    """ A Location workspace
    """

class ILocation(Interface):
    """ A Location workspace
    """

class ILocations(Interface):
    """ A Location container
    """
