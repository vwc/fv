## Controller Python Script "send_feedback_site"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=Send feedback to portal administrator
##
REQUEST=context.REQUEST

# context.plone_log('->> send_feedback_site')

from Products.CMFPlone.utils import transaction_note
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _
from ZODB.POSException import ConflictError

##
## This may change depending on the called (portal_feedback or author)
state_success = "success"
state_failure = "failure"

plone_utils = getToolByName(context, 'plone_utils')
urltool = getToolByName(context, 'portal_url')
portal = urltool.getPortalObject()
url = urltool()

# club,organisation,full_name,member_number,street,city,phone
## make these arguments?
club = REQUEST.get('club', '')
organisation = REQUEST.get('organisation', '')
fullname = REQUEST.get('fullname', '')
member_number = REQUEST.get('member_number', '')
street = REQUEST.get('street', '')
city = REQUEST.get('city', '')
phone = REQUEST.get('phone', '')

materials_id = REQUEST.get('material_id', [])
materials_name = REQUEST.get('material_name', [])
materials_price = REQUEST.get('material_price', [])
materials_number = REQUEST.get('material_number', [])

materials = []
for idx in range(len(materials_id)):
    if (materials_number[idx]):
        materials.append({
            'id': materials_id[idx],
            'name': materials_name[idx],
            'price': materials_price[idx],
            'number': materials_number[idx],
        })

send_to_address = portal.getProperty('email_from_address')
envelope_from = portal.getProperty('email_from_address')

state.set(status=state_success) ## until proven otherwise

host = context.MailHost # plone_utils.getMailHost() (is private)
encoding = portal.getProperty('email_charset')

variables = {
    'club'          : club,
    'organisation'  : organisation,
    'fullname'      : fullname,
    'member_number' : member_number,
    'street'        : street,
    'city'          : city,
    'phone'         : phone,
    'materials'     : materials
}
materials_mail = context.FischereiverbandTool.materials_mail

try:
    subject = ''
    message = context.materials_feedback_template(context, **variables)
    message = message.encode(encoding)
    # we do'nt send mail to admin, we send to email list get in material mail config.
    #result = host.send(message, send_to_address, envelope_from,
                       #subject=subject, charset=encoding)
    if materials_mail:
        for email in materials_mail:
            results = host.send(message, email, envelope_from,
                       subject=subject, charset=encoding)

        
except ConflictError:
    raise
except: # TODO Too many things could possibly go wrong. So we catch all.
    exception = plone_utils.exceptionString()
    message = _(u'Unable to send mail: ${exception}',
                mapping={u'exception' : exception})
    plone_utils.addPortalMessage(message, 'error')
    return state.set(status=state_failure)

## clear request variables so form is cleared as well
REQUEST.set('club', None)
REQUEST.set('organisation', None)
REQUEST.set('fullname', None)
REQUEST.set('member_number', None)
REQUEST.set('street', None)
REQUEST.set('city', None)
REQUEST.set('phone', None)

plone_utils.addPortalMessage(_(u'Mail sent.'))
return state
