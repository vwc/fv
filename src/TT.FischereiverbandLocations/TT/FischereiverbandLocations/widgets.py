from Products.Archetypes.Widget import TypesWidget
from Products.Archetypes.Registry import registerWidget

class LocationAreaWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "widgets/location_area_widget",
        'blurrable' : True,
        })

registerWidget(LocationAreaWidget,
               title='List',
               description=(''),
               used_for=('TT.FischereiverbandLocations.fields.LocationAreaField',)
               )
