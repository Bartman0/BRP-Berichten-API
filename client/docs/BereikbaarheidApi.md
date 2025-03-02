# berichten_api.BereikbaarheidApi

All URIs are relative to *https://apigw.idm.diginetwerk.net/api/brp/berichten/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_get**](BereikbaarheidApi.md#ping_get) | **GET** /berichten/ping | Ping operatie t.b.v. het toetsen van de bereikbaarheid van de API vanuit de aangesloten partij.
[**ping_head**](BereikbaarheidApi.md#ping_head) | **HEAD** /berichten/ping | Ping operatie t.b.v. het toetsen van de bereikbaarheid van de API vanuit de aangesloten partij.


# **ping_get**
> ping_get()

Ping operatie t.b.v. het toetsen van de bereikbaarheid van de API vanuit de aangesloten partij.

Deze operatie kan aangeroepen worden door aangesloten partijen om te verifiëren dat er communicatie met de berichtendienst mogelijks is. 

### Example

* OAuth Authentication (LapOAuth):
* OAuth Authentication (PrdOAuth):
* OAuth Authentication (DemoOAuth):
* OAuth Authentication (AccOAuth):
* Basic Authentication (DemoBasicAuth):

```python
import berichten_api
from berichten_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apigw.idm.diginetwerk.net/api/brp/berichten/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = berichten_api.Configuration(
    host = "https://apigw.idm.diginetwerk.net/api/brp/berichten/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: DemoBasicAuth
configuration = berichten_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with berichten_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = berichten_api.BereikbaarheidApi(api_client)

    try:
        # Ping operatie t.b.v. het toetsen van de bereikbaarheid van de API vanuit de aangesloten partij.
        api_instance.ping_get()
    except Exception as e:
        print("Exception when calling BereikbaarheidApi->ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[LapOAuth](../README.md#LapOAuth), [PrdOAuth](../README.md#PrdOAuth), [DemoOAuth](../README.md#DemoOAuth), [AccOAuth](../README.md#AccOAuth), [DemoBasicAuth](../README.md#DemoBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Geeft aan dat de API bereikt kon worden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_head**
> ping_head()

Ping operatie t.b.v. het toetsen van de bereikbaarheid van de API vanuit de aangesloten partij.

Deze operatie kan aangeroepen worden door aangesloten partijen om te verifiëren dat er communicatie met de berichtendienst mogelijks is. 

### Example

* OAuth Authentication (LapOAuth):
* OAuth Authentication (PrdOAuth):
* OAuth Authentication (DemoOAuth):
* OAuth Authentication (AccOAuth):
* Basic Authentication (DemoBasicAuth):

```python
import berichten_api
from berichten_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apigw.idm.diginetwerk.net/api/brp/berichten/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = berichten_api.Configuration(
    host = "https://apigw.idm.diginetwerk.net/api/brp/berichten/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: DemoBasicAuth
configuration = berichten_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with berichten_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = berichten_api.BereikbaarheidApi(api_client)

    try:
        # Ping operatie t.b.v. het toetsen van de bereikbaarheid van de API vanuit de aangesloten partij.
        api_instance.ping_head()
    except Exception as e:
        print("Exception when calling BereikbaarheidApi->ping_head: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[LapOAuth](../README.md#LapOAuth), [PrdOAuth](../README.md#PrdOAuth), [DemoOAuth](../README.md#DemoOAuth), [AccOAuth](../README.md#AccOAuth), [DemoBasicAuth](../README.md#DemoBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Geeft aan dat de API bereikt kon worden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

