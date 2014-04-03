from plone.theme.interfaces import IDefaultPloneLayer


class IFischereiverbandNewsLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "FischereiverbandNews" theme, this interface must be its layer
       (in FischereiverbandNews/viewlets/configure.zcml).
    """
