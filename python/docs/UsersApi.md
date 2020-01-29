# swagger_client.UsersApi

All URIs are relative to *https://virtserver.swaggerhub.com/Arouf-Project/Arouf-project-Back/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UsersApi.md#add_user) | **POST** /add | Ajoute un utilisateur
[**authenticate**](UsersApi.md#authenticate) | **POST** /auth | Permet à un utilisateur de s&#39;identifier
[**error_get**](UsersApi.md#error_get) | **GET** /error | Teste le reporting Sentry
[**get_all**](UsersApi.md#get_all) | **GET** /get/all | Récupère tous les users de la DB
[**get_user**](UsersApi.md#get_user) | **GET** /get | Trouve un utilisateur précis


# **add_user**
> add_user(nom=nom, prenom=prenom, username=username, password=password, email=email)

Ajoute un utilisateur

Ajoute un utilisateur à la base de donnée

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
nom = 'nom_example' # str |  (optional)
prenom = 'prenom_example' # str |  (optional)
username = 'username_example' # str |  (optional)
password = 'password_example' # str |  (optional)
email = 'email_example' # str |  (optional)

try:
    # Ajoute un utilisateur
    api_instance.add_user(nom=nom, prenom=prenom, username=username, password=password, email=email)
except ApiException as e:
    print("Exception when calling UsersApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nom** | **str**|  | [optional] 
 **prenom** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate**
> authenticate(username=username, password=password)

Permet à un utilisateur de s'identifier

Vérifie les identifiants de connexion de l'utilisateur et lui accorde l'accès le cas échéan

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
username = 'username_example' # str |  (optional)
password = 'password_example' # str |  (optional)

try:
    # Permet à un utilisateur de s'identifier
    api_instance.authenticate(username=username, password=password)
except ApiException as e:
    print("Exception when calling UsersApi->authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **error_get**
> error_get()

Teste le reporting Sentry

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Teste le reporting Sentry
    api_instance.error_get()
except ApiException as e:
    print("Exception when calling UsersApi->error_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> get_all()

Récupère tous les users de la DB

Récupère tous les utilisateurs présents en base de données 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Récupère tous les users de la DB
    api_instance.get_all()
except ApiException as e:
    print("Exception when calling UsersApi->get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> get_user(username=username)

Trouve un utilisateur précis

Retourne les informations complète sur un utilisateur précis à partir de son username

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
username = 'username_example' # str |  (optional)

try:
    # Trouve un utilisateur précis
    api_instance.get_user(username=username)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

