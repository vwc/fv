from plone.app.portlets.portlets.navigation import Renderer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class TT_NavigationRenderer(Renderer):
    _template = ViewPageTemplateFile('navigation.pt')
    recurse = ViewPageTemplateFile('navigation_recurse.pt')