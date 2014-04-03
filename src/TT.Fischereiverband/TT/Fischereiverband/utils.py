from TT.Fischereiverband.config import MAX_TEXT_PREVIEW
from AccessControl.SecurityInfo import ModuleSecurityInfo
from AccessControl.SecurityInfo import ClassSecurityInfo

import re
from DateTime.DateTime import DateTime

security = ModuleSecurityInfo('TT.Fischereiverband.utils')

security.declarePublic('remove_html_tags')
def remove_html_tags(txt):
    p = re.compile(r'<.*?>')
    return p.sub('', txt)

security.declarePublic('back_space')
def back_space(txt, MAX_PREVIEW=300):
    if not txt: return ''
    if len(txt) <= MAX_PREVIEW: return txt
    m = MAX_PREVIEW
    while (txt[m] != ' '): m += 1
    return txt[0:m]+'...'

security.declarePublic('format')
def format(txt, MAX_PREVIEW=300):
    txt = remove_html_tags(txt)
    return back_space(txt, MAX_TEXT_PREVIEW)
