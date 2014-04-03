from AccessControl import ClassSecurityInfo
from Products.Archetypes.Widget import TypesWidget

class VorstandSelectionWidget(TypesWidget):
	_properties = TypesWidget._properties.copy()
	_properties.update({
		'macro' : "VorstandSelectionWidget",
		'size'	: 5,	
	})
	
	security = ClassSecurityInfo()