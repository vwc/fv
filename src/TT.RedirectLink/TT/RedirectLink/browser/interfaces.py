from plone.theme.interfaces import IDefaultPloneLayer


class IRedirectLinkLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "RedirectLink" theme, this interface must be its layer
       (in RedirectLink/viewlets/configure.zcml).
    """
