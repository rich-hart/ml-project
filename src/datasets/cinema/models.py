from django.db import models
from django_neomodel import DjangoNode, DjangoField as DF
from django.db.models.fields import Field, AutoField
from neomodel import StructuredNode, StringProperty, DateProperty, IntegerProperty
from django.db.models.options import Options

#class StringField(AutoField, StringProperty):
#    pass
#class StringField(AutoField, StringProperty):
#    def __init__(self, unique_index=None, name=None, *args, **kwargs):
#        super(AutoField, self).__init__(*args, **kwargs)
#        super(StringProperty, self).__init__(unique_index,*args, **kwargs)
#        self.serialize = True
#        self.remote_field = False
#        self.name = name
#
#class IntegerField(AutoField, IntegerProperty):
#    def __init__(self, unique_index=None, name=None, *args, **kwargs):
#        super(AutoField, self).__init__(*args, **kwargs)
#        super(IntegerProperty, self).__init__(unique_index,*args, **kwargs)
#        self.serialize = True
#        self.remote_field = False
#        self.name = name
#class DjangoField(DF,Field):
##    @property
##    def name(self):
##        import ipdb; ipdb.set_trace()
##        pass
#
#    def __init__(self,prop,key,unique_index=None,*args, **kwargs):
#        super(Field,self).__init__(*args, **kwargs)
#        super(DjangoField,self).__init__(prop,key,*args, **kwargs)
#        self.serialize = True
#        self.remote_field = False
#        self.name = key
#        self.unique_for_date = False
#        self.unique_for_month = False
#        self.unique_for_year = False 
#def classproperty(f):
#    class cpf(object):
#        def __init__(self, getter):
#            self.getter = getter
#
#        def __get__(self, obj, type=None):
#            return self.getter(type)
#    return cpf(f)

#class BaseNode(DjangoNode):
#    @classproperty
#    def _meta(self):
#        if hasattr(self.Meta, 'unique_together'):
#            raise NotImplementedError('unique_together property not supported by neomodel')
#
#        opts = Options(self.Meta, app_label=self.Meta.app_label)
#        opts.contribute_to_class(self.__class__, self.__class__.__name__)
#        opts.concrete_model = self
#        opts.pk = self.pk
#        for key, prop in self.__all_properties__:
#            opts.add_field(DjangoField(prop, key), getattr(prop, 'private', False))
#
#        return opts

class Movie(DjangoNode):
#    pk = IntegerField(unique_index=True,name='pk')
#    id = IntegerField(unique_index=True,name='id')
    title = StringProperty(unique_index=True)
#    released = DateProperty()

    class Meta:
        app_label = 'cinema'
#        concrete_model = Movie
class TVShow(DjangoNode):
#    pk = IntegerField(unique_index=True,name='pk')
#    id = IntegerField(unique_index=True,name='id')
    title = StringProperty(unique_index=True)
#    released = DateProperty()
    class Meta:
        app_label = 'cinema'
#        concrete_model = TVShow
