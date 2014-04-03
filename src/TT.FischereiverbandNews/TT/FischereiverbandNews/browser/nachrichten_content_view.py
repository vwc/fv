# Five imports
from Products.Five.browser import BrowserView

# CMFPlone imports
from Products.CMFPlone import utils
from Products.CMFPlone.PloneBatch import Batch

# CMFCore imports
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.utils import decode

# This Module imports
from TT.FischereiverbandNews.config import *
from TT.FischereiverbandNews.utils import *

class NachrichtenContentView(BrowserView):
    """
    """
    def getParentLink(self, REQUEST=None):
        return self.context.aq_parent.absolute_url()

    def getImages(self,nachrichten):
        objItems = nachrichten.objectItems()
        return [item[1] for item in objItems]   
        
    def redirectToParent(self):
        destination = self.getParentLink()
        return self.context.REQUEST.RESPONSE.redirect(destination)
        
    def queryCatalog(self,nachrichten_id, REQUEST=None,review_state=None):
        """
        """
        if REQUEST is None:
            REQUEST = getattr(self.context, 'REQUEST', {})

        q = {'portal_type'  : 'NachrichtenItem', 
             'sort_on'      : 'effective',
             'sort_order'   : 'reverse'}
             
        if review_state: q['review_state'] = review_state
        # Quering
        pcatalog = getToolByName(self, 'portal_catalog')
        results = pcatalog.searchResults(REQUEST, **q)
        nachricten = ''
        for result in results:
            item = result.getObject()
            item_id = item.getId()
            if item_id == nachrichten_id:
                nachricten = item
        return nachricten
