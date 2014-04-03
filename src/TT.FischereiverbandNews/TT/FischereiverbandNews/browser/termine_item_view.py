# Five imports
from Products.Five.browser import BrowserView

# CMFPlone imports
from Products.CMFPlone import utils

# CMFCore imports
from Products.CMFCore.utils import getToolByName

# This Module imports
from TT.FischereiverbandNews.config import *
from TT.FischereiverbandNews.utils import *

class TermineItemView(BrowserView):
    """
    """
    def getShortText(self, compact=False):
        return self.context.getShortText()
        
    def getText(self):
        return self.context.getText()
        
    def getLinksText(self):
        return self.context.getLinksText()
        
    def getParentLink(self, REQUEST=None):
        return self.context.aq_parent.absolute_url()
        
    def showFiles(self):
        f = self.context.getFirstFile()
        s = self.context.getSecondFile()
        if (f and s):
            if (f.getSize() or s.getSize()): return True
        return False
    
    def checkExistFirstFile(self):
        f = self.context.getFirstFile()
        try:
            if f.getSize(): return True
            return False
        except:
            return False
            
    def checkExistSecondFile(self):
        s = self.context.getSecondFile()
        try:
            if s.getSize(): return True
            return False
        except:
            return False
        
    def format(self, txt):
        return format(txt)