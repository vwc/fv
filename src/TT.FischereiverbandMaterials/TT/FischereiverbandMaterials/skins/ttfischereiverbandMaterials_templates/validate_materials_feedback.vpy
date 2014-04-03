## Controller Script Python "validate_materials_feedback"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state  
##bind subpath=traverse_subpath
##parameters=club,fullname,street,city,phone,material_number
##title=validates the form for sending feedback

from Products.CMFPlone import PloneMessageFactory as _
reg_tool=context.portal_registration 

if not (club and club.strip()):
    state.setError('club', _(u'Please enter your club.'), 'club_required')

if not (fullname and fullname.strip()):
    state.setError('fullname', _(u'Please enter your full name'), 'fullname_required')

if not (street and street.strip()):
    state.setError('street', _(u'Please enter your street'), 'street_required')

if not (city and city.strip()):
    state.setError('city', _(u'Please enter your city'), 'city_required')

if not (phone and phone.strip()):
    state.setError('phone', _(u'Please enter your phone'), 'phone_required')

isSelectMaterial = False
for material in material_number:
    if material: isSelectMaterial = True

if not isSelectMaterial:
    state.setError('materials', _(u'Please select materials'), 'materials_required')

if state.getErrors():
    context.plone_utils.addPortalMessage(_(u'Please correct the indicated errors.'), 'error')
    return state.set(status='failure')
else:
    return state
