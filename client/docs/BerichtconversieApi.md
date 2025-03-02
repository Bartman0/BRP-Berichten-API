# berichten_api.BerichtconversieApi

All URIs are relative to *https://apigw.idm.diginetwerk.net/api/brp/berichten/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**converteer**](BerichtconversieApi.md#converteer) | **POST** /berichten/conversie | Dit endpoint faciliteert bij de conversie van berichten tussen de verschillende soorten berichtformaten.


# **converteer**
> Converteer200Response converteer(body=body)

Dit endpoint faciliteert bij de conversie van berichten tussen de verschillende soorten berichtformaten.

### Example

* OAuth Authentication (LapOAuth):
* OAuth Authentication (PrdOAuth):
* OAuth Authentication (DemoOAuth):
* OAuth Authentication (AccOAuth):
* Basic Authentication (DemoBasicAuth):

```python
import berichten_api
from berichten_api.models.converteer200_response import Converteer200Response
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
    api_instance = berichten_api.BerichtconversieApi(api_client)
    body = 'body_example' # str | Er zijn verschillende waarden die voor de headers `Content-Type` en `Accept` gebruikt kunnen worden. Elk van deze waarden stelt een van de bekende formaten voor:   - \"text/plain; charset=teletex\": Het klassieke berichtenformaat waarbij de teletex charset wordt gehanteerd.   - \"text/plain+base64; charset=teletex\": Het klassieke berichtenformaat waarbij de teletex charset wordt gehanteerd. De body is in dit geval Base64 geëncodeerd.   - \"text/plain; charset=utf-8\": Het klassieke berichtenformaat waarbij de UTF-8 charset wordt gehanteerd.   - \"text/plain+base64; charset=utf-8\": Het klassieke berichtenformaat waarbij de UTF-8 charset wordt gehanteerd. De body is in dit geval Base64 geëncodeerd.   - \"application/json\": Het meest recente berichtenformaat gebaseerd op JSON en de UTF-8 charset.  Middels deze waarden kunt u via de Content-Type en Accept headers aanduiden welk formaat u instuurt en welk formaat u terug wenst te ontvangen.  (optional)

    try:
        # Dit endpoint faciliteert bij de conversie van berichten tussen de verschillende soorten berichtformaten.
        api_response = api_instance.converteer(body=body)
        print("The response of BerichtconversieApi->converteer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BerichtconversieApi->converteer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Er zijn verschillende waarden die voor de headers &#x60;Content-Type&#x60; en &#x60;Accept&#x60; gebruikt kunnen worden. Elk van deze waarden stelt een van de bekende formaten voor:   - \&quot;text/plain; charset&#x3D;teletex\&quot;: Het klassieke berichtenformaat waarbij de teletex charset wordt gehanteerd.   - \&quot;text/plain+base64; charset&#x3D;teletex\&quot;: Het klassieke berichtenformaat waarbij de teletex charset wordt gehanteerd. De body is in dit geval Base64 geëncodeerd.   - \&quot;text/plain; charset&#x3D;utf-8\&quot;: Het klassieke berichtenformaat waarbij de UTF-8 charset wordt gehanteerd.   - \&quot;text/plain+base64; charset&#x3D;utf-8\&quot;: Het klassieke berichtenformaat waarbij de UTF-8 charset wordt gehanteerd. De body is in dit geval Base64 geëncodeerd.   - \&quot;application/json\&quot;: Het meest recente berichtenformaat gebaseerd op JSON en de UTF-8 charset.  Middels deze waarden kunt u via de Content-Type en Accept headers aanduiden welk formaat u instuurt en welk formaat u terug wenst te ontvangen.  | [optional] 

### Return type

[**Converteer200Response**](Converteer200Response.md)

### Authorization

[LapOAuth](../README.md#LapOAuth), [PrdOAuth](../README.md#PrdOAuth), [DemoOAuth](../README.md#DemoOAuth), [AccOAuth](../README.md#AccOAuth), [DemoBasicAuth](../README.md#DemoBasicAuth)

### HTTP request headers

 - **Content-Type**: text/plain; charset=utf-8, text/plain+base64; charset=utf-8, text/plain; charset=teletex, text/plain+base64; charset=teletex, application/json
 - **Accept**: application/json, text/plain; charset=utf-8, text/plain+base64; charset=utf-8, text/plain; charset=teletex, text/plain+base64; charset=teletex, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Een naar JSON geconverteerd bericht |  -  |
**400** | Wanneer het aangeleverde bericht niet voldeed en daardoor niet vertaald kon worden. |  -  |
**401** | Onjuiste of ontbrekende authenticatie |  -  |
**406** | Wanneer een conversie werd aangevraagd voor een doelformaat dat niet ondersteund wordt. |  -  |
**415** | Wanneer een conversie werd aangevraagd voor een bronformaat dat niet ondersteund wordt. |  -  |
**500** | Onbekende/technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

