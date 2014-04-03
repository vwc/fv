def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('TT.Fischereiverband_various.txt') is None:
        return

    # Add additional setup code here
    site = context.getSite()
    importDefaultContents(site)
    setNavDisplayedTypes(site)
    deleteSiteActions(site)

import os
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter

def importDefaultContents(context):
    listing = []
    impath = os.path.dirname(__file__) + os.path.sep + 'import'
    directory = os.path.join(impath)
    if os.path.isdir(directory):
        listing = [f for f in os.listdir(directory) if f.endswith('.zexp')]
        listing.sort()

    for imfile in listing:
        name = imfile.split('.zexp')[0]
        filepath = impath + os.path.sep + imfile
        obj = getattr(context, name, None)
        if obj: continue # object already exist
        context._importObjectFromFile(filepath)

def setNavDisplayedTypes(context):
    # hide image object from navigation
    pprop = getToolByName(context, 'portal_properties')
    navProps = pprop.navtree_properties
    navProps._updateProperty('metaTypesNotToList', ['File',
                                                    'Image',
                                                    'Material',
                                                    'LocationItem', 
                                                    'NachrichtenItem',
                                                    'TermineItem',
                                                    'Event',
                                                    'News Item',
                                                    'Link'])

    # exclude default folders from Navigation
    for name in ['news', 'events', 'Members']:
        obj = getattr(context, name, None)
        if not obj: continue
        obj.setExcludeFromNav(True)
        obj.reindexObject()

def deleteSiteActions(context):
    atool = getToolByName(context,'portal_actions')
    try:
        site_actions =atool.site_actions
        action_info = site_actions.listActions()
        for info in action_info:
            info_id = info.getId()
            if info_id in ['plone_setup','sitemap','accessibility','contact']:
                site_actions.manage_delObjects(info_id)
        portal_tabs=atool.portal_tabs 
        tab_info = portal_tabs.listActions()
        for tab in tab_info:
            tab_id = tab.getId()
            if tab_id == 'index_html':
                portal_tabs.manage_delObjects(tab_id)
    except Exception,error:
        print 'Erorr: ', error
        

    


