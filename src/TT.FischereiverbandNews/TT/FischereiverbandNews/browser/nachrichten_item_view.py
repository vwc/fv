# Five imports
from Products.Five.browser import BrowserView

# CMFPlone imports
from Products.CMFPlone import utils

# CMFCore imports
from Products.CMFCore.utils import getToolByName

# This Module imports
from TT.FischereiverbandNews.config import *
from TT.FischereiverbandNews.utils import *

class NachrichtenItemView(BrowserView):
    """
    """
    def getShortText(self, compact=False):
        return self.context.getShortText()
        
    def getText(self):
        return self.context.getText()
        
    def getParentLink(self, REQUEST=None):
        return self.context.aq_parent.absolute_url()
        
    def getImages(self):
        objItems = self.context.objectItems()
        return [item[1] for item in objItems]   
        
    def format(self, txt):
        return format(txt)