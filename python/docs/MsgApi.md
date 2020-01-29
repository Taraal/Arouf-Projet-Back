# swagger_client.MsgApi

All URIs are relative to *https://virtserver.swaggerhub.com/Arouf-Project/Arouf-project-Back/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receive**](MsgApi.md#receive) | **GET** /receive | Reçoit les messages venant d&#39;un utilisateur
[**send**](MsgApi.md#send) | **GET** /send | Envoie un message à un receveur


# **receive**
> receive(receiver=receiver, sender=sender)

Reçoit les messages venant d'un utilisateur

Reçoit les messages venant d'un utilisateur

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MsgApi()
receiver = 8.14 # float |  (optional)
sender = 8.14 # float |  (optional)

try:
    # Reçoit les messages venant d'un utilisateur
    api_instance.receive(receiver=receiver, sender=sender)
except ApiException as e:
    print("Exception when calling MsgApi->receive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiver** | **float**|  | [optional] 
 **sender** | **float**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send**
> send(sender=sender, receiver=receiver, content=content)

Envoie un message à un receveur

Envoie un message à la base de donnée et stocke l'envoyeur, le receveur, et le contenu

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MsgApi()
sender = 8.14 # float |  (optional)
receiver = 8.14 # float |  (optional)
content = 'content_example' # str |  (optional)

try:
    # Envoie un message à un receveur
    api_instance.send(sender=sender, receiver=receiver, content=content)
except ApiException as e:
    print("Exception when calling MsgApi->send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender** | **float**|  | [optional] 
 **receiver** | **float**|  | [optional] 
 **content** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

