from Products.Archetypes.Field import ObjectField, Field
from Products.Archetypes.Registry import registerField

class LocationAreaField(ObjectField):
    """A field that stores strings"""
    _properties = Field._properties.copy()
    _properties.update({
        'type' : 'string',
        'default': '',
        })

registerField(LocationAreaField,
              title='String',
              description='Used for storing simple strings')
