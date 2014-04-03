from AccessControl import ClassSecurityInfo
from Products.Archetypes.Field import Field
from Products.Archetypes.Field import ObjectField
from Products.Archetypes.Field import encode, decode

from Products.Archetypes.Registry import registerField

from TT.Fischereiverband.Widget import VorstandSelectionWidget

class VorstandListField(ObjectField):
    """Used for storing list of user"""
    
    _properties = Field._properties.copy()
    _properties.update({
        'type'      : 'list',
        'default'   : (),
        'widget'    : VorstandSelectionWidget,
    })
    
    security = ClassSecurityInfo()
    
    security.declarePrivate('set')
    def set(self, instance, value, **kwargs):
        if type(value).__name__ == 'str':
            value = [value]    
        ObjectField.set(self, instance, value, **kwargs)

    security.declarePrivate('get')
    def get(self, instance, **kwargs):
        value = ObjectField.get(self, instance, **kwargs) or ()
        return [v for v in value]

registerField(VorstandListField,
              title='VorstandListField',
              description=('Used for storing list vorstand'))