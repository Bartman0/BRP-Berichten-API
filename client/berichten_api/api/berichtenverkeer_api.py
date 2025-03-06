# coding: utf-8

"""
    BRP Berichten API

    Een REST API voor het a-synchroon uitwisselen van berichten welke in het Logisch Ontwerp gedefinieerd zijn.  # Wijzigingshistorie:  ## 0.6.3 Januari 2025 - Tekstuele verwijzing naar '/berichten/list' vervangen door '/berichten'.  ## 0.6.2 Januari 2025 - OAuth endpoint demo omgeving gecorrigeerd.  ## 0.6.1 Januari 2025 - Ping endpoints zijn niet langer bereikbaar zonder eerst te authenticeren.  ## 0.6.0 Januari 2025 - Servers toegevoegd.   - Hiervoor moesten de paden van de endpoints aangepast worden. Hierdoor is '/api/v1' komen te vervallen bij de endpoints. Dit is verhuist naar de base-url's van de genoemde servers. - Authenticatie details toegevoegd. - Foutmeldingen bij het conversie endpoint bijgewerkt. - Alle namespace paden van de foutmeldingen nagelopen en gecorrigeerd daar waar nodig. Dit zodat ze consistent starten met: \"https://www.rvig.nl/brp/berichten-api/probleem/\".  ## 0.5.5 November 2024 - 'berichtVolgnummer' en 'afzender' required gemaakt in ListMessageKenmerken (en daardoor ook in GetMessageKenmerken). - De GET en DELETE foutsituaties zijn voorzien van discriminators ten behoeve van het onderscheiden van foutsituatie subtypes door de gegenereerde client.  ## 0.5.4 November 2024 - Properties van PagineringResultaat en PagineerbaarResultaat welke altijd aanwezig zullen zijn bij een list-request required gemaakt. - Required properties van put-message-antwoord gecorrigeerd. - Schema van het Null bericht gecorrigeerd.  ## 0.5.3 November 2024 - Het Sv11 bericht is qua schema aangepast aangezien deze onterecht de property plData bevatte. Deze property is verwijderd uit dit bericht. - Foutsituaties zijn voorzien van discriminators ten behoeve van het onderscheiden van foutsituatie subtypes door de gegenereerde client.  ## 0.5.2 Oktober 2024 - De request die volledig afgekeurd worden en een statuscode 4xx of 5xx retourneren, doen dit nu met de response header 'Content-Type: application/problem+json'. - Requests die een 2xx response in JSON formaat retourneren, doen dit met \"Content-Type: application/json\" ipv \"Content-Type: application/json: charset=utf-8\". Conform rfc8259 (https://www.rfc-editor.org/rfc/rfc8259) is JSON altijd in UTF-8 formaat en heeft dit type geen charset parameter.  ## 0.5.1 Oktober 2024  - De fout BBA-PUT-F002 is aangepast naar een algemene fout voor onjuiste velden in een PutMessage, via het veld \"invalidParams\" in de response word aangegeven welke velden onjuist zijn en waarom.  ## 0.5.0 September 2024  - Het veld berichtId en verwijzingBerichtId zijn omgezet van type 'integer' naar type 'string' om beter aan te sluiten op de bestaande voorziening.  - Het probleem-antwoord response object is overal vervangen met de algemene Foutmelding response welke zich conformeert aan RFC7807.  - De velden 'foutTitel', 'foutType', 'foutDetail' zijn aangepast naar 'title, 'type', 'detail' zodat zij zich conformeren aan de RFC7807.  - De afhankelijkheid op 'openapi-problem-detail-v1.yml' is komen te vervallen (https://github.com/rvig-brp/BRP-Berichten-API/issues/3).  ## 0.4.1 Juli 2024  - Het json-schema voor de autorisatieberichten Ct01, Cw01 en Cb01 is toegevoegd.  - De ontvanger is opgenomen in de response bij het verzenden van een bericht. Dit is met name relevant wanneer er een bericht naar een berichtgroep gestuurd wordt. In dat geval weet de verzender wie de uiteindelijke ontvangers zijn. Bij het versturen van een bericht naar de een regulier account zal dit nummer 1:1 overeenkomen met de ontvanger die bij het te verzenden bericht is opgegeven.  ## 0.4.0 Juni 2024 - De json-schema's van de berichtsoorten zijn opgenomen in de OpenAPI Specificatie. Voor elke berichtsoort die het LO beschrijft, is opgenomen hoe dit bericht gestructureerd is.   - Houdt er rekening mee dat het weergeven van de OpenAPI specificatie in de web-versie va SwaggerUI hierdoor trager geworden is. Het is aan te raden om de alternatieve (redocly) weergave te gebruiken:     - https://brp-berichten-api.dictua.ictu-sr.nl/openapi/berichten-api.html     - De JSON schema's zijn tevens te vinden op onze Github pagina. - De JSON-response van het conversie endpoint is iets aangepast zodat naast het geconverteerde bericht tevens validatiefouten opgenomen kunnen worden.  ## 0.3.0 - Mei 2024 - Conversie endpoints   - Introductie bericht-conversie (/berichten/conversie) endpoint. Houdt er rekening mee dat de conversie naar JSON opgenomen is, maar nog niet geïmplementeerd is in de demo omgeving. - Het limiet van het aantal berichten dat verwijderd kan worden is gelijkgesteld aan dat wat gelijktijdig opgehaald kan worden (100). - De API is hernoemd van \"BRP A-Synchrone berichten API\" naar \"BRP berichten API\".   - Nieuwe URL's demo omgeving:     - https://brp-berichten-api.dictua.ictu-sr.nl/api/v1/berichten     - https://brp-berichten-api.dictua.ictu-sr.nl/openapi/berichten-api.html     - https://brp-berichten-api.dictua.ictu-sr.nl/swagger-ui/index.html - Beschikbaarheid endpoint(s)   - Er is een tweede ping endpoint bijgekomen waardoor en nu een HEAD of een GET gedaan kan worden. De response blijft hetzelfde. U kunt zelf kiezen welke van deze twee u hanteert.   - De noodzaak voor authenticatie op het `ping` endpoint is komen te vervallen. U kunt dus zonder noodzaak van authenticatie vaststellen of de dienst beschikbaar is.  ## 0.2.2 - April 2024 - Ping operatie toegevoegd t.b.v. het verifiëren dat er communicatie met de berichtendienst mogelijks is. - De standaard sortering bij een LIST operatie is op dit moment:   1. `Datum + tijdstip van ontvangst` waarbij geldt dat het oudste bericht als eerste wordt weergegeven in de lijst met beschikbare berichten (rationale deze dient als eerste verwerkt worden door de ontvanger).   2. Indien `datum + tijdstip van ontvangst` gelijk zijn (wat kan voorkomen aangezien er meerdere berichten tegelijk ingestuurd kunnen worden), dan worden `afzender` en het `messageId` meegenomen in de sortering. De volgorde die de afzender toegekend heen via de messageId is op dat moment dus bepalend.  ## 0.2.1 - April 2024 - Mogelijkheden tot sortering bij een list operatie zijn verwijderd. De standaard sortering wordt nog bepaald. - Demo omgeving is toegevoegd aan de lijst met servers.   - API te benaderen via https://brp-berichten-api.dictua.ictu-sr.nl/api/v1/berichten   - Swagger UI via: https://brp-berichten-api.dictua.ictu-sr.nl/swagger-ui/index.html   - De OpenAPI specificatie via: https://brp-berichten-api.dictua.ictu-sr.nl/openapi.brp-berichten-api-v1.yaml - Wachtwoord wijzigingen optie is verwijderd. - Het `berichtFormaat` attribuut is komen te vervallen. Alle berichten zijn nu per definitie in JSON formaat. De eis om de berichtInhoud Base64 te   encoderen komt daarmee te vervallen. - Voorbeelddata verbeterd. - Tellingen endpoint toegevoegd welke invulling geeft aan de mailbox Summarize tegenhanger. - Delete endpoint gecorrigeerd. De collectie `succesvolVerwijderdeBerichten` was van het type string i.p.v. berichtTransportId. - Limieten zijn gewijzigd:   - Het aantal berichten dat via een PUT verstuurd kan worden is verhoogd naar 25. Uitgaande van een gemiddelde berichtgrootte van 40kb geeft dat een request van 1MB groot.   - Het aantal berichten dat via een LIST opgevraagd kan worden is vergroot naar 2000. Daarbij krijgt u de mogelijkheid om dit aantal te beperken.     - 2000 berichten in een LIST operatie komt neer op ongeveer 600KB response grootte.   - Het aantal berichten dat via een GET ontvangen kan worden is verhoogd naar 100. Dit heeft te maken met de gangbare (veilige) restricties van een URL qua lengte (2KB).     - Voor de URL worden 256 bytes gereserveerd.       - Voor de UUID blijven dan 1.792 bytes over.     - Een BerichtTransportId is 17 bytes groot (UUID + separatie-karakter ',')       - Uitgaande van 17 bytes, zou dit 105 keer herhaald kunnen worden. Om aan de veilige kan te zitten en om op een mooi rond getal uit te komen kiezen wij voor 100 als limiet.     - Uitgaande van een gemiddelde berichtgrootte van 40KB komt je met 100 berichten uit op 4MB qua response-grootte. - \"aantalKeerOpgehaald\" en \"dtLaatstOpgehaald\" zijn verwijderd uit response van LIST (ListMessageKenmerken schema). Wij zien hierin geen meerwaarde voor de aansluitende partijen. Wel kunt u blijven zien OF het bericht is opgehaald (boolean waarde).  ## 0.2.0 - April 2024 - \"List\" verzoek is verhuisd van \"/berichten/lijst\" --> \"/berichten\" - \"GET\" van meerdere berichten wordt gedaan middels path-parameters i.p.v. query-parameters en is samengevoegd met het endpoint voor het ophalen van een enkel bericht.<br/>   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID])   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID]) - \"DELETE\" van meerdere berichten wordt gedaan middels path-parameters i.p.v. query-parameters en is samengevoegd met het endpoint voor het verwijderen van een enkel bericht.<br/>   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID]) - Het \"berichtId\" wat correspondeert met het \"MessageId\" veld van de mailboxserver is qua type gewijzigd van String naar Integer. Maximale lengte 12.   - Beschrijving LO: MessageId, lengte: 12, Het unieke volgnummer dat aan het uitgaande bericht wordt toegekend. - Het veld \"verwijzingBerichtId\" wat correspondeert met het \"CrossReference\" veld van de mailboxserver:   - is qua type gewijzigd van String naar Integer. Maximale lengte 12.   - kan of weggelaten worden, of gevuld worden met 0 indien het bericht een eerste bericht in de cyclus betreft. - \"aantalKeerOpgehaald\" is toegevoegd aan de ListMessageKenmerken.  ## 0.1.0 - Maart 2024 Initiële versie.  # In ontwikkeling: - Bepalen of het een checksum op de berichtinhoud van meerwaarde kan zijn.  # Voorlopige limieten: | Waarde | Omschrijving | |--------|--------------| | 1      | Aantal ontvangers per bericht. | | 25     | Maximum aantal berichten dat in één PUT request verstuurd mag worden. | | 100     | Maximum aantal berichten dat in één DELETE request verwijderd mag worden | | 2000   | Maximum aantal berichten dat in één LIST request getoond zal worden. Indien wenselijk kunt u dit aantal middels een query-parameter beperken. | | 100    | Maximum aantal berichten dat in één GET request ontvangen mag worden. | | 64kb   | Maximum grootte van één enkel bericht. Één request zal qua grootte dan uitkomen op ((maximale-grootte-enkel-bericht * maximaal-aantal-berichten) + overhead). Houdt er rekening mee dat dit een waarde is die in te toekomst kan gaan groeien. Beperk uw oplossing dus niet op deze waarde! | 

    The version of the OpenAPI document: 0.6.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from berichten_api.models.delete_message_antwoord import DeleteMessageAntwoord
from berichten_api.models.get_message_antwoord import GetMessageAntwoord
from berichten_api.models.list_message_antwoord import ListMessageAntwoord
from berichten_api.models.put_message_antwoord import PutMessageAntwoord
from berichten_api.models.put_message_request import PutMessageRequest
from berichten_api.models.summarize200_response import Summarize200Response

from berichten_api.api_client import ApiClient, RequestSerialized
from berichten_api.api_response import ApiResponse
from berichten_api.rest import RESTResponseType


class BerichtenverkeerApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def delete_messages(
        self,
        bericht_transport_ids_param: Annotated[List[StrictStr], Field(description="Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`. ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> DeleteMessageAntwoord:
        """Het verwijderen van een of meerdere berichten (DELETE).

        Verwijderen van een of meerdere berichten. De berichten kunnen na deze actie niet meer bij de berichten API opgehaald worden. 

        :param bericht_transport_ids_param: Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`.  (required)
        :type bericht_transport_ids_param: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_messages_serialize(
            bericht_transport_ids_param=bericht_transport_ids_param,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DeleteMessageAntwoord",
            '400': "BBADELETEF004",
            '401': "ListMessages401Response",
            '500': "BBAF999",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_messages_with_http_info(
        self,
        bericht_transport_ids_param: Annotated[List[StrictStr], Field(description="Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`. ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[DeleteMessageAntwoord]:
        """Het verwijderen van een of meerdere berichten (DELETE).

        Verwijderen van een of meerdere berichten. De berichten kunnen na deze actie niet meer bij de berichten API opgehaald worden. 

        :param bericht_transport_ids_param: Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`.  (required)
        :type bericht_transport_ids_param: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_messages_serialize(
            bericht_transport_ids_param=bericht_transport_ids_param,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DeleteMessageAntwoord",
            '400': "BBADELETEF004",
            '401': "ListMessages401Response",
            '500': "BBAF999",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_messages_without_preload_content(
        self,
        bericht_transport_ids_param: Annotated[List[StrictStr], Field(description="Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`. ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Het verwijderen van een of meerdere berichten (DELETE).

        Verwijderen van een of meerdere berichten. De berichten kunnen na deze actie niet meer bij de berichten API opgehaald worden. 

        :param bericht_transport_ids_param: Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`.  (required)
        :type bericht_transport_ids_param: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_messages_serialize(
            bericht_transport_ids_param=bericht_transport_ids_param,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DeleteMessageAntwoord",
            '400': "BBADELETEF004",
            '401': "ListMessages401Response",
            '500': "BBAF999",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_messages_serialize(
        self,
        bericht_transport_ids_param,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'berichtTransportIdsParam': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if bericht_transport_ids_param is not None:
            _path_params['berichtTransportIdsParam'] = bericht_transport_ids_param
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'LapOAuth', 
            'PrdOAuth', 
            'DemoOAuth', 
            'AccOAuth', 
            'DemoBasicAuth'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/berichten/{berichtTransportIdsParam}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_messages(
        self,
        bericht_transport_ids_param: Annotated[List[StrictStr], Field(description="Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`. ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetMessageAntwoord:
        """Het ophalen van een of meerdere berichten (GET).

        Dit endpoint gebruikt u om berichten op te halen. 

        :param bericht_transport_ids_param: Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`.  (required)
        :type bericht_transport_ids_param: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_messages_serialize(
            bericht_transport_ids_param=bericht_transport_ids_param,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetMessageAntwoord",
            '400': "BBAGETF004",
            '401': "ListMessages401Response",
            '500': "BBAF999",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_messages_with_http_info(
        self,
        bericht_transport_ids_param: Annotated[List[StrictStr], Field(description="Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`. ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[GetMessageAntwoord]:
        """Het ophalen van een of meerdere berichten (GET).

        Dit endpoint gebruikt u om berichten op te halen. 

        :param bericht_transport_ids_param: Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`.  (required)
        :type bericht_transport_ids_param: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_messages_serialize(
            bericht_transport_ids_param=bericht_transport_ids_param,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetMessageAntwoord",
            '400': "BBAGETF004",
            '401': "ListMessages401Response",
            '500': "BBAF999",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_messages_without_preload_content(
        self,
        bericht_transport_ids_param: Annotated[List[StrictStr], Field(description="Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`. ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Het ophalen van een of meerdere berichten (GET).

        Dit endpoint gebruikt u om berichten op te halen. 

        :param bericht_transport_ids_param: Een UUID of meerdere UUID's van het bericht(en) die opgehaald moet worden. Indien meerdere UUID's, dan scheiden met een komma. Deze query parameter verwijst naar het berichtenId zoals deze bij de \"BRP berichten API\" bekend is, niet te verwarren met het BerichtId dat door de verzender is opgegeven. U verkrijgt deze UUID's middels een request naar `/berichten`.  (required)
        :type bericht_transport_ids_param: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_messages_serialize(
            bericht_transport_ids_param=bericht_transport_ids_param,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetMessageAntwoord",
            '400': "BBAGETF004",
            '401': "ListMessages401Response",
            '500': "BBAF999",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_messages_serialize(
        self,
        bericht_transport_ids_param,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'berichtTransportIdsParam': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if bericht_transport_ids_param is not None:
            _path_params['berichtTransportIdsParam'] = bericht_transport_ids_param
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'LapOAuth', 
            'PrdOAuth', 
            'DemoOAuth', 
            'AccOAuth', 
            'DemoBasicAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/berichten/{berichtTransportIdsParam}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_messages(
        self,
        status: Annotated[Optional[List[StrictStr]], Field(description="Geeft aan welke berichten opgenomen moeten worden in het resultaat. Comma-gescheiden veld. Indien leeg worden alle niet opgehaalde berichten getoond (`nieuw` + `gezien-in-lijst`).    - `nieuw`: Geeft berichten welke nog nooit opgehaald zijn en tevens niet in de lijst operatie zijn getoond.   - `gezien-in-lijst`: Geeft berichten die nog niet opgehaald zijn, maar al wel gezien zijn in de lijst.   - `opgehaald`: Geeft berichten reeds opgehaald zijn. ")] = None,
        bericht_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=4)]], Field(description="Geeft aan welke type berichten opgenomen moeten worden in het resultaat. Indien leeg of niet aanwezig worden alle berichten getoond. Niet hoofdlettergevoelig.")] = None,
        vanaf_moment: Annotated[Optional[datetime], Field(description="Het resultaat zal alleen berichten bevatten die vanaf dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond die nog beschikbaar zijn (waarvan de retentietijd nog niet verlopen is).")] = None,
        tot_moment: Annotated[Optional[datetime], Field(description="Het resultaat zal alleen berichten bevatten die tot dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond t/m het heden.")] = None,
        pagina: Annotated[Optional[StrictInt], Field(description="Pagina nummer, startend bij 1 t/m N (niet bij 0).")] = None,
        berichten_per_pagina: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Het maximum aantal berichten dat geretourneerd mag worden. Indien deze waarde het ingesteld systeemlimiet overschrijdt, dan wordt het systeemlimiet gehanteerd. Indien er geen waarde wordt opgegeven, dan wordt tevens het systeemlimiet gehanteerd. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ListMessageAntwoord:
        """Het ophalen van een lijst met berichten die klaarstaan (LIST).

        Dit endpoint gebruikt u om te achterhalen welke berichten er voor u beschikbaar zijn. 

        :param status: Geeft aan welke berichten opgenomen moeten worden in het resultaat. Comma-gescheiden veld. Indien leeg worden alle niet opgehaalde berichten getoond (`nieuw` + `gezien-in-lijst`).    - `nieuw`: Geeft berichten welke nog nooit opgehaald zijn en tevens niet in de lijst operatie zijn getoond.   - `gezien-in-lijst`: Geeft berichten die nog niet opgehaald zijn, maar al wel gezien zijn in de lijst.   - `opgehaald`: Geeft berichten reeds opgehaald zijn. 
        :type status: List[str]
        :param bericht_type: Geeft aan welke type berichten opgenomen moeten worden in het resultaat. Indien leeg of niet aanwezig worden alle berichten getoond. Niet hoofdlettergevoelig.
        :type bericht_type: str
        :param vanaf_moment: Het resultaat zal alleen berichten bevatten die vanaf dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond die nog beschikbaar zijn (waarvan de retentietijd nog niet verlopen is).
        :type vanaf_moment: datetime
        :param tot_moment: Het resultaat zal alleen berichten bevatten die tot dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond t/m het heden.
        :type tot_moment: datetime
        :param pagina: Pagina nummer, startend bij 1 t/m N (niet bij 0).
        :type pagina: int
        :param berichten_per_pagina: Het maximum aantal berichten dat geretourneerd mag worden. Indien deze waarde het ingesteld systeemlimiet overschrijdt, dan wordt het systeemlimiet gehanteerd. Indien er geen waarde wordt opgegeven, dan wordt tevens het systeemlimiet gehanteerd. 
        :type berichten_per_pagina: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_messages_serialize(
            status=status,
            bericht_type=bericht_type,
            vanaf_moment=vanaf_moment,
            tot_moment=tot_moment,
            pagina=pagina,
            berichten_per_pagina=berichten_per_pagina,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListMessageAntwoord",
            '400': "BBALISTF001",
            '401': "ListMessages401Response",
            '500': "Foutmelding",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_messages_with_http_info(
        self,
        status: Annotated[Optional[List[StrictStr]], Field(description="Geeft aan welke berichten opgenomen moeten worden in het resultaat. Comma-gescheiden veld. Indien leeg worden alle niet opgehaalde berichten getoond (`nieuw` + `gezien-in-lijst`).    - `nieuw`: Geeft berichten welke nog nooit opgehaald zijn en tevens niet in de lijst operatie zijn getoond.   - `gezien-in-lijst`: Geeft berichten die nog niet opgehaald zijn, maar al wel gezien zijn in de lijst.   - `opgehaald`: Geeft berichten reeds opgehaald zijn. ")] = None,
        bericht_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=4)]], Field(description="Geeft aan welke type berichten opgenomen moeten worden in het resultaat. Indien leeg of niet aanwezig worden alle berichten getoond. Niet hoofdlettergevoelig.")] = None,
        vanaf_moment: Annotated[Optional[datetime], Field(description="Het resultaat zal alleen berichten bevatten die vanaf dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond die nog beschikbaar zijn (waarvan de retentietijd nog niet verlopen is).")] = None,
        tot_moment: Annotated[Optional[datetime], Field(description="Het resultaat zal alleen berichten bevatten die tot dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond t/m het heden.")] = None,
        pagina: Annotated[Optional[StrictInt], Field(description="Pagina nummer, startend bij 1 t/m N (niet bij 0).")] = None,
        berichten_per_pagina: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Het maximum aantal berichten dat geretourneerd mag worden. Indien deze waarde het ingesteld systeemlimiet overschrijdt, dan wordt het systeemlimiet gehanteerd. Indien er geen waarde wordt opgegeven, dan wordt tevens het systeemlimiet gehanteerd. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ListMessageAntwoord]:
        """Het ophalen van een lijst met berichten die klaarstaan (LIST).

        Dit endpoint gebruikt u om te achterhalen welke berichten er voor u beschikbaar zijn. 

        :param status: Geeft aan welke berichten opgenomen moeten worden in het resultaat. Comma-gescheiden veld. Indien leeg worden alle niet opgehaalde berichten getoond (`nieuw` + `gezien-in-lijst`).    - `nieuw`: Geeft berichten welke nog nooit opgehaald zijn en tevens niet in de lijst operatie zijn getoond.   - `gezien-in-lijst`: Geeft berichten die nog niet opgehaald zijn, maar al wel gezien zijn in de lijst.   - `opgehaald`: Geeft berichten reeds opgehaald zijn. 
        :type status: List[str]
        :param bericht_type: Geeft aan welke type berichten opgenomen moeten worden in het resultaat. Indien leeg of niet aanwezig worden alle berichten getoond. Niet hoofdlettergevoelig.
        :type bericht_type: str
        :param vanaf_moment: Het resultaat zal alleen berichten bevatten die vanaf dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond die nog beschikbaar zijn (waarvan de retentietijd nog niet verlopen is).
        :type vanaf_moment: datetime
        :param tot_moment: Het resultaat zal alleen berichten bevatten die tot dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond t/m het heden.
        :type tot_moment: datetime
        :param pagina: Pagina nummer, startend bij 1 t/m N (niet bij 0).
        :type pagina: int
        :param berichten_per_pagina: Het maximum aantal berichten dat geretourneerd mag worden. Indien deze waarde het ingesteld systeemlimiet overschrijdt, dan wordt het systeemlimiet gehanteerd. Indien er geen waarde wordt opgegeven, dan wordt tevens het systeemlimiet gehanteerd. 
        :type berichten_per_pagina: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_messages_serialize(
            status=status,
            bericht_type=bericht_type,
            vanaf_moment=vanaf_moment,
            tot_moment=tot_moment,
            pagina=pagina,
            berichten_per_pagina=berichten_per_pagina,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListMessageAntwoord",
            '400': "BBALISTF001",
            '401': "ListMessages401Response",
            '500': "Foutmelding",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_messages_without_preload_content(
        self,
        status: Annotated[Optional[List[StrictStr]], Field(description="Geeft aan welke berichten opgenomen moeten worden in het resultaat. Comma-gescheiden veld. Indien leeg worden alle niet opgehaalde berichten getoond (`nieuw` + `gezien-in-lijst`).    - `nieuw`: Geeft berichten welke nog nooit opgehaald zijn en tevens niet in de lijst operatie zijn getoond.   - `gezien-in-lijst`: Geeft berichten die nog niet opgehaald zijn, maar al wel gezien zijn in de lijst.   - `opgehaald`: Geeft berichten reeds opgehaald zijn. ")] = None,
        bericht_type: Annotated[Optional[Annotated[str, Field(strict=True, max_length=4)]], Field(description="Geeft aan welke type berichten opgenomen moeten worden in het resultaat. Indien leeg of niet aanwezig worden alle berichten getoond. Niet hoofdlettergevoelig.")] = None,
        vanaf_moment: Annotated[Optional[datetime], Field(description="Het resultaat zal alleen berichten bevatten die vanaf dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond die nog beschikbaar zijn (waarvan de retentietijd nog niet verlopen is).")] = None,
        tot_moment: Annotated[Optional[datetime], Field(description="Het resultaat zal alleen berichten bevatten die tot dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond t/m het heden.")] = None,
        pagina: Annotated[Optional[StrictInt], Field(description="Pagina nummer, startend bij 1 t/m N (niet bij 0).")] = None,
        berichten_per_pagina: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Het maximum aantal berichten dat geretourneerd mag worden. Indien deze waarde het ingesteld systeemlimiet overschrijdt, dan wordt het systeemlimiet gehanteerd. Indien er geen waarde wordt opgegeven, dan wordt tevens het systeemlimiet gehanteerd. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Het ophalen van een lijst met berichten die klaarstaan (LIST).

        Dit endpoint gebruikt u om te achterhalen welke berichten er voor u beschikbaar zijn. 

        :param status: Geeft aan welke berichten opgenomen moeten worden in het resultaat. Comma-gescheiden veld. Indien leeg worden alle niet opgehaalde berichten getoond (`nieuw` + `gezien-in-lijst`).    - `nieuw`: Geeft berichten welke nog nooit opgehaald zijn en tevens niet in de lijst operatie zijn getoond.   - `gezien-in-lijst`: Geeft berichten die nog niet opgehaald zijn, maar al wel gezien zijn in de lijst.   - `opgehaald`: Geeft berichten reeds opgehaald zijn. 
        :type status: List[str]
        :param bericht_type: Geeft aan welke type berichten opgenomen moeten worden in het resultaat. Indien leeg of niet aanwezig worden alle berichten getoond. Niet hoofdlettergevoelig.
        :type bericht_type: str
        :param vanaf_moment: Het resultaat zal alleen berichten bevatten die vanaf dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond die nog beschikbaar zijn (waarvan de retentietijd nog niet verlopen is).
        :type vanaf_moment: datetime
        :param tot_moment: Het resultaat zal alleen berichten bevatten die tot dit moment ontvangen zijn. Wanneer deze waarde niet opgegeven is, worden alle berichten getoond t/m het heden.
        :type tot_moment: datetime
        :param pagina: Pagina nummer, startend bij 1 t/m N (niet bij 0).
        :type pagina: int
        :param berichten_per_pagina: Het maximum aantal berichten dat geretourneerd mag worden. Indien deze waarde het ingesteld systeemlimiet overschrijdt, dan wordt het systeemlimiet gehanteerd. Indien er geen waarde wordt opgegeven, dan wordt tevens het systeemlimiet gehanteerd. 
        :type berichten_per_pagina: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_messages_serialize(
            status=status,
            bericht_type=bericht_type,
            vanaf_moment=vanaf_moment,
            tot_moment=tot_moment,
            pagina=pagina,
            berichten_per_pagina=berichten_per_pagina,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListMessageAntwoord",
            '400': "BBALISTF001",
            '401': "ListMessages401Response",
            '500': "Foutmelding",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_messages_serialize(
        self,
        status,
        bericht_type,
        vanaf_moment,
        tot_moment,
        pagina,
        berichten_per_pagina,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'status': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if status is not None:
            
            _query_params.append(('status', status))
            
        if bericht_type is not None:
            
            _query_params.append(('berichtType', bericht_type))
            
        if vanaf_moment is not None:
            if isinstance(vanaf_moment, datetime):
                _query_params.append(
                    (
                        'vanafMoment',
                        vanaf_moment.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('vanafMoment', vanaf_moment))
            
        if tot_moment is not None:
            if isinstance(tot_moment, datetime):
                _query_params.append(
                    (
                        'totMoment',
                        tot_moment.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('totMoment', tot_moment))
            
        if pagina is not None:
            
            _query_params.append(('pagina', pagina))
            
        if berichten_per_pagina is not None:
            
            _query_params.append(('berichtenPerPagina', berichten_per_pagina))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'LapOAuth', 
            'PrdOAuth', 
            'DemoOAuth', 
            'AccOAuth', 
            'DemoBasicAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/berichten',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def put_messages(
        self,
        put_message_request: Optional[PutMessageRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PutMessageAntwoord:
        """Het versturen van een of meerdere berichten (PUT).

        Dit endpoint gebruikt u om berichten zoals gespecificeerd in het Logisch Ontwerp te versturen. 

        :param put_message_request:
        :type put_message_request: PutMessageRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._put_messages_serialize(
            put_message_request=put_message_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "PutMessageAntwoord",
            '400': "BBAPUTF001",
            '401': "ListMessages401Response",
            '500': "BBAF999",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def put_messages_with_http_info(
        self,
        put_message_request: Optional[PutMessageRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PutMessageAntwoord]:
        """Het versturen van een of meerdere berichten (PUT).

        Dit endpoint gebruikt u om berichten zoals gespecificeerd in het Logisch Ontwerp te versturen. 

        :param put_message_request:
        :type put_message_request: PutMessageRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._put_messages_serialize(
            put_message_request=put_message_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "PutMessageAntwoord",
            '400': "BBAPUTF001",
            '401': "ListMessages401Response",
            '500': "BBAF999",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def put_messages_without_preload_content(
        self,
        put_message_request: Optional[PutMessageRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Het versturen van een of meerdere berichten (PUT).

        Dit endpoint gebruikt u om berichten zoals gespecificeerd in het Logisch Ontwerp te versturen. 

        :param put_message_request:
        :type put_message_request: PutMessageRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._put_messages_serialize(
            put_message_request=put_message_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "PutMessageAntwoord",
            '400': "BBAPUTF001",
            '401': "ListMessages401Response",
            '500': "BBAF999",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _put_messages_serialize(
        self,
        put_message_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if put_message_request is not None:
            _body_params = put_message_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'LapOAuth', 
            'PrdOAuth', 
            'DemoOAuth', 
            'AccOAuth', 
            'DemoBasicAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/berichten',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def summarize(
        self,
        soort: Annotated[StrictStr, Field(description="Geeft aan welke telling er uitgevoerd moet worden.   - nieuw: Geeft het aantal nieuwe berichten terug dat nog niet gezien is via een LIST operatie en tevens nog niet opgehaald is middels een GET operatie.   - gezien-in-lijst-en-niet-opgehaald: Geeft het aantal nieuwe berichten terug dat gezien is via een LIST operatie, maar nog niet opgehaald is middels een GET operatie.   - niet-opgehaald: Geeft het aantal nieuwe berichten terug dat nog niet opgehaald is middels een GET operatie. ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Summarize200Response:
        """Voert verschillende soorten tellingen uit waarmee bepaald kan worden hoeveel berichten er verwerkt dienen te worden (SUMMARIZE).


        :param soort: Geeft aan welke telling er uitgevoerd moet worden.   - nieuw: Geeft het aantal nieuwe berichten terug dat nog niet gezien is via een LIST operatie en tevens nog niet opgehaald is middels een GET operatie.   - gezien-in-lijst-en-niet-opgehaald: Geeft het aantal nieuwe berichten terug dat gezien is via een LIST operatie, maar nog niet opgehaald is middels een GET operatie.   - niet-opgehaald: Geeft het aantal nieuwe berichten terug dat nog niet opgehaald is middels een GET operatie.  (required)
        :type soort: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._summarize_serialize(
            soort=soort,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Summarize200Response",
            '400': "BBASUMMARIZEF001",
            '401': "ListMessages401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def summarize_with_http_info(
        self,
        soort: Annotated[StrictStr, Field(description="Geeft aan welke telling er uitgevoerd moet worden.   - nieuw: Geeft het aantal nieuwe berichten terug dat nog niet gezien is via een LIST operatie en tevens nog niet opgehaald is middels een GET operatie.   - gezien-in-lijst-en-niet-opgehaald: Geeft het aantal nieuwe berichten terug dat gezien is via een LIST operatie, maar nog niet opgehaald is middels een GET operatie.   - niet-opgehaald: Geeft het aantal nieuwe berichten terug dat nog niet opgehaald is middels een GET operatie. ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Summarize200Response]:
        """Voert verschillende soorten tellingen uit waarmee bepaald kan worden hoeveel berichten er verwerkt dienen te worden (SUMMARIZE).


        :param soort: Geeft aan welke telling er uitgevoerd moet worden.   - nieuw: Geeft het aantal nieuwe berichten terug dat nog niet gezien is via een LIST operatie en tevens nog niet opgehaald is middels een GET operatie.   - gezien-in-lijst-en-niet-opgehaald: Geeft het aantal nieuwe berichten terug dat gezien is via een LIST operatie, maar nog niet opgehaald is middels een GET operatie.   - niet-opgehaald: Geeft het aantal nieuwe berichten terug dat nog niet opgehaald is middels een GET operatie.  (required)
        :type soort: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._summarize_serialize(
            soort=soort,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Summarize200Response",
            '400': "BBASUMMARIZEF001",
            '401': "ListMessages401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def summarize_without_preload_content(
        self,
        soort: Annotated[StrictStr, Field(description="Geeft aan welke telling er uitgevoerd moet worden.   - nieuw: Geeft het aantal nieuwe berichten terug dat nog niet gezien is via een LIST operatie en tevens nog niet opgehaald is middels een GET operatie.   - gezien-in-lijst-en-niet-opgehaald: Geeft het aantal nieuwe berichten terug dat gezien is via een LIST operatie, maar nog niet opgehaald is middels een GET operatie.   - niet-opgehaald: Geeft het aantal nieuwe berichten terug dat nog niet opgehaald is middels een GET operatie. ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Voert verschillende soorten tellingen uit waarmee bepaald kan worden hoeveel berichten er verwerkt dienen te worden (SUMMARIZE).


        :param soort: Geeft aan welke telling er uitgevoerd moet worden.   - nieuw: Geeft het aantal nieuwe berichten terug dat nog niet gezien is via een LIST operatie en tevens nog niet opgehaald is middels een GET operatie.   - gezien-in-lijst-en-niet-opgehaald: Geeft het aantal nieuwe berichten terug dat gezien is via een LIST operatie, maar nog niet opgehaald is middels een GET operatie.   - niet-opgehaald: Geeft het aantal nieuwe berichten terug dat nog niet opgehaald is middels een GET operatie.  (required)
        :type soort: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._summarize_serialize(
            soort=soort,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Summarize200Response",
            '400': "BBASUMMARIZEF001",
            '401': "ListMessages401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _summarize_serialize(
        self,
        soort,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if soort is not None:
            
            _query_params.append(('soort', soort))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'LapOAuth', 
            'PrdOAuth', 
            'DemoOAuth', 
            'AccOAuth', 
            'DemoBasicAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/berichten/telling',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


