from Products.Archetypes.Registry import registerWidget,registerPropertyType
from AccessControl import ClassSecurityInfo
from types import StringType
from Products.Archetypes.utils import shasattr
from Products.Archetypes.Widget import TypesWidget

class ImagesWidget(TypesWidget):
	_properties = TypesWidget._properties.copy()
	_properties.update({
		'macro' : "ImagesMacro",
	})
	security = ClassSecurityInfo()

registerWidget(ImagesWidget,
               title='ImagesWidget',
               description=('This widget that allows you to upload '
                            'other images')
               )
