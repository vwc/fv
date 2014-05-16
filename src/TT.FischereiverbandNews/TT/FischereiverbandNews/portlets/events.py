from plone.memoize.instance import memoize
from plone.memoize import ram
from plone.memoize.compress import xhtml_compress
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.layout.navigation.root import getNavigationRootObject
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from zope import schema

from Acquisition import aq_inner
from DateTime.DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.cache import render_cachekey
from plone.app.portlets.portlets import base

from TT.FischereiverbandNews.utils import *


class IEventsPortlet(IPortletDataProvider):

    count = schema.Int(
        title=_(u'Number of items to display'),
        description=_(u'How many items to list.'),
        required=True,
        default=10
    )

    state = schema.Tuple(
        title=_(u"Workflow state"),
        description=_(u"Items in which workflow state to show."),
        default=('published', ),
        required=True,
        value_type=schema.Choice(
            vocabulary="plone.app.vocabularies.WorkflowStates")
    )

    forChildren = schema.Bool(
        title=_(u'For children'),
        description=_(u'If selected, the children can see this content'),
        default=False
    )


class Assignment(base.Assignment):
    implements(IEventsPortlet)

    def __init__(self, count=10, state=('published', ), forChildren=False):
        self.count = count
        self.state = state
        self.forChildren = forChildren

    @property
    def title(self):
        return _(u"Events")


class Renderer(base.Renderer):

    _template = ViewPageTemplateFile('events.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        self.anonymous = portal_state.anonymous()
        self.navigation_root_url = portal_state.navigation_root_url()
        self.portal = portal_state.portal()
        self.navigation_root_path = portal_state.navigation_root_path()
        self.navigation_root_object = getNavigationRootObject(self.context,
                                                              self.portal)

    #@ram.cache(render_cachekey)
    def render(self):
        return xhtml_compress(self._template())

    @property
    def available(self):
        return not self.anonymous and \
            self.data.count > 0 and \
            len(self._data())

    def published_events(self):
        return self._data()

    @memoize
    def have_events_folder(self):
        return 'events' in self.navigation_root_object.objectIds()

    def all_events_link(self):
        navigation_root_url = self.navigation_root_url
        if self.have_events_folder():
            return '%s/events' % navigation_root_url
        else:
            return '%s/events_listing' % navigation_root_url

    def prev_events_link(self):
        # take care dont use self.portal here since support
        # of INavigationRoot features likely will breake #9246 #9668
        if (self.have_events_folder() and
            'aggregator' in self.navigation_root_object['events'].objectIds() and
            'previous' in self.navigation_root_object['events']['aggregator'].objectIds()):
            return '%s/events/aggregator/previous' % self.navigation_root_url
        elif (self.have_events_folder() and
            'previous' in self.navigation_root_object['events'].objectIds()):
            return '%s/events/previous' % self.navigation_root_url
        return None

    def getDatumFomat(self, dateTime):
        return dateTimeToString(dateTime)

    def getTypeObject(self, object):
        return getTypeObject(object)

    def checkForChildren(self):
        t = self.getTypeObject(self.context)
        if t=='Termine' or t=='TermineItem':
            return self.context.getForChildren()
        return False

    def getViewMoreLink(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        result = catalog(portal_type='Termine',
                       review_state='published')
        forChildren = False
        t = self.getTypeObject(self.context)
        if t=='Termine' or t=='TermineItem':
            if self.context.getForChildren(): forChildren = True
        for res in result:
            if res.getObject().getForChildren() == forChildren:
                return res
        return None

    @memoize
    def _data(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        limit = self.data.count
        state = self.data.state
        path = self.navigation_root_path
        results = catalog(portal_type='TermineItem',
                          review_state=state,
                          path=path,
                          sort_on='start',
                          sort_order='ascending')

        if self.data.forChildren:
            results = [obj for obj in results if obj.getObject().getForChildren()==self.data.forChildren]
        return results[0:limit]

class AddForm(base.AddForm):
    form_fields = form.Fields(IEventsPortlet)
    label = _(u"Add Events Portlet")
    description = _(u"This portlet lists upcoming Events.")

    def create(self, data):
        return Assignment(count=data.get('count', 10), state=data.get('state', ('published',)), forChildren=data.get('forChildren', False))

class EditForm(base.EditForm):
    form_fields = form.Fields(IEventsPortlet)
    label = _(u"Edit Events Portlet")
    description = _(u"This portlet lists upcoming Events.")
