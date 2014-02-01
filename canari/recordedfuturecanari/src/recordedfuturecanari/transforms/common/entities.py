#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule

__author__ = 'Christian Heinrich'
__copyright__ = 'Copyright 2014, Recordedfuturecanari Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Christian Heinrich'
__email__ = 'christian.heinrich@cmlh.id.au'
__status__ = 'Development'

__all__ = [
    'RecordedfuturecanariEntity',
    'MyRecordedfuturecanariEntity'
]

"""
DO NOT EDIT:
The following entity is the base entity type from which all your entities will inherit from. This provides you with the
default namespace that all your entities will use for their unique entity type in Maltego. For example, MyRecordedfuturecanariEntity will
have an entity type name of recordedfuturecanari.MyRecordedfuturecanariEntity. When adding a new entity in Maltego, you will have to specify this
name (recordedfuturecanari.MyRecordedfuturecanariEntity) in the 'Unique entity type' field.
"""
class RecordedfuturecanariEntity(Entity):
    namespace = 'recordedfuturecanari'


"""
You can specify as many entity fields as you want by just adding an extra @EntityField() decorator to your entities. The
@EntityField() decorator takes the following parameters:
    - name: the name of the field without spaces or special characters except for dots ('.') (required)
    - propname: the name of the object's property used to get and set the value of the field (required, if name contains dots)
    - displayname: the name of the entity as it appears in Maltego (optional)
    - type: the data type of the field (optional, default: EntityFieldType.String)
    - required: whether or not the field's value must be set before sending back the message (optional, default: False)
    - choices: a list of acceptable field values for this field (optional)
    - matchingrule: whether or not the field should be loosely or strictly matched (optional, default: MatchingRule.Strict)
    - decorator: a function that is invoked each and everytime the field's value is set or changed.
TODO: define as many custom fields and entity types as you wish:)
"""    
@EntityField(name='recordedfuturecanari.fieldN', propname='fieldN', displayname='Field N', matchingrule=MatchingRule.Loose)
@EntityField(name='recordedfuturecanari.field1', propname='field1', displayname='Field 1', type=EntityFieldType.Integer)
class MyRecordedfuturecanariEntity(RecordedfuturecanariEntity):
    """
    Uncomment the line below and comment out the pass if you wish to define a ridiculous entity type name like
    'my.fancy.EntityType'
    """
    # name = my.fancy.EntityType
    pass