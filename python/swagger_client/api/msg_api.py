# coding: utf-8

"""
    API de gestion des messages entre utilisateurs

    Api Messages  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: sylouan.corfa@epsi.fr
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MsgApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def receive(self, **kwargs):  # noqa: E501
        """Reçoit les messages venant d'un utilisateur  # noqa: E501

        Reçoit les messages venant d'un utilisateur  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.receive(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float receiver:
        :param float sender:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.receive_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.receive_with_http_info(**kwargs)  # noqa: E501
            return data

    def receive_with_http_info(self, **kwargs):  # noqa: E501
        """Reçoit les messages venant d'un utilisateur  # noqa: E501

        Reçoit les messages venant d'un utilisateur  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.receive_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float receiver:
        :param float sender:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['receiver', 'sender']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method receive" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'receiver' in params:
            form_params.append(('receiver', params['receiver']))  # noqa: E501
        if 'sender' in params:
            form_params.append(('sender', params['sender']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/receive', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send(self, **kwargs):  # noqa: E501
        """Envoie un message à un receveur  # noqa: E501

        Envoie un message à la base de donnée et stocke l'envoyeur, le receveur, et le contenu  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float sender:
        :param float receiver:
        :param str content:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.send_with_http_info(**kwargs)  # noqa: E501
            return data

    def send_with_http_info(self, **kwargs):  # noqa: E501
        """Envoie un message à un receveur  # noqa: E501

        Envoie un message à la base de donnée et stocke l'envoyeur, le receveur, et le contenu  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float sender:
        :param float receiver:
        :param str content:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sender', 'receiver', 'content']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'sender' in params:
            form_params.append(('sender', params['sender']))  # noqa: E501
        if 'receiver' in params:
            form_params.append(('receiver', params['receiver']))  # noqa: E501
        if 'content' in params:
            form_params.append(('content', params['content']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/send', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
