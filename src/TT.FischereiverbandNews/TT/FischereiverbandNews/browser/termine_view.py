# Five imports
from Products.Five.browser import BrowserView

# CMFPlone imports
from Products.CMFPlone import utils
from Products.CMFPlone.PloneBatch import Batch

# CMFCore imports
from Products.CMFCore.utils import getToolByName

# This Module imports
from TT.FischereiverbandNews.config import *
from TT.FischereiverbandNews.utils import *

class TermineView(BrowserView):
    """
    """
    def getShortText(self):
        return self.context.getShortText()
        
    def getForChildren(self):
        return self.context.getForChildren()
        
    def getDatumFomat(self, dateTime):
        return dateTimeToString(dateTime)
        
    def getUserFullName(self, user):
        try:
            return user.getProperty('fullname', user.getId())
        except:
            return user.getId()
        
    def queryCatalog(self, 
                    REQUEST=None, 
                    batch=False, 
                    b_size=None,
                    review_state=None,
                    for_children=None,
                    show_all=False):
        # Get request info
        if REQUEST is None:
            REQUEST = getattr(self.context, 'REQUEST', {})
        b_start = REQUEST.get('b_start', 0)
        b_size = b_size or ITEMS_PER_PAGE
        
        # Query's arguments default
        q = {'portal_type'  : 'TermineItem', 
             'sort_on'      : 'effective',
             'sort_order'   : 'reverse'}
             
        # review_state
        if review_state: q['review_state'] = review_state
        
        # for_children
        #if for_children: q['forChildren'] = for_children
        
        # show_all
        if show_all:
            q['show_all'] = 1
            q['show_inactive'] = 1
        
        # Quering
        pcatalog = getToolByName(self, 'portal_catalog')
        results = pcatalog.searchResults(REQUEST, **q)

        # FIX ME:
        if for_children:
            results = [obj for obj in results if obj.getObject().getForChildren()==for_children]
            
        # Create a batch
        if batch:
            batch = Batch(results, b_size, int(b_start), orphan=0)
            return batch
        return results
        
    def format(self, txt):
        return format(txt)
