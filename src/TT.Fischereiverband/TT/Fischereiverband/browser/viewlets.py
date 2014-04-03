from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import GlobalSectionsViewlet, ViewletBase
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter

class GlobalSectionsViewlet(GlobalSectionsViewlet):
    def selectedTabs(self, default_tab='aktuelles', portal_tabs=()):
        plone_url = getToolByName(self.context, 'portal_url')()
        plone_url_len = len(plone_url)
        request = self.request
        valid_actions = []

        url = request['URL']
        path = url[plone_url_len:]

        for action in portal_tabs:
            if not action['url'].startswith(plone_url):
                continue
            action_path = action['url'][plone_url_len:]
            if not action_path.startswith('/'):
                action_path = '/' + action_path
            if path.startswith(action_path):
                valid_actions.append((len(action_path), action['id']))
        valid_actions.sort()
        if valid_actions:
            return {'portal' : valid_actions[-1][1]}

        return {'portal' : default_tab}
        
    render = ViewPageTemplateFile('sections.pt')

class MetaActionsViewlet(ViewletBase):
    index = ViewPageTemplateFile('meta_actions.pt')

    def update(self):
        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')
        self.meta_actions = context_state.actions('meta_actions')
