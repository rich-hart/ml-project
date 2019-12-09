from django.db import models

from django_neomodel import DjangoNode
from neomodel import (
    StructuredNode, StringProperty, RelationshipTo, Relationship,
    DateProperty,
)
class Person(DjangoNode):
    name = StringProperty()
    born = DateProperty() 
    class Meta:
        app_label = 'users'

