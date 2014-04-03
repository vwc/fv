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

class TermineContentView(BrowserView):
    """
    """
    def getParentLink(self, REQUEST=None):
        return self.context.absolute_url()

    def showFiles(self,termine):
        f = termine.getFirstFile()
        s = termine.getSecondFile()
        if (f and s):
            if (f.getSize() or s.getSize()): return True
        return False
    
    def checkExistFirstFile(self,termine):
        f = termine.getFirstFile()
        try:
            if f.getSize(): return True
            return False
        except:
            return False
            
    def checkExistSecondFile(self,termine):
        s = termine.getSecondFile()
        try:
            if s.getSize(): return True
            return False
        except:
            return False
        
    def redirectToParent(self):
        destination = self.getParentLink()
        return self.context.REQUEST.RESPONSE.redirect(destination)
        
    def queryCatalog(self,termine_id, REQUEST=None,review_state=None):
        """
        """
        if REQUEST is None:
            REQUEST = getattr(self.context, 'REQUEST', {})

        q = {'portal_type'  : 'TermineItem', 
             'sort_on'      : 'effective',
             'sort_order'   : 'reverse'}
             
        if review_state: q['review_state'] = review_state
        # Quering
        pcatalog = getToolByName(self, 'portal_catalog')
        results = pcatalog.searchResults(REQUEST, **q)
        termine = ''
        for result in results:
            item = result.getObject()
            item_id = item.getId()
            if item_id == termine_id:
                termine = item
        return termine
