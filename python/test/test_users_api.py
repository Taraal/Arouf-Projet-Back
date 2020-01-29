# coding: utf-8

"""
    API de gestion des messages entre utilisateurs

    Api Messages  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: sylouan.corfa@epsi.fr
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user(self):
        """Test case for add_user

        Ajoute un utilisateur  # noqa: E501
        """
        pass

    def test_authenticate(self):
        """Test case for authenticate

        Permet à un utilisateur de s'identifier  # noqa: E501
        """
        pass

    def test_error_get(self):
        """Test case for error_get

        Teste le reporting Sentry  # noqa: E501
        """
        pass

    def test_get_all(self):
        """Test case for get_all

        Récupère tous les users de la DB  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Trouve un utilisateur précis  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
