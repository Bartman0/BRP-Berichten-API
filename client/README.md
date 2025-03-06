# berichten-api
Een REST API voor het a-synchroon uitwisselen van berichten welke in het Logisch Ontwerp gedefinieerd zijn.

# Wijzigingshistorie:

## 0.6.3 Januari 2025
- Tekstuele verwijzing naar '/berichten/list' vervangen door '/berichten'.

## 0.6.2 Januari 2025
- OAuth endpoint demo omgeving gecorrigeerd.

## 0.6.1 Januari 2025
- Ping endpoints zijn niet langer bereikbaar zonder eerst te authenticeren.

## 0.6.0 Januari 2025
- Servers toegevoegd.
  - Hiervoor moesten de paden van de endpoints aangepast worden. Hierdoor is '/api/v1' komen te vervallen bij de endpoints. Dit is verhuist naar de base-url's van de genoemde servers.
- Authenticatie details toegevoegd.
- Foutmeldingen bij het conversie endpoint bijgewerkt.
- Alle namespace paden van de foutmeldingen nagelopen en gecorrigeerd daar waar nodig. Dit zodat ze consistent starten met: \"https://www.rvig.nl/brp/berichten-api/probleem/\".

## 0.5.5 November 2024
- 'berichtVolgnummer' en 'afzender' required gemaakt in ListMessageKenmerken (en daardoor ook in GetMessageKenmerken).
- De GET en DELETE foutsituaties zijn voorzien van discriminators ten behoeve van het onderscheiden van foutsituatie subtypes door de gegenereerde client.

## 0.5.4 November 2024
- Properties van PagineringResultaat en PagineerbaarResultaat welke altijd aanwezig zullen zijn bij een list-request required gemaakt.
- Required properties van put-message-antwoord gecorrigeerd.
- Schema van het Null bericht gecorrigeerd.

## 0.5.3 November 2024
- Het Sv11 bericht is qua schema aangepast aangezien deze onterecht de property plData bevatte. Deze property is verwijderd uit dit bericht.
- Foutsituaties zijn voorzien van discriminators ten behoeve van het onderscheiden van foutsituatie subtypes door de gegenereerde client.

## 0.5.2 Oktober 2024
- De request die volledig afgekeurd worden en een statuscode 4xx of 5xx retourneren, doen dit nu met de response header 'Content-Type: application/problem+json'.
- Requests die een 2xx response in JSON formaat retourneren, doen dit met \"Content-Type: application/json\" ipv \"Content-Type: application/json: charset=utf-8\". Conform rfc8259 (https://www.rfc-editor.org/rfc/rfc8259) is JSON altijd in UTF-8 formaat en heeft dit type geen charset parameter.

## 0.5.1 Oktober 2024
 - De fout BBA-PUT-F002 is aangepast naar een algemene fout voor onjuiste velden in een PutMessage, via het veld \"invalidParams\" in de response word aangegeven welke velden onjuist zijn en waarom.

