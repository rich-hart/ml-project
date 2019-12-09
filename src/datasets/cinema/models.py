from django.db import models
from django_neomodel import DjangoNode
from neomodel import StructuredNode, StringProperty, DateProperty

class Movie(DjangoNode):
    title = StringProperty(unique_index=True)
    released = DateProperty()
    class Meta:
        app_label = 'cinema'

class TVShow(DjangoNode):
    title = StringProperty(unique_index=True)
    released = DateProperty()
    class Meta:
        app_label = 'cinema'
