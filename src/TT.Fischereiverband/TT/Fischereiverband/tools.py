from App.class_init import InitializeClass
from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.utils import UniqueObject
from Products.CMFPlone.PloneBaseTool import PloneBaseTool
from Products.CMFPlone.utils import safe_unicode
from Products.CMFPlone.browser.navtree import getNavigationRoot


class FischereiverbandTool(SimpleItem, UniqueObject, PloneBaseTool):
	""" FischereiverbandTool
	"""
	meta_type	   = 'PicturesEdit Tool'
	security		= ClassSecurityInfo()
	randStyle	   = ''

	implements	 = (PloneBaseTool, SimpleItem, )
	
	maps_api_key = 'ABQIAAAA2nYaRSxqJ2fFShiGSyaIAhQgCipEkmNSAXz9OLOESzSt8Qd8ChTCSpc8903NlwAUOxt-tejL6ju4Qg'
	maps_company_address = '1395 3 thang 2, Ho chi minh'
	materials_mail =[]

InitializeClass(FischereiverbandTool)


