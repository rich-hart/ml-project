import ipdb; ipdb.set_trace()
from rest_framework.test import APITestCase
from django.urls import reverse

from neomodel import db, clear_neo4j_database

from .models import *

class MyTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        pass
#        cls.movie = Movie.objects.create(title='test')
        # Set up data for the whole TestCase
        #cls.foo = Foo.objects.create(bar="Test")
        #...

    def setUp(self):
        clear_neo4j_database(db)

    def test1(self):
        import ipdb; ipdb.set_trace()
        url = reverse('movie-list')
        data = {'title': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
#        response = self.client.get('/movies', format='json', follow=True)
       
        # Some test using self.foo
        #...

    def test2(self):
        pass
        # Some other test using self.foo
        #...