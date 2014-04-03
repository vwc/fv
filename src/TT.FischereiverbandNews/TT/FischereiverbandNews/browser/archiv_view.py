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
import datetime
from DateTime import DateTime
class ArchivView(BrowserView):
    """
    """
    def queryCatalog(self, 
                    REQUEST=None, 
                    batch=False, 
                    b_size=None,
                    review_state=None,
                    show_all=False):
        # Get request info
        if REQUEST is None:
            REQUEST = getattr(self.context, 'REQUEST', {})
        b_start = REQUEST.get('b_start', 0)
        b_size = b_size or ITEMS_PER_PAGE
        
        # Query's arguments default
        q = {'portal_type'  : 'NachrichtenItem', 
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

        # Create a batch
        if batch:
            batch = Batch(results, b_size, int(b_start), orphan=0)
            return batch
        return results
        
    def availableYear(self):
        now = datetime.datetime.now()
        curentYear = now.year
        available = [curentYear]
        pcatalog = getToolByName(self, 'portal_catalog')
        results = pcatalog.searchResults(portal_type= 'NachrichtenItem',
                                        sort_on= 'effective',sort_order= 'reverse',review_state='published')
        for result in results:
            obj = result.getObject()
            obj_date = DateTime(obj.Date()).toZone('GMT')
            obj_year = obj_date.year()
            if obj_year not in available:
                available.append(obj_year)
        return available
        


        
    def format(self, txt):
        return format(txt)
