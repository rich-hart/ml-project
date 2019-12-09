from django.db import models
from django_neomodel import DjangoNode, DjangoField as DF
from django.db.models.fields import Field, AutoField
from neomodel import (
    StructuredNode, StringProperty, DateProperty, IntegerProperty, 
    StructuredRel, RelationshipTo, Relationship,
)
from django.db.models.options import Options
from users.models import Person


class Character(DjangoNode):
    name = StringProperty()
    class Meta:
        app_label = 'cinema'


class CinemaPiece(DjangoNode):
    title = StringProperty(unique_index=True)
    released = DateProperty()
    characters = RelationshipTo('Character', 'FEATURED')


class Movie(CinemaPiece):
    pass
#    class Meta:
#        app_label = 'cinema'



class Season(DjangoNode):
    number = IntegerProperty()
    episodes = Relationship('Episode', 'PRODUCED')

class Episode(DjangoNode):
    number = IntegerProperty()

class TVShow(CinemaPiece):
    seasons = Relationship('Season', 'PRODUCED')
#    class Meta:
#        app_label = 'cinema'
 

class Actor(Person):
    roles = Relationship('Character', 'ACTED_AS')

