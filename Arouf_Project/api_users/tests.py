from django.test import TestCase
from django.urls import reverse
import os
import django

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

os.environ['DJANGO_SETTINGS_MODULE'] = 'arouf_projects.settings'

class UserTest(APITestCase):

    django.setup()
    client = APIClient()

    def test_addUser(self):
        response = self.client.post(reverse('api_users:addUser'), data={"prenom": "prenom", "nom": "nom",
                                                             'email':'nomprenom@test.fr', 'username':'nomprenom',
                                                             'password': 'test'
                                                             })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode("utf-8") , 'True')

    def test_getAllUsers(self):
        response = self.client.get(reverse('api_users:getAllUsers'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('nom' in response.content.decode("utf-8"), True)
        self.assertGreater(len(response.content), 0)

    def test_auth(self):
        response = self.client.post(reverse('api_users:authenticate'), data={'username': 'titu', 'password':'titi'})

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_getUser(self):
        response = self.client.get(reverse('api_users:getUser'), data={'username': 'titu'}, format='json')






# Create your tests here.
