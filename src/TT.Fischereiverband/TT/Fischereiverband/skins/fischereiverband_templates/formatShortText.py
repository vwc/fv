## Controller Python Script "formatShortText"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= txt, maxview
##title= formatShortText.
from TT.Fischereiverband.utils import format
return format(txt,maxview)