## 0.5.0 September 2024
 - Het veld berichtId en verwijzingBerichtId zijn omgezet van type 'integer' naar type 'string' om beter aan te sluiten op de bestaande voorziening.
 - Het probleem-antwoord response object is overal vervangen met de algemene Foutmelding response welke zich conformeert aan RFC7807.
 - De velden 'foutTitel', 'foutType', 'foutDetail' zijn aangepast naar 'title, 'type', 'detail' zodat zij zich conformeren aan de RFC7807.
 - De afhankelijkheid op 'openapi-problem-detail-v1.yml' is komen te vervallen (https://github.com/rvig-brp/BRP-Berichten-API/issues/3).

## 0.4.1 Juli 2024
 - Het json-schema voor de autorisatieberichten Ct01, Cw01 en Cb01 is toegevoegd.
 - De ontvanger is opgenomen in de response bij het verzenden van een bericht. Dit is met name relevant wanneer er een bericht naar een berichtgroep gestuurd wordt. In dat geval weet de verzender wie de uiteindelijke ontvangers zijn. Bij het versturen van een bericht naar de een regulier account zal dit nummer 1:1 overeenkomen met de ontvanger die bij het te verzenden bericht is opgegeven.

## 0.4.0 Juni 2024
- De json-schema's van de berichtsoorten zijn opgenomen in de OpenAPI Specificatie. Voor elke berichtsoort die het LO beschrijft, is opgenomen hoe dit bericht gestructureerd is.
  - Houdt er rekening mee dat het weergeven van de OpenAPI specificatie in de web-versie va SwaggerUI hierdoor trager geworden is. Het is aan te raden om de alternatieve (redocly) weergave te gebruiken:
    - https://brp-berichten-api.dictua.ictu-sr.nl/openapi/berichten-api.html
    - De JSON schema's zijn tevens te vinden op onze Github pagina.
- De JSON-response van het conversie endpoint is iets aangepast zodat naast het geconverteerde bericht tevens validatiefouten opgenomen kunnen worden.

## 0.3.0 - Mei 2024
- Conversie endpoints
  - Introductie bericht-conversie (/berichten/conversie) endpoint. Houdt er rekening mee dat de conversie naar JSON opgenomen is, maar nog niet geïmplementeerd is in de demo omgeving.
- Het limiet van het aantal berichten dat verwijderd kan worden is gelijkgesteld aan dat wat gelijktijdig opgehaald kan worden (100).
- De API is hernoemd van \"BRP A-Synchrone berichten API\" naar \"BRP berichten API\".
  - Nieuwe URL's demo omgeving:
    - https://brp-berichten-api.dictua.ictu-sr.nl/api/v1/berichten
    - https://brp-berichten-api.dictua.ictu-sr.nl/openapi/berichten-api.html
    - https://brp-berichten-api.dictua.ictu-sr.nl/swagger-ui/index.html
- Beschikbaarheid endpoint(s)
  - Er is een tweede ping endpoint bijgekomen waardoor en nu een HEAD of een GET gedaan kan worden. De response blijft hetzelfde. U kunt zelf kiezen welke van deze twee u hanteert.
  - De noodzaak voor authenticatie op het `ping` endpoint is komen te vervallen. U kunt dus zonder noodzaak van authenticatie vaststellen of de dienst beschikbaar is.

## 0.2.2 - April 2024
- Ping operatie toegevoegd t.b.v. het verifiëren dat er communicatie met de berichtendienst mogelijks is.
- De standaard sortering bij een LIST operatie is op dit moment:
  1. `Datum + tijdstip van ontvangst` waarbij geldt dat het oudste bericht als eerste wordt weergegeven in de lijst met beschikbare berichten (rationale deze dient als eerste verwerkt worden door de ontvanger).
  2. Indien `datum + tijdstip van ontvangst` gelijk zijn (wat kan voorkomen aangezien er meerdere berichten tegelijk ingestuurd kunnen worden), dan worden `afzender` en het `messageId` meegenomen in de sortering. De volgorde die de afzender toegekend heen via de messageId is op dat moment dus bepalend.

## 0.2.1 - April 2024
- Mogelijkheden tot sortering bij een list operatie zijn verwijderd. De standaard sortering wordt nog bepaald.
- Demo omgeving is toegevoegd aan de lijst met servers.
  - API te benaderen via https://brp-berichten-api.dictua.ictu-sr.nl/api/v1/berichten
  - Swagger UI via: https://brp-berichten-api.dictua.ictu-sr.nl/swagger-ui/index.html
  - De OpenAPI specificatie via: https://brp-berichten-api.dictua.ictu-sr.nl/openapi.brp-berichten-api-v1.yaml
- Wachtwoord wijzigingen optie is verwijderd.
- Het `berichtFormaat` attribuut is komen te vervallen. Alle berichten zijn nu per definitie in JSON formaat. De eis om de berichtInhoud Base64 te
  encoderen komt daarmee te vervallen.
- Voorbeelddata verbeterd.
- Tellingen endpoint toegevoegd welke invulling geeft aan de mailbox Summarize tegenhanger.
- Delete endpoint gecorrigeerd. De collectie `succesvolVerwijderdeBerichten` was van het type string i.p.v. berichtTransportId.
- Limieten zijn gewijzigd:
  - Het aantal berichten dat via een PUT verstuurd kan worden is verhoogd naar 25. Uitgaande van een gemiddelde berichtgrootte van 40kb geeft dat een request van 1MB groot.
  - Het aantal berichten dat via een LIST opgevraagd kan worden is vergroot naar 2000. Daarbij krijgt u de mogelijkheid om dit aantal te beperken.
    - 2000 berichten in een LIST operatie komt neer op ongeveer 600KB response grootte.
  - Het aantal berichten dat via een GET ontvangen kan worden is verhoogd naar 100. Dit heeft te maken met de gangbare (veilige) restricties van een URL qua lengte (2KB).
    - Voor de URL worden 256 bytes gereserveerd.
      - Voor de UUID blijven dan 1.792 bytes over.
    - Een BerichtTransportId is 17 bytes groot (UUID + separatie-karakter ',')
      - Uitgaande van 17 bytes, zou dit 105 keer herhaald kunnen worden. Om aan de veilige kan te zitten en om op een mooi rond getal uit te komen kiezen wij voor 100 als limiet.
    - Uitgaande van een gemiddelde berichtgrootte van 40KB komt je met 100 berichten uit op 4MB qua response-grootte.
- \"aantalKeerOpgehaald\" en \"dtLaatstOpgehaald\" zijn verwijderd uit response van LIST (ListMessageKenmerken schema). Wij zien hierin geen meerwaarde voor de aansluitende partijen. Wel kunt u blijven zien OF het bericht is opgehaald (boolean waarde).

## 0.2.0 - April 2024
- \"List\" verzoek is verhuisd van \"/berichten/lijst\" --> \"/berichten\"
- \"GET\" van meerdere berichten wordt gedaan middels path-parameters i.p.v. query-parameters en is samengevoegd met het endpoint voor het ophalen van een enkel bericht.<br/>
  (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID])
  (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID])
