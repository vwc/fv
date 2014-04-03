from Acquisition import aq_inner, aq_parent
from Products.CMFCore.utils import getToolByName

def manage_edit(instance, event):
    """ 
    """
    parent = aq_parent( aq_inner( instance ) )
    if hasattr(parent,'portal_type') and \
        parent.portal_type == 'TempFolder': return
    print '->> instance.REQUEST.RESPONSE.redirect ', parent.absolute_url()
    instance.REQUEST.RESPONSE.redirect(parent.absolute_url())
    