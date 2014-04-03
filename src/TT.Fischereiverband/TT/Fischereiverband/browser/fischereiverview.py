from zope.interface import implements
from zope.component import getMultiAdapter

from Acquisition import aq_inner
from Products.Five import BrowserView

from interfaces import IFischereiverView

_marker = []


class FischereiverView(BrowserView):
    implements(IFischereiverView)

    # Utility methods
    def getNameOfColumn(self,view=None):
        """
        """
        context = aq_inner(self.context)
        plone_view = getMultiAdapter((context, self.request), name=u'plone')
        sl = plone_view.have_portlets('plone.leftcolumn', view=view);
        sr = plone_view.have_portlets('plone.rightcolumn', view=view);
        if not sl and not sr:
            return 'content'
        elif sl and sr:
            return 'full'
        elif sr and not sl:
            return 'right'
        elif sl and not sr :
            return 'left'
            	
    def getColumnsClass(self, view=None):
        """Determine whether a column should be shown. The left column is called
        plone.leftcolumn; the right column is called plone.rightcolumn.
        """
        context = aq_inner(self.context)
        plone_view = getMultiAdapter((context, self.request), name=u'plone')
        sl = plone_view.have_portlets('plone.leftcolumn', view=view);
        sr = plone_view.have_portlets('plone.rightcolumn', view=view);
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')

        if not sl and not sr:
            # we don't have columns, thus conten takes the whole width
            return "one-column"
        elif sl and sr:
            # In case we have both columns, content takes 50% of the whole
            # width and the rest 50% is spread between the columns
            return "three-column"
        elif (sr and not sl) and (not portal_state.is_rtl()):
            # We have right column and we are NOT in RTL language
            return "three-column two-column-right"
        elif (sl and not sr) and (not portal_state.is_rtl()):
            # We have left column and we are in NOT RTL language
            return "three-column two-column-left"