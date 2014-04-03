from AccessControl import ClassSecurityInfo
from Products.Archetypes.Field import ObjectField, Field
from Products.Archetypes.Registry import registerField

class ListObjectsField(ObjectField):
    """A field that stores strings"""
    _properties = Field._properties.copy()
    _properties.update({
        'type' : 'string',
        'default': '',
        })
        
    security = ClassSecurityInfo()
        
    security.declarePrivate('set')
    def set(self, instance, value, **kwargs):
        if value:
            ObjectField.set(self, instance, value, **kwargs)
        
    security.declarePrivate('get')
    def get(self, instance, **kwargs):
        return ObjectField.get(self, instance, **kwargs) or None

registerField(ListObjectsField,
              title='String',
              description='Used for storing simple strings')
