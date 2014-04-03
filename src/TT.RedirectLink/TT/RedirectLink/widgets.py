from Products.Archetypes.Widget import TypesWidget
from Products.Archetypes.Registry import registerWidget

class ListObjectsWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "widgets/list_objects_widget",
        })

registerWidget(ListObjectsWidget,
               title='List Objects Internal',
               description=(''),
               used_for=('TT.RedirectLink.fields.ListObjectsField',)
               )
