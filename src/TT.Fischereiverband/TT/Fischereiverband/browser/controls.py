from zope.interface import implements
from zope.component import getMultiAdapter

from Acquisition import aq_inner
from Products.Five import BrowserView

from interfaces import IFischereiverView


class MapsControl(BrowserView):
    implements(IFischereiverView)

    def maps_control_submit(self):
        maps_company_address = self.context.REQUEST.get('company_address')
        maps_api_key = self.context.REQUEST.get('api_key')
        tool = self.context.FischereiverbandTool
        tool.maps_api_key = maps_api_key
        tool.maps_company_address = maps_company_address
        return self.context.REQUEST.RESPONSE.redirect('@@maps-controlpanel')
        
class MailControl(BrowserView):
    implements(IFischereiverView)

    def mail_control_submit(self):
        material_mail = self.context.REQUEST.get('material_mail')
        tool = self.context.FischereiverbandTool
        tool.materials_mail = eval(material_mail)
        return self.context.REQUEST.RESPONSE.redirect('@@materialmail-controlpanel')