- \"DELETE\" van meerdere berichten wordt gedaan middels path-parameters i.p.v. query-parameters en is samengevoegd met het endpoint voor het verwijderen van een enkel bericht.<br/>
  (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID])
- Het \"berichtId\" wat correspondeert met het \"MessageId\" veld van de mailboxserver is qua type gewijzigd van String naar Integer. Maximale lengte 12.
  - Beschrijving LO: MessageId, lengte: 12, Het unieke volgnummer dat aan het uitgaande bericht wordt toegekend.
- Het veld \"verwijzingBerichtId\" wat correspondeert met het \"CrossReference\" veld van de mailboxserver:
  - is qua type gewijzigd van String naar Integer. Maximale lengte 12.
  - kan of weggelaten worden, of gevuld worden met 0 indien het bericht een eerste bericht in de cyclus betreft.
- \"aantalKeerOpgehaald\" is toegevoegd aan de ListMessageKenmerken.

## 0.1.0 - Maart 2024
Initiële versie.

# In ontwikkeling:
- Bepalen of het een checksum op de berichtinhoud van meerwaarde kan zijn.

# Voorlopige limieten:
| Waarde | Omschrijving |
|--------|--------------|
| 1      | Aantal ontvangers per bericht. |
| 25     | Maximum aantal berichten dat in één PUT request verstuurd mag worden. |
| 100     | Maximum aantal berichten dat in één DELETE request verwijderd mag worden |
| 2000   | Maximum aantal berichten dat in één LIST request getoond zal worden. Indien wenselijk kunt u dit aantal middels een query-parameter beperken. |
| 100    | Maximum aantal berichten dat in één GET request ontvangen mag worden. |
| 64kb   | Maximum grootte van één enkel bericht. Één request zal qua grootte dan uitkomen op ((maximale-grootte-enkel-bericht * maximaal-aantal-berichten) + overhead). Houdt er rekening mee dat dit een waarde is die in te toekomst kan gaan groeien. Beperk uw oplossing dus niet op deze waarde! |


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.6.3
- Package version: 1.0.0
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import berichten_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import berichten_api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    except ApiException as e:
        print("Exception when calling BereikbaarheidApi->ping_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://apigw.idm.diginetwerk.net/api/brp/berichten/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BereikbaarheidApi* | [**ping_get**](docs/BereikbaarheidApi.md#ping_get) | **GET** /berichten/ping | Ping operatie t.b.v. het toetsen van de bereikbaarheid van de API vanuit de aangesloten partij.
*BereikbaarheidApi* | [**ping_head**](docs/BereikbaarheidApi.md#ping_head) | **HEAD** /berichten/ping | Ping operatie t.b.v. het toetsen van de bereikbaarheid van de API vanuit de aangesloten partij.
*BerichtconversieApi* | [**converteer**](docs/BerichtconversieApi.md#converteer) | **POST** /berichten/conversie | Dit endpoint faciliteert bij de conversie van berichten tussen de verschillende soorten berichtformaten.
*BerichtenverkeerApi* | [**delete_messages**](docs/BerichtenverkeerApi.md#delete_messages) | **DELETE** /berichten/{berichtTransportIdsParam} | Het verwijderen van een of meerdere berichten (DELETE).
*BerichtenverkeerApi* | [**get_messages**](docs/BerichtenverkeerApi.md#get_messages) | **GET** /berichten/{berichtTransportIdsParam} | Het ophalen van een of meerdere berichten (GET).
*BerichtenverkeerApi* | [**list_messages**](docs/BerichtenverkeerApi.md#list_messages) | **GET** /berichten | Het ophalen van een lijst met berichten die klaarstaan (LIST).
*BerichtenverkeerApi* | [**put_messages**](docs/BerichtenverkeerApi.md#put_messages) | **POST** /berichten | Het versturen van een of meerdere berichten (PUT).
*BerichtenverkeerApi* | [**summarize**](docs/BerichtenverkeerApi.md#summarize) | **GET** /berichten/telling | Voert verschillende soorten tellingen uit waarmee bepaald kan worden hoeveel berichten er verwerkt dienen te worden (SUMMARIZE).


## Documentation For Models

 - [Af01](docs/Af01.md)
 - [Af01PlData](docs/Af01PlData.md)
 - [Af01PlDataC01Inner](docs/Af01PlDataC01Inner.md)
 - [Af01PlDataC01InnerAllOfHistorieInner](docs/Af01PlDataC01InnerAllOfHistorieInner.md)
 - [Af01PlDataC02Inner](docs/Af01PlDataC02Inner.md)
 - [Af01PlDataC02InnerAllOfHistorieInner](docs/Af01PlDataC02InnerAllOfHistorieInner.md)
 - [Af01PlDataC04Inner](docs/Af01PlDataC04Inner.md)
 - [Af01PlDataC04InnerAllOfHistorieInner](docs/Af01PlDataC04InnerAllOfHistorieInner.md)
 - [Af01PlDataC05Inner](docs/Af01PlDataC05Inner.md)
 - [Af01PlDataC05InnerAllOfHistorieInner](docs/Af01PlDataC05InnerAllOfHistorieInner.md)
 - [Af01PlDataC06Inner](docs/Af01PlDataC06Inner.md)
 - [Af01PlDataC06InnerAllOfHistorieInner](docs/Af01PlDataC06InnerAllOfHistorieInner.md)
 - [Af01PlDataC07Inner](docs/Af01PlDataC07Inner.md)
 - [Af01PlDataC07InnerAllOfHistorieInner](docs/Af01PlDataC07InnerAllOfHistorieInner.md)
 - [Af01PlDataC08Inner](docs/Af01PlDataC08Inner.md)
 - [Af01PlDataC08InnerAllOfHistorieInner](docs/Af01PlDataC08InnerAllOfHistorieInner.md)
 - [Af01PlDataC09Inner](docs/Af01PlDataC09Inner.md)
 - [Af01PlDataC09InnerAllOfHistorieInner](docs/Af01PlDataC09InnerAllOfHistorieInner.md)
 - [Af01PlDataC10Inner](docs/Af01PlDataC10Inner.md)
 - [Af01PlDataC10InnerAllOfHistorieInner](docs/Af01PlDataC10InnerAllOfHistorieInner.md)
 - [Af01PlDataC11Inner](docs/Af01PlDataC11Inner.md)
 - [Af01PlDataC11InnerAllOfHistorieInner](docs/Af01PlDataC11InnerAllOfHistorieInner.md)
 - [Af01PlDataC12Inner](docs/Af01PlDataC12Inner.md)
 - [Af01PlDataC12InnerAllOfHistorieInner](docs/Af01PlDataC12InnerAllOfHistorieInner.md)
 - [Af01PlDataC13Inner](docs/Af01PlDataC13Inner.md)
 - [Af01PlDataC13InnerAllOfHistorieInner](docs/Af01PlDataC13InnerAllOfHistorieInner.md)
 - [Af01PlDataC14Inner](docs/Af01PlDataC14Inner.md)
 - [Af01PlDataC14InnerAllOfHistorieInner](docs/Af01PlDataC14InnerAllOfHistorieInner.md)
 - [Af01PlDataC15Inner](docs/Af01PlDataC15Inner.md)
 - [Af01PlDataC15InnerAllOfHistorieInner](docs/Af01PlDataC15InnerAllOfHistorieInner.md)
 - [Af01PlDataC16Inner](docs/Af01PlDataC16Inner.md)
 - [Af01PlDataC16InnerAllOfHistorieInner](docs/Af01PlDataC16InnerAllOfHistorieInner.md)
 - [Af01PlDataC17Inner](docs/Af01PlDataC17Inner.md)
 - [Af01PlDataC17InnerAllOfHistorieInner](docs/Af01PlDataC17InnerAllOfHistorieInner.md)
 - [Af01PlDataC21Inner](docs/Af01PlDataC21Inner.md)
 - [Af01PlDataC21InnerAllOfHistorieInner](docs/Af01PlDataC21InnerAllOfHistorieInner.md)
 - [Af11](docs/Af11.md)
 - [Ag01](docs/Ag01.md)
 - [Ag11](docs/Ag11.md)
 - [Ag21](docs/Ag21.md)
 - [Ag31](docs/Ag31.md)
 - [Ap01](docs/Ap01.md)
 - [Autorisatietabelregel](docs/Autorisatietabelregel.md)
 - [Av01](docs/Av01.md)
 - [BBAAUTHF001](docs/BBAAUTHF001.md)
 - [BBAAUTHF002](docs/BBAAUTHF002.md)
 - [BBACONVF001](docs/BBACONVF001.md)
 - [BBACONVF002](docs/BBACONVF002.md)
 - [BBACONVF003](docs/BBACONVF003.md)
 - [BBACONVF004](docs/BBACONVF004.md)
 - [BBACONVF005](docs/BBACONVF005.md)
 - [BBACONVF006](docs/BBACONVF006.md)
 - [BBADELETEF001](docs/BBADELETEF001.md)
 - [BBADELETEF002](docs/BBADELETEF002.md)
 - [BBADELETEF003](docs/BBADELETEF003.md)
 - [BBADELETEF004](docs/BBADELETEF004.md)
 - [BBAF999](docs/BBAF999.md)
 - [BBAGETF001](docs/BBAGETF001.md)
 - [BBAGETF002](docs/BBAGETF002.md)
 - [BBAGETF003](docs/BBAGETF003.md)
 - [BBAGETF004](docs/BBAGETF004.md)
 - [BBALISTF001](docs/BBALISTF001.md)
 - [BBAPUTF001](docs/BBAPUTF001.md)
 - [BBAPUTF002](docs/BBAPUTF002.md)
 - [BBAPUTF003](docs/BBAPUTF003.md)
 - [BBAPUTF004](docs/BBAPUTF004.md)
 - [BBASUMMARIZEF001](docs/BBASUMMARIZEF001.md)
 - [BerichtKenmerken](docs/BerichtKenmerken.md)
 - [Cb01](docs/Cb01.md)
 - [Converteer200Response](docs/Converteer200Response.md)
 - [Converteer200ResponseValidatieFoutenInner](docs/Converteer200ResponseValidatieFoutenInner.md)
 - [Converteer400Response](docs/Converteer400Response.md)
 - [Converteer406Response](docs/Converteer406Response.md)
 - [Converteer415Response](docs/Converteer415Response.md)
 - [Ct01](docs/Ct01.md)
 - [Cw01](docs/Cw01.md)
 - [DeleteMessageAntwoord](docs/DeleteMessageAntwoord.md)
 - [DeleteMessageAntwoordAllOfFoutmeldingen](docs/DeleteMessageAntwoordAllOfFoutmeldingen.md)
 - [DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten](docs/DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten.md)
 - [Dt01](docs/Dt01.md)
 - [Dw01](docs/Dw01.md)
 - [Foutmelding](docs/Foutmelding.md)
 - [GeneriekAntwoord](docs/GeneriekAntwoord.md)
 - [GetMessageAntwoord](docs/GetMessageAntwoord.md)
 - [GetMessageAntwoordAllOfFoutmeldingen](docs/GetMessageAntwoordAllOfFoutmeldingen.md)
 - [GetMessageAntwoordAllOfNietOpgehaaldeBerichten](docs/GetMessageAntwoordAllOfNietOpgehaaldeBerichten.md)
 - [GetMessageAntwoordAllOfOpgehaaldeBerichten](docs/GetMessageAntwoordAllOfOpgehaaldeBerichten.md)
 - [GetMessageKenmerken](docs/GetMessageKenmerken.md)
 - [Gv01](docs/Gv01.md)
 - [Gv02](docs/Gv02.md)
 - [Ha01](docs/Ha01.md)
 - [Hf01](docs/Hf01.md)
 - [Hq01](docs/Hq01.md)
 - [Ib01](docs/Ib01.md)
 - [If01](docs/If01.md)
 - [If21](docs/If21.md)
 - [If31](docs/If31.md)
 - [If41](docs/If41.md)
 - [Ii01](docs/Ii01.md)
 - [InvalidParametersInner](docs/InvalidParametersInner.md)
 - [Iv01](docs/Iv01.md)
 - [Iv11](docs/Iv11.md)
 - [Iv21](docs/Iv21.md)
 - [Jb01](docs/Jb01.md)
 - [Jf01](docs/Jf01.md)
 - [Jf21](docs/Jf21.md)
 - [Jf31](docs/Jf31.md)
 - [Ji01](docs/Ji01.md)
 - [Jv01](docs/Jv01.md)
 - [La01](docs/La01.md)
 - [Lf01](docs/Lf01.md)
 - [Lg01](docs/Lg01.md)
 - [Lg01PlData](docs/Lg01PlData.md)
 - [ListMessageAntwoord](docs/ListMessageAntwoord.md)
 - [ListMessageKenmerken](docs/ListMessageKenmerken.md)
 - [ListMessages401Response](docs/ListMessages401Response.md)
 - [LoBericht](docs/LoBericht.md)
 - [Lq01](docs/Lq01.md)
 - [Ng01](docs/Ng01.md)
 - [Null](docs/Null.md)
 - [Of11](docs/Of11.md)
 - [Og11](docs/Og11.md)
 - [PagineerbaarResultaat](docs/PagineerbaarResultaat.md)
 - [PagineringResultaat](docs/PagineringResultaat.md)
 - [PagineringVerzoek](docs/PagineringVerzoek.md)
 - [Pf01](docs/Pf01.md)
 - [Pf02](docs/Pf02.md)
 - [Pf03](docs/Pf03.md)
 - [PutMessage](docs/PutMessage.md)
 - [PutMessageAntwoord](docs/PutMessageAntwoord.md)
 - [PutMessageAntwoordAllOfFoutmeldingen](docs/PutMessageAntwoordAllOfFoutmeldingen.md)
 - [PutMessageAntwoordAllOfNietVerwerkteBerichten](docs/PutMessageAntwoordAllOfNietVerwerkteBerichten.md)
 - [PutMessageAntwoordAllOfVerwerkteBerichten](docs/PutMessageAntwoordAllOfVerwerkteBerichten.md)
 - [PutMessageKenmerken](docs/PutMessageKenmerken.md)
 - [PutMessageRequest](docs/PutMessageRequest.md)
 - [Rb01](docs/Rb01.md)
 - [Rf01](docs/Rf01.md)
 - [Rf31](docs/Rf31.md)
 - [Rv01](docs/Rv01.md)
 - [Summarize200Response](docs/Summarize200Response.md)
 - [Sv01](docs/Sv01.md)
 - [Sv11](docs/Sv11.md)
 - [Tb01](docs/Tb01.md)
 - [Tb02](docs/Tb02.md)
 - [Tf01](docs/Tf01.md)
 - [Tf11](docs/Tf11.md)
 - [Tf21](docs/Tf21.md)
 - [Tv01](docs/Tv01.md)
 - [Vb01](docs/Vb01.md)
 - [Vb02](docs/Vb02.md)
 - [Wa01](docs/Wa01.md)
 - [Wa11](docs/Wa11.md)
 - [Wf01](docs/Wf01.md)
 - [Xa01](docs/Xa01.md)
 - [Xf01](docs/Xf01.md)
 - [Xq01](docs/Xq01.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="DemoBasicAuth"></a>
### DemoBasicAuth

- **Type**: HTTP basic authentication

<a id="DemoOAuth"></a>
### DemoOAuth

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **demo-bba-mailboxid**: 'mailboxid' dient vervangen te worden met het daadwerkelijke nummer van de mailbox.

<a id="AccOAuth"></a>
### AccOAuth

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **acc-bba-mailboxid**: 'mailboxid' dient vervangen te worden met het daadwerkelijke nummer van de mailbox.

<a id="LapOAuth"></a>
### LapOAuth

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **lap-bba-mailboxid**: 'mailboxid' dient vervangen te worden met het daadwerkelijke nummer van de mailbox.

<a id="PrdOAuth"></a>
### PrdOAuth

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **bba-mailboxid**: 'mailboxid' dient vervangen te worden met het daadwerkelijke nummer van de mailbox.


## Author




