## Controller Python Script "getAchivByYear"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=year
##title=getAchivByYear
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
archives= []

if year:
    path = '/'.join(context.getPhysicalPath())
    pcatalog = getToolByName(context, 'portal_catalog')
    results = pcatalog.searchResults(portal_type= 'NachrichtenItem',
                                        sort_on= 'effective',sort_order= 'reverse',review_state='published')
    for result in results:
        obj = result.getObject()
        obj_date = DateTime(obj.Date()).toZone('GMT')
        obj_year = obj_date.year()
        if str(obj_year) == str(year):
            archives.append(obj)
    return archives
return []                
    
