from plone.memoize import ram
from plone.memoize.compress import xhtml_compress
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.layout.navigation.root import getNavigationRootObject
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from zope import schema

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.cache import render_cachekey
from plone.app.portlets.portlets import base

from TT.FischereiverbandNews.utils import *

class INewsPortlet(IPortletDataProvider):

    count = schema.Int(title=_(u'Number of items to display'),
                       description=_(u'How many items to list.'),
                       required=True,
                       default=3)
                       
    forChildren = schema.Bool(title=_(u'For children'),
                        description=_(u'If selected, the children can see this content'),
                        default=False)

class Assignment(base.Assignment):
    implements(INewsPortlet)

    def __init__(self, count=5, state=('published', ), forChildren=False):
        self.count = count
        self.state = state
        self.forChildren = forChildren
        

    @property
    def title(self):
        return _(u"News")

class Renderer(base.Renderer):

    _template = ViewPageTemplateFile('news.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    #@ram.cache(render_cachekey)
    def render(self):
        return xhtml_compress(self._template())

    @property
    def available(self):
        return len(self._data())

    def published_news_items(self):
        return self._data()
        
        
    def format(self, txt):
        return format(txt)
        
    def getDatumFomat(self, dateTime):
        return dateTimeToString(dateTime)

    def all_news_link(self):
        return None
        
    def getTypeObject(self, object):
        return getTypeObject(object)

    @memoize
    def _data(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path()
        limit = self.data.count
        state = self.data.state
        results = catalog(portal_type='NachrichtenItem',
                       review_state=state,
                       path=path,
                       sort_on='effective',
                       sort_order='reverse')
#        return catalog(portal_type='NachrichtenItem',
#                       review_state=state,
#                       path=path,
#                       sort_on='effective',
#                       sort_order='reverse',
#                       sort_limit=limit)[:limit]
        if self.data.forChildren:
            results = [obj for obj in results if obj.getObject().getForChildren()==self.data.forChildren]
        return results[0:limit]

class AddForm(base.AddForm):
    form_fields = form.Fields(INewsPortlet)
    label = _(u"Add News Portlet")
    description = _(u"This portlet displays recent News Items.")

    def create(self, data):
        return Assignment(count=data.get('count', 3), state=data.get('state', ('published',)), forChildren=data.get('forChildren', False))

class EditForm(base.EditForm):
    form_fields = form.Fields(INewsPortlet)
    label = _(u"Edit News Portlet")
    description = _(u"This portlet displays recent News Items.")
