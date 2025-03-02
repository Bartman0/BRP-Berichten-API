# berichten_api.BerichtenverkeerApi

All URIs are relative to *https://apigw.idm.diginetwerk.net/api/brp/berichten/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_messages**](BerichtenverkeerApi.md#delete_messages) | **DELETE** /berichten/{berichtTransportIdsParam} | Het verwijderen van een of meerdere berichten (DELETE).
[**get_messages**](BerichtenverkeerApi.md#get_messages) | **GET** /berichten/{berichtTransportIdsParam} | Het ophalen van een of meerdere berichten (GET).
[**list_messages**](BerichtenverkeerApi.md#list_messages) | **GET** /berichten | Het ophalen van een lijst met berichten die klaarstaan (LIST).
[**put_messages**](BerichtenverkeerApi.md#put_messages) | **POST** /berichten | Het versturen van een of meerdere berichten (PUT).
[**summarize**](BerichtenverkeerApi.md#summarize) | **GET** /berichten/telling | Voert verschillende soorten tellingen uit waarmee bepaald kan worden hoeveel berichten er verwerkt dienen te worden (SUMMARIZE).


# **delete_messages**
> DeleteMessageAntwoord delete_messages(bericht_transport_ids_param)

Het verwijderen van een of meerdere berichten (DELETE).

Verwijderen van een of meerdere berichten. De berichten kunnen na deze actie niet meer bij de berichten API opgehaald worden. 

### Example

* OAuth Authentication (LapOAuth):
* OAuth Authentication (PrdOAuth):
* OAuth Authentication (DemoOAuth):
* OAuth Authentication (AccOAuth):
* Basic Authentication (DemoBasicAuth):

```python
import berichten_api
from berichten_api.models.delete_message_antwoord import DeleteMessageAntwoord
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
    api_instance = berichten_api.BerichtenverkeerApi(api_client)
    bericht_transport_ids_param = ['28122289-f2f2-41c3-b33d-4c25c6620e9b'] # List[str] | Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten/list`. 

    try:
        # Het verwijderen van een of meerdere berichten (DELETE).
        api_response = api_instance.delete_messages(bericht_transport_ids_param)
        print("The response of BerichtenverkeerApi->delete_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BerichtenverkeerApi->delete_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bericht_transport_ids_param** | [**List[str]**](str.md)| Een UUID of meerdere UUID&#39;s van het bericht(en) die opgehaald moet worden. Indien meerdere UUID&#39;s, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \&quot;BRP berichten API\&quot; bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID&#39;s middels een request naar &#x60;/berichten/list&#x60;.  | 

### Return type

[**DeleteMessageAntwoord**](DeleteMessageAntwoord.md)

### Authorization

[LapOAuth](../README.md#LapOAuth), [PrdOAuth](../README.md#PrdOAuth), [DemoOAuth](../README.md#DemoOAuth), [AccOAuth](../README.md#AccOAuth), [DemoBasicAuth](../README.md#DemoBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deze 200 OK response wordt vrijwel alle situaties geretourneerd, mits er geen technische fouten opgetreden zijn. Indien er bij het verwijderen van het bericht iets mis ging, dan vindt u dat per bericht terug in de response. |  -  |
**400** | Onjuist verzoek |  -  |
**401** | Onjuiste of ontbrekende authenticatie |  -  |
**500** | Onbekende/technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> GetMessageAntwoord get_messages(bericht_transport_ids_param)

Het ophalen van een of meerdere berichten (GET).

Dit endpoint gebruikt u om berichten op te halen. 

### Example

* OAuth Authentication (LapOAuth):
* OAuth Authentication (PrdOAuth):
* OAuth Authentication (DemoOAuth):
* OAuth Authentication (AccOAuth):
* Basic Authentication (DemoBasicAuth):

```python
import berichten_api
from berichten_api.models.get_message_antwoord import GetMessageAntwoord
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
    api_instance = berichten_api.BerichtenverkeerApi(api_client)
    bericht_transport_ids_param = ['28122289-f2f2-41c3-b33d-4c25c6620e9b'] # List[str] | Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten/list`. 

    try:
        # Het ophalen van een of meerdere berichten (GET).
        api_response = api_instance.get_messages(bericht_transport_ids_param)
        print("The response of BerichtenverkeerApi->get_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BerichtenverkeerApi->get_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bericht_transport_ids_param** | [**List[str]**](str.md)| Een UUID of meerdere UUID&#39;s van het bericht(en) die opgehaald moet worden. Indien meerdere UUID&#39;s, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \&quot;BRP berichten API\&quot; bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID&#39;s middels een request naar &#x60;/berichten/list&#x60;.  | 

### Return type

[**GetMessageAntwoord**](GetMessageAntwoord.md)

### Authorization

[LapOAuth](../README.md#LapOAuth), [PrdOAuth](../README.md#PrdOAuth), [DemoOAuth](../README.md#DemoOAuth), [AccOAuth](../README.md#AccOAuth), [DemoBasicAuth](../README.md#DemoBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deze 200 OK response wordt vrijwel alle situaties geretourneerd, mits er geen technische fouten opgetreden zijn. Indien er bij het ophalen van het bericht iets mis ging, dan vindt u dat per bericht terug in de response. |  -  |
**400** | Onjuist verzoek |  -  |
**401** | Onjuiste of ontbrekende authenticatie |  -  |
**500** | Onbekende/technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_messages**
> ListMessageAntwoord list_messages(status=status, bericht_type=bericht_type, vanaf_moment=vanaf_moment, tot_moment=tot_moment, pagina=pagina, berichten_per_pagina=berichten_per_pagina)

Het ophalen van een lijst met berichten die klaarstaan (LIST).

Dit endpoint gebruikt u om te achterhalen welke berichten er voor u beschikbaar zijn. 

### Example

* OAuth Authentication (LapOAuth):
* OAuth Authentication (PrdOAuth):
* OAuth Authentication (DemoOAuth):
* OAuth Authentication (AccOAuth):
* Basic Authentication (DemoBasicAuth):

```python
import berichten_api
from berichten_api.models.list_message_antwoord import ListMessageAntwoord
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
    api_instance = berichten_api.BerichtenverkeerApi(api_client)
    status = ["nieuw","gezien-in-lijst"] # List[str] | Geeft aan welke berichten opgenomen moeten worden in het resultaat. Comma-gescheiden veld. Indien leeg worden alle niet opgehaalde berichten getoond (`nieuw` + `gezien-in-lijst`).    - `nieuw`: Geeft berichten welke nog nooit opgehaald zijn en tevens niet in de lijst operatie zijn getoond.   - `gezien-in-lijst`: Geeft berichten die nog niet opgehaald zijn, maar al wel gezien zijn in de lijst.   - `opgehaald`: Geeft berichten reeds opgehaald zijn.  (optional) (default to ["nieuw","gezien-in-lijst"])
    bericht_type = 'bericht_type_example' # str | Geeft aan welke type berichten opgenomen moeten worden in het resultaat. Indien leeg of niet aanwezig worden alle berichten getoond. Niet hoofdlettergevoelig. (optional)
    vanaf_moment = '2013-10-20T19:20:30+01:00' # datetime | Het resultaat zal alleen berichten bevatten die vanaf dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond die nog beschikbaar zijn (waarvan de retentietijd nog niet verlopen is). (optional)
    tot_moment = '2013-10-20T19:20:30+01:00' # datetime | Het resultaat zal alleen berichten bevatten die tot dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond t/m het heden. (optional)
    pagina = 1 # int | Pagina nummer, startend bij 1 t/m N (niet bij 0). (optional) (default to 1)
    berichten_per_pagina = 56 # int | Het maximum aantal berichten dat geretourneerd mag worden. Indien deze waarde het ingesteld systeemlimiet overschrijdt, dan wordt het systeemlimiet gehanteerd. Indien er geen waarde wordt opgegeven, dan wordt tevens het systeemlimiet gehanteerd.  (optional)

    try:
        # Het ophalen van een lijst met berichten die klaarstaan (LIST).
        api_response = api_instance.list_messages(status=status, bericht_type=bericht_type, vanaf_moment=vanaf_moment, tot_moment=tot_moment, pagina=pagina, berichten_per_pagina=berichten_per_pagina)
        print("The response of BerichtenverkeerApi->list_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BerichtenverkeerApi->list_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**List[str]**](str.md)| Geeft aan welke berichten opgenomen moeten worden in het resultaat. Comma-gescheiden veld. Indien leeg worden alle niet opgehaalde berichten getoond (&#x60;nieuw&#x60; + &#x60;gezien-in-lijst&#x60;).    - &#x60;nieuw&#x60;: Geeft berichten welke nog nooit opgehaald zijn en tevens niet in de lijst operatie zijn getoond.   - &#x60;gezien-in-lijst&#x60;: Geeft berichten die nog niet opgehaald zijn, maar al wel gezien zijn in de lijst.   - &#x60;opgehaald&#x60;: Geeft berichten reeds opgehaald zijn.  | [optional] [default to [&quot;nieuw&quot;,&quot;gezien-in-lijst&quot;]]
 **bericht_type** | **str**| Geeft aan welke type berichten opgenomen moeten worden in het resultaat. Indien leeg of niet aanwezig worden alle berichten getoond. Niet hoofdlettergevoelig. | [optional] 
 **vanaf_moment** | **datetime**| Het resultaat zal alleen berichten bevatten die vanaf dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond die nog beschikbaar zijn (waarvan de retentietijd nog niet verlopen is). | [optional] 
 **tot_moment** | **datetime**| Het resultaat zal alleen berichten bevatten die tot dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond t/m het heden. | [optional] 
 **pagina** | **int**| Pagina nummer, startend bij 1 t/m N (niet bij 0). | [optional] [default to 1]
 **berichten_per_pagina** | **int**| Het maximum aantal berichten dat geretourneerd mag worden. Indien deze waarde het ingesteld systeemlimiet overschrijdt, dan wordt het systeemlimiet gehanteerd. Indien er geen waarde wordt opgegeven, dan wordt tevens het systeemlimiet gehanteerd.  | [optional] 

### Return type

[**ListMessageAntwoord**](ListMessageAntwoord.md)

### Authorization

[LapOAuth](../README.md#LapOAuth), [PrdOAuth](../README.md#PrdOAuth), [DemoOAuth](../README.md#DemoOAuth), [AccOAuth](../README.md#AccOAuth), [DemoBasicAuth](../README.md#DemoBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Een opsomming van de berichten die beschikbaar zijn voor de mailbox die gekoppeld is aan het geauthenticeerde account. |  -  |
**400** | Onjuist verzoek |  -  |
**401** | Onjuiste of ontbrekende authenticatie |  -  |
**500** | Interne technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_messages**
> PutMessageAntwoord put_messages(put_message_request=put_message_request)

Het versturen van een of meerdere berichten (PUT).

Dit endpoint gebruikt u om berichten zoals gespecificeerd in het Logisch Ontwerp te versturen. 

### Example

* OAuth Authentication (LapOAuth):
* OAuth Authentication (PrdOAuth):
* OAuth Authentication (DemoOAuth):
* OAuth Authentication (AccOAuth):
* Basic Authentication (DemoBasicAuth):

```python
import berichten_api
from berichten_api.models.put_message_antwoord import PutMessageAntwoord
from berichten_api.models.put_message_request import PutMessageRequest
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
    api_instance = berichten_api.BerichtenverkeerApi(api_client)
    put_message_request = berichten_api.PutMessageRequest() # PutMessageRequest |  (optional)

    try:
        # Het versturen van een of meerdere berichten (PUT).
        api_response = api_instance.put_messages(put_message_request=put_message_request)
        print("The response of BerichtenverkeerApi->put_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BerichtenverkeerApi->put_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_message_request** | [**PutMessageRequest**](PutMessageRequest.md)|  | [optional] 

### Return type

[**PutMessageAntwoord**](PutMessageAntwoord.md)

### Authorization

[LapOAuth](../README.md#LapOAuth), [PrdOAuth](../README.md#PrdOAuth), [DemoOAuth](../README.md#DemoOAuth), [AccOAuth](../README.md#AccOAuth), [DemoBasicAuth](../README.md#DemoBasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | a-Synchrone response. Een eventueel antwoord op een bericht wordt later voor u klaargezet en dient separaat opgehaald te worden. |  -  |
**400** | Het verzoek is onjuist en is daarom niet verwerkt. |  -  |
**401** | Onjuiste of ontbrekende authenticatie |  -  |
**500** | Onbekende/technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summarize**
> Summarize200Response summarize(soort)

Voert verschillende soorten tellingen uit waarmee bepaald kan worden hoeveel berichten er verwerkt dienen te worden (SUMMARIZE).

### Example

* OAuth Authentication (LapOAuth):
* OAuth Authentication (PrdOAuth):
* OAuth Authentication (DemoOAuth):
* OAuth Authentication (AccOAuth):
* Basic Authentication (DemoBasicAuth):

```python
import berichten_api
from berichten_api.models.summarize200_response import Summarize200Response
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
    api_instance = berichten_api.BerichtenverkeerApi(api_client)
    soort = 'soort_example' # str | Geeft aan welke telling er uitgevoerd moet worden.   - nieuw: Geeft het aantal nieuwe berichten terug dat nog niet gezien is via een LIST operatie en tevens nog niet opgehaald is middels een GET operatie.   - gezien-in-lijst-en-niet-opgehaald: Geeft het aantal nieuwe berichten terug dat gezien is via een LIST operatie, maar nog niet opgehaald is middels een GET operatie.   - niet-opgehaald: Geeft het aantal nieuwe berichten terug dat nog niet opgehaald is middels een GET operatie. 

    try:
        # Voert verschillende soorten tellingen uit waarmee bepaald kan worden hoeveel berichten er verwerkt dienen te worden (SUMMARIZE).
        api_response = api_instance.summarize(soort)
        print("The response of BerichtenverkeerApi->summarize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BerichtenverkeerApi->summarize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soort** | **str**| Geeft aan welke telling er uitgevoerd moet worden.   - nieuw: Geeft het aantal nieuwe berichten terug dat nog niet gezien is via een LIST operatie en tevens nog niet opgehaald is middels een GET operatie.   - gezien-in-lijst-en-niet-opgehaald: Geeft het aantal nieuwe berichten terug dat gezien is via een LIST operatie, maar nog niet opgehaald is middels een GET operatie.   - niet-opgehaald: Geeft het aantal nieuwe berichten terug dat nog niet opgehaald is middels een GET operatie.  | 

### Return type

[**Summarize200Response**](Summarize200Response.md)

### Authorization

[LapOAuth](../README.md#LapOAuth), [PrdOAuth](../README.md#PrdOAuth), [DemoOAuth](../README.md#DemoOAuth), [AccOAuth](../README.md#AccOAuth), [DemoBasicAuth](../README.md#DemoBasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Het resultaat van de telling. |  -  |
**400** | Indien er een telling-soort gevraagd werdt die niet bestaat, of wanneer er geen telling-soort is opgegeven. |  -  |
**401** | Onjuiste of ontbrekende authenticatie |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

