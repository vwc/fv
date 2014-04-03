  # -*- extra stuff goes here -*- 

from Products.CMFCore import utils as cmf_utils
from Products.Archetypes.atapi import *
from Products.Archetypes import listTypes

from TT.RedirectLink.config import *

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    from AccessControl import allow_module
    allow_module('zope.component')
    allow_module('zope.event')
    allow_module("pdb")
    
    import TT.RedirectLink.content
    
    # Initialize portal content
    all_content_types, all_constructors, all_ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)
        
    cmf_utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = all_content_types,
        permission         = ADD_CONTENT_PERMISSION,
        extra_constructors = all_constructors,
        fti                = all_ftis,
        ).initialize(context)

    print '> __init__ initialize TT.RedirectLink success.'