from TT.FischereiverbandNews.config import MAX_TEXT_PREVIEW
import re
from DateTime.DateTime import DateTime

def remove_html_tags(txt):
    p = re.compile(r'<.*?>')
    return p.sub('', txt)

def back_space(txt, MAX_PREVIEW=300):
    if not txt: return ''
    if txt.split()==[]: return ''
    if len(txt) <= MAX_PREVIEW: return txt
    m = MAX_PREVIEW
    while (txt[m] != ' '): m -= 1
    return txt[0:m]+'...'
    
def format(txt, MAX_PREVIEW=300):
    txt = remove_html_tags(txt)
    return back_space(txt, MAX_TEXT_PREVIEW)
    
def getTypeObject(object):
    return object.meta_type
    
def dateTimeToString(dateTime):
    return DateTime(dateTime).toZone('GMT').strftime('%d.%m.%Y')