# -*- extra stuff goes here -*- 
from Products.Archetypes.public import *
from Products.Archetypes import listTypes
from Products.CMFCore import permissions, utils, DirectoryView

from config import PROJECTNAME, SKINS_DIR

ADD_CONTENT_PERMISSION = permissions.AddPortalContent
DirectoryView.registerDirectory(SKINS_DIR, globals())

def initialize(context):
    """ Initializer called when used as a Zope 2 product.
    """
    import contents

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME
    )

    allTypes = zip(content_types, constructors)

    for atype, constructor in allTypes:
        kind = "%s: %s" % (PROJECTNAME, atype.archetype_name)
        utils.ContentInit(
            kind,
            content_types      = (atype,),
            permission         = ADD_CONTENT_PERMISSION,
            extra_constructors = (constructor,),
            fti                = ftis,
        ).initialize(context)
