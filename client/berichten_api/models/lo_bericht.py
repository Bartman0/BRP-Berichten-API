# coding: utf-8

"""
    BRP Berichten API

    Een REST API voor het a-synchroon uitwisselen van berichten welke in het Logisch Ontwerp gedefinieerd zijn.  # Wijzigingshistorie:  ## 0.6.3 Januari 2025 - Tekstuele verwijzing naar '/berichten/list' vervangen door '/berichten'.  ## 0.6.2 Januari 2025 - OAuth endpoint demo omgeving gecorrigeerd.  ## 0.6.1 Januari 2025 - Ping endpoints zijn niet langer bereikbaar zonder eerst te authenticeren.  ## 0.6.0 Januari 2025 - Servers toegevoegd.   - Hiervoor moesten de paden van de endpoints aangepast worden. Hierdoor is '/api/v1' komen te vervallen bij de endpoints. Dit is verhuist naar de base-url's van de genoemde servers. - Authenticatie details toegevoegd. - Foutmeldingen bij het conversie endpoint bijgewerkt. - Alle namespace paden van de foutmeldingen nagelopen en gecorrigeerd daar waar nodig. Dit zodat ze consistent starten met: \"https://www.rvig.nl/brp/berichten-api/probleem/\".  ## 0.5.5 November 2024 - 'berichtVolgnummer' en 'afzender' required gemaakt in ListMessageKenmerken (en daardoor ook in GetMessageKenmerken). - De GET en DELETE foutsituaties zijn voorzien van discriminators ten behoeve van het onderscheiden van foutsituatie subtypes door de gegenereerde client.  ## 0.5.4 November 2024 - Properties van PagineringResultaat en PagineerbaarResultaat welke altijd aanwezig zullen zijn bij een list-request required gemaakt. - Required properties van put-message-antwoord gecorrigeerd. - Schema van het Null bericht gecorrigeerd.  ## 0.5.3 November 2024 - Het Sv11 bericht is qua schema aangepast aangezien deze onterecht de property plData bevatte. Deze property is verwijderd uit dit bericht. - Foutsituaties zijn voorzien van discriminators ten behoeve van het onderscheiden van foutsituatie subtypes door de gegenereerde client.  ## 0.5.2 Oktober 2024 - De request die volledig afgekeurd worden en een statuscode 4xx of 5xx retourneren, doen dit nu met de response header 'Content-Type: application/problem+json'. - Requests die een 2xx response in JSON formaat retourneren, doen dit met \"Content-Type: application/json\" ipv \"Content-Type: application/json: charset=utf-8\". Conform rfc8259 (https://www.rfc-editor.org/rfc/rfc8259) is JSON altijd in UTF-8 formaat en heeft dit type geen charset parameter.  ## 0.5.1 Oktober 2024  - De fout BBA-PUT-F002 is aangepast naar een algemene fout voor onjuiste velden in een PutMessage, via het veld \"invalidParams\" in de response word aangegeven welke velden onjuist zijn en waarom.  ## 0.5.0 September 2024  - Het veld berichtId en verwijzingBerichtId zijn omgezet van type 'integer' naar type 'string' om beter aan te sluiten op de bestaande voorziening.  - Het probleem-antwoord response object is overal vervangen met de algemene Foutmelding response welke zich conformeert aan RFC7807.  - De velden 'foutTitel', 'foutType', 'foutDetail' zijn aangepast naar 'title, 'type', 'detail' zodat zij zich conformeren aan de RFC7807.  - De afhankelijkheid op 'openapi-problem-detail-v1.yml' is komen te vervallen (https://github.com/rvig-brp/BRP-Berichten-API/issues/3).  ## 0.4.1 Juli 2024  - Het json-schema voor de autorisatieberichten Ct01, Cw01 en Cb01 is toegevoegd.  - De ontvanger is opgenomen in de response bij het verzenden van een bericht. Dit is met name relevant wanneer er een bericht naar een berichtgroep gestuurd wordt. In dat geval weet de verzender wie de uiteindelijke ontvangers zijn. Bij het versturen van een bericht naar de een regulier account zal dit nummer 1:1 overeenkomen met de ontvanger die bij het te verzenden bericht is opgegeven.  ## 0.4.0 Juni 2024 - De json-schema's van de berichtsoorten zijn opgenomen in de OpenAPI Specificatie. Voor elke berichtsoort die het LO beschrijft, is opgenomen hoe dit bericht gestructureerd is.   - Houdt er rekening mee dat het weergeven van de OpenAPI specificatie in de web-versie va SwaggerUI hierdoor trager geworden is. Het is aan te raden om de alternatieve (redocly) weergave te gebruiken:     - https://brp-berichten-api.dictua.ictu-sr.nl/openapi/berichten-api.html     - De JSON schema's zijn tevens te vinden op onze Github pagina. - De JSON-response van het conversie endpoint is iets aangepast zodat naast het geconverteerde bericht tevens validatiefouten opgenomen kunnen worden.  ## 0.3.0 - Mei 2024 - Conversie endpoints   - Introductie bericht-conversie (/berichten/conversie) endpoint. Houdt er rekening mee dat de conversie naar JSON opgenomen is, maar nog niet geïmplementeerd is in de demo omgeving. - Het limiet van het aantal berichten dat verwijderd kan worden is gelijkgesteld aan dat wat gelijktijdig opgehaald kan worden (100). - De API is hernoemd van \"BRP A-Synchrone berichten API\" naar \"BRP berichten API\".   - Nieuwe URL's demo omgeving:     - https://brp-berichten-api.dictua.ictu-sr.nl/api/v1/berichten     - https://brp-berichten-api.dictua.ictu-sr.nl/openapi/berichten-api.html     - https://brp-berichten-api.dictua.ictu-sr.nl/swagger-ui/index.html - Beschikbaarheid endpoint(s)   - Er is een tweede ping endpoint bijgekomen waardoor en nu een HEAD of een GET gedaan kan worden. De response blijft hetzelfde. U kunt zelf kiezen welke van deze twee u hanteert.   - De noodzaak voor authenticatie op het `ping` endpoint is komen te vervallen. U kunt dus zonder noodzaak van authenticatie vaststellen of de dienst beschikbaar is.  ## 0.2.2 - April 2024 - Ping operatie toegevoegd t.b.v. het verifiëren dat er communicatie met de berichtendienst mogelijks is. - De standaard sortering bij een LIST operatie is op dit moment:   1. `Datum + tijdstip van ontvangst` waarbij geldt dat het oudste bericht als eerste wordt weergegeven in de lijst met beschikbare berichten (rationale deze dient als eerste verwerkt worden door de ontvanger).   2. Indien `datum + tijdstip van ontvangst` gelijk zijn (wat kan voorkomen aangezien er meerdere berichten tegelijk ingestuurd kunnen worden), dan worden `afzender` en het `messageId` meegenomen in de sortering. De volgorde die de afzender toegekend heen via de messageId is op dat moment dus bepalend.  ## 0.2.1 - April 2024 - Mogelijkheden tot sortering bij een list operatie zijn verwijderd. De standaard sortering wordt nog bepaald. - Demo omgeving is toegevoegd aan de lijst met servers.   - API te benaderen via https://brp-berichten-api.dictua.ictu-sr.nl/api/v1/berichten   - Swagger UI via: https://brp-berichten-api.dictua.ictu-sr.nl/swagger-ui/index.html   - De OpenAPI specificatie via: https://brp-berichten-api.dictua.ictu-sr.nl/openapi.brp-berichten-api-v1.yaml - Wachtwoord wijzigingen optie is verwijderd. - Het `berichtFormaat` attribuut is komen te vervallen. Alle berichten zijn nu per definitie in JSON formaat. De eis om de berichtInhoud Base64 te   encoderen komt daarmee te vervallen. - Voorbeelddata verbeterd. - Tellingen endpoint toegevoegd welke invulling geeft aan de mailbox Summarize tegenhanger. - Delete endpoint gecorrigeerd. De collectie `succesvolVerwijderdeBerichten` was van het type string i.p.v. berichtTransportId. - Limieten zijn gewijzigd:   - Het aantal berichten dat via een PUT verstuurd kan worden is verhoogd naar 25. Uitgaande van een gemiddelde berichtgrootte van 40kb geeft dat een request van 1MB groot.   - Het aantal berichten dat via een LIST opgevraagd kan worden is vergroot naar 2000. Daarbij krijgt u de mogelijkheid om dit aantal te beperken.     - 2000 berichten in een LIST operatie komt neer op ongeveer 600KB response grootte.   - Het aantal berichten dat via een GET ontvangen kan worden is verhoogd naar 100. Dit heeft te maken met de gangbare (veilige) restricties van een URL qua lengte (2KB).     - Voor de URL worden 256 bytes gereserveerd.       - Voor de UUID blijven dan 1.792 bytes over.     - Een BerichtTransportId is 17 bytes groot (UUID + separatie-karakter ',')       - Uitgaande van 17 bytes, zou dit 105 keer herhaald kunnen worden. Om aan de veilige kan te zitten en om op een mooi rond getal uit te komen kiezen wij voor 100 als limiet.     - Uitgaande van een gemiddelde berichtgrootte van 40KB komt je met 100 berichten uit op 4MB qua response-grootte. - \"aantalKeerOpgehaald\" en \"dtLaatstOpgehaald\" zijn verwijderd uit response van LIST (ListMessageKenmerken schema). Wij zien hierin geen meerwaarde voor de aansluitende partijen. Wel kunt u blijven zien OF het bericht is opgehaald (boolean waarde).  ## 0.2.0 - April 2024 - \"List\" verzoek is verhuisd van \"/berichten/lijst\" --> \"/berichten\" - \"GET\" van meerdere berichten wordt gedaan middels path-parameters i.p.v. query-parameters en is samengevoegd met het endpoint voor het ophalen van een enkel bericht.<br/>   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID])   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID]) - \"DELETE\" van meerdere berichten wordt gedaan middels path-parameters i.p.v. query-parameters en is samengevoegd met het endpoint voor het verwijderen van een enkel bericht.<br/>   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID]) - Het \"berichtId\" wat correspondeert met het \"MessageId\" veld van de mailboxserver is qua type gewijzigd van String naar Integer. Maximale lengte 12.   - Beschrijving LO: MessageId, lengte: 12, Het unieke volgnummer dat aan het uitgaande bericht wordt toegekend. - Het veld \"verwijzingBerichtId\" wat correspondeert met het \"CrossReference\" veld van de mailboxserver:   - is qua type gewijzigd van String naar Integer. Maximale lengte 12.   - kan of weggelaten worden, of gevuld worden met 0 indien het bericht een eerste bericht in de cyclus betreft. - \"aantalKeerOpgehaald\" is toegevoegd aan de ListMessageKenmerken.  ## 0.1.0 - Maart 2024 Initiële versie.  # In ontwikkeling: - Bepalen of het een checksum op de berichtinhoud van meerwaarde kan zijn.  # Voorlopige limieten: | Waarde | Omschrijving | |--------|--------------| | 1      | Aantal ontvangers per bericht. | | 25     | Maximum aantal berichten dat in één PUT request verstuurd mag worden. | | 100     | Maximum aantal berichten dat in één DELETE request verwijderd mag worden | | 2000   | Maximum aantal berichten dat in één LIST request getoond zal worden. Indien wenselijk kunt u dit aantal middels een query-parameter beperken. | | 100    | Maximum aantal berichten dat in één GET request ontvangen mag worden. | | 64kb   | Maximum grootte van één enkel bericht. Één request zal qua grootte dan uitkomen op ((maximale-grootte-enkel-bericht * maximaal-aantal-berichten) + overhead). Houdt er rekening mee dat dit een waarde is die in te toekomst kan gaan groeien. Beperk uw oplossing dus niet op deze waarde! | 

    The version of the OpenAPI document: 0.6.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from berichten_api.models.af01 import Af01
from berichten_api.models.af11 import Af11
from berichten_api.models.ag01 import Ag01
from berichten_api.models.ag11 import Ag11
from berichten_api.models.ag21 import Ag21
from berichten_api.models.ag31 import Ag31
from berichten_api.models.ap01 import Ap01
from berichten_api.models.av01 import Av01
from berichten_api.models.cb01 import Cb01
from berichten_api.models.ct01 import Ct01
from berichten_api.models.cw01 import Cw01
from berichten_api.models.dt01 import Dt01
from berichten_api.models.dw01 import Dw01
from berichten_api.models.gv01 import Gv01
from berichten_api.models.gv02 import Gv02
from berichten_api.models.ha01 import Ha01
from berichten_api.models.hf01 import Hf01
from berichten_api.models.hq01 import Hq01
from berichten_api.models.ib01 import Ib01
from berichten_api.models.if01 import If01
from berichten_api.models.if21 import If21
from berichten_api.models.if31 import If31
from berichten_api.models.if41 import If41
from berichten_api.models.ii01 import Ii01
from berichten_api.models.iv01 import Iv01
from berichten_api.models.iv11 import Iv11
from berichten_api.models.iv21 import Iv21
from berichten_api.models.jb01 import Jb01
from berichten_api.models.jf01 import Jf01
from berichten_api.models.jf21 import Jf21
from berichten_api.models.jf31 import Jf31
from berichten_api.models.ji01 import Ji01
from berichten_api.models.jv01 import Jv01
from berichten_api.models.la01 import La01
from berichten_api.models.lf01 import Lf01
from berichten_api.models.lg01 import Lg01
from berichten_api.models.lq01 import Lq01
from berichten_api.models.ng01 import Ng01
from berichten_api.models.null import Null
from berichten_api.models.of11 import Of11
from berichten_api.models.og11 import Og11
from berichten_api.models.pf01 import Pf01
from berichten_api.models.pf02 import Pf02
from berichten_api.models.pf03 import Pf03
from berichten_api.models.rb01 import Rb01
from berichten_api.models.rf01 import Rf01
from berichten_api.models.rf31 import Rf31
from berichten_api.models.rv01 import Rv01
from berichten_api.models.sv01 import Sv01
from berichten_api.models.sv11 import Sv11
from berichten_api.models.tb01 import Tb01
from berichten_api.models.tb02 import Tb02
from berichten_api.models.tf01 import Tf01
from berichten_api.models.tf11 import Tf11
from berichten_api.models.tf21 import Tf21
from berichten_api.models.tv01 import Tv01
from berichten_api.models.vb01 import Vb01
from berichten_api.models.vb02 import Vb02
from berichten_api.models.wa01 import Wa01
from berichten_api.models.wa11 import Wa11
from berichten_api.models.wf01 import Wf01
from berichten_api.models.xa01 import Xa01
from berichten_api.models.xf01 import Xf01
from berichten_api.models.xq01 import Xq01
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

LOBERICHT_ONE_OF_SCHEMAS = ["Af01", "Af11", "Ag01", "Ag11", "Ag21", "Ag31", "Ap01", "Av01", "Cb01", "Ct01", "Cw01", "Dt01", "Dw01", "Gv01", "Gv02", "Ha01", "Hf01", "Hq01", "Ib01", "If01", "If21", "If31", "If41", "Ii01", "Iv01", "Iv11", "Iv21", "Jb01", "Jf01", "Jf21", "Jf31", "Ji01", "Jv01", "La01", "Lf01", "Lg01", "Lq01", "Ng01", "Null", "Of11", "Og11", "Pf01", "Pf02", "Pf03", "Rb01", "Rf01", "Rf31", "Rv01", "Sv01", "Sv11", "Tb01", "Tb02", "Tf01", "Tf11", "Tf21", "Tv01", "Vb01", "Vb02", "Wa01", "Wa11", "Wf01", "Xa01", "Xf01", "Xq01"]

class LoBericht(BaseModel):
    """
    LoBericht
    """
    # data type: Af01
    oneof_schema_1_validator: Optional[Af01] = None
    # data type: Af11
    oneof_schema_2_validator: Optional[Af11] = None
    # data type: Ag01
    oneof_schema_3_validator: Optional[Ag01] = None
    # data type: Ag11
    oneof_schema_4_validator: Optional[Ag11] = None
    # data type: Ag21
    oneof_schema_5_validator: Optional[Ag21] = None
    # data type: Ag31
    oneof_schema_6_validator: Optional[Ag31] = None
    # data type: Ap01
    oneof_schema_7_validator: Optional[Ap01] = None
    # data type: Av01
    oneof_schema_8_validator: Optional[Av01] = None
    # data type: Cb01
    oneof_schema_9_validator: Optional[Cb01] = None
    # data type: Ct01
    oneof_schema_10_validator: Optional[Ct01] = None
    # data type: Cw01
    oneof_schema_11_validator: Optional[Cw01] = None
    # data type: Dt01
    oneof_schema_12_validator: Optional[Dt01] = None
    # data type: Dw01
    oneof_schema_13_validator: Optional[Dw01] = None
    # data type: Gv01
    oneof_schema_14_validator: Optional[Gv01] = None
    # data type: Gv02
    oneof_schema_15_validator: Optional[Gv02] = None
    # data type: Ha01
    oneof_schema_16_validator: Optional[Ha01] = None
    # data type: Hf01
    oneof_schema_17_validator: Optional[Hf01] = None
    # data type: Hq01
    oneof_schema_18_validator: Optional[Hq01] = None
    # data type: Ib01
    oneof_schema_19_validator: Optional[Ib01] = None
    # data type: If01
    oneof_schema_20_validator: Optional[If01] = None
    # data type: If21
    oneof_schema_21_validator: Optional[If21] = None
    # data type: If31
    oneof_schema_22_validator: Optional[If31] = None
    # data type: If41
    oneof_schema_23_validator: Optional[If41] = None
    # data type: Ii01
    oneof_schema_24_validator: Optional[Ii01] = None
    # data type: Iv01
    oneof_schema_25_validator: Optional[Iv01] = None
    # data type: Iv11
    oneof_schema_26_validator: Optional[Iv11] = None
    # data type: Iv21
    oneof_schema_27_validator: Optional[Iv21] = None
    # data type: Jb01
    oneof_schema_28_validator: Optional[Jb01] = None
    # data type: Jf01
    oneof_schema_29_validator: Optional[Jf01] = None
    # data type: Jf21
    oneof_schema_30_validator: Optional[Jf21] = None
    # data type: Jf31
    oneof_schema_31_validator: Optional[Jf31] = None
    # data type: Ji01
    oneof_schema_32_validator: Optional[Ji01] = None
    # data type: Jv01
    oneof_schema_33_validator: Optional[Jv01] = None
    # data type: La01
    oneof_schema_34_validator: Optional[La01] = None
    # data type: Lf01
    oneof_schema_35_validator: Optional[Lf01] = None
    # data type: Lg01
    oneof_schema_36_validator: Optional[Lg01] = None
    # data type: Lq01
    oneof_schema_37_validator: Optional[Lq01] = None
    # data type: Ng01
    oneof_schema_38_validator: Optional[Ng01] = None
    # data type: Null
    oneof_schema_39_validator: Optional[Null] = None
    # data type: Of11
    oneof_schema_40_validator: Optional[Of11] = None
    # data type: Og11
    oneof_schema_41_validator: Optional[Og11] = None
    # data type: Pf01
    oneof_schema_42_validator: Optional[Pf01] = None
    # data type: Pf02
    oneof_schema_43_validator: Optional[Pf02] = None
    # data type: Pf03
    oneof_schema_44_validator: Optional[Pf03] = None
    # data type: Rb01
    oneof_schema_45_validator: Optional[Rb01] = None
    # data type: Rf01
    oneof_schema_46_validator: Optional[Rf01] = None
    # data type: Rf31
    oneof_schema_47_validator: Optional[Rf31] = None
    # data type: Rv01
    oneof_schema_48_validator: Optional[Rv01] = None
    # data type: Sv01
    oneof_schema_49_validator: Optional[Sv01] = None
    # data type: Sv11
    oneof_schema_50_validator: Optional[Sv11] = None
    # data type: Tb01
    oneof_schema_51_validator: Optional[Tb01] = None
    # data type: Tb02
    oneof_schema_52_validator: Optional[Tb02] = None
    # data type: Tf01
    oneof_schema_53_validator: Optional[Tf01] = None
    # data type: Tf11
    oneof_schema_54_validator: Optional[Tf11] = None
    # data type: Tf21
    oneof_schema_55_validator: Optional[Tf21] = None
    # data type: Tv01
    oneof_schema_56_validator: Optional[Tv01] = None
    # data type: Vb01
    oneof_schema_57_validator: Optional[Vb01] = None
    # data type: Vb02
    oneof_schema_58_validator: Optional[Vb02] = None
    # data type: Wa01
    oneof_schema_59_validator: Optional[Wa01] = None
    # data type: Wa11
    oneof_schema_60_validator: Optional[Wa11] = None
    # data type: Wf01
    oneof_schema_61_validator: Optional[Wf01] = None
    # data type: Xa01
    oneof_schema_62_validator: Optional[Xa01] = None
    # data type: Xf01
    oneof_schema_63_validator: Optional[Xf01] = None
    # data type: Xq01
    oneof_schema_64_validator: Optional[Xq01] = None
    actual_instance: Optional[Union[Af01, Af11, Ag01, Ag11, Ag21, Ag31, Ap01, Av01, Cb01, Ct01, Cw01, Dt01, Dw01, Gv01, Gv02, Ha01, Hf01, Hq01, Ib01, If01, If21, If31, If41, Ii01, Iv01, Iv11, Iv21, Jb01, Jf01, Jf21, Jf31, Ji01, Jv01, La01, Lf01, Lg01, Lq01, Ng01, Null, Of11, Og11, Pf01, Pf02, Pf03, Rb01, Rf01, Rf31, Rv01, Sv01, Sv11, Tb01, Tb02, Tf01, Tf11, Tf21, Tv01, Vb01, Vb02, Wa01, Wa11, Wf01, Xa01, Xf01, Xq01]] = None
    one_of_schemas: Set[str] = { "Af01", "Af11", "Ag01", "Ag11", "Ag21", "Ag31", "Ap01", "Av01", "Cb01", "Ct01", "Cw01", "Dt01", "Dw01", "Gv01", "Gv02", "Ha01", "Hf01", "Hq01", "Ib01", "If01", "If21", "If31", "If41", "Ii01", "Iv01", "Iv11", "Iv21", "Jb01", "Jf01", "Jf21", "Jf31", "Ji01", "Jv01", "La01", "Lf01", "Lg01", "Lq01", "Ng01", "Null", "Of11", "Og11", "Pf01", "Pf02", "Pf03", "Rb01", "Rf01", "Rf31", "Rv01", "Sv01", "Sv11", "Tb01", "Tb02", "Tf01", "Tf11", "Tf21", "Tv01", "Vb01", "Vb02", "Wa01", "Wa11", "Wf01", "Xa01", "Xf01", "Xq01" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = LoBericht.model_construct()
        error_messages = []
        match = 0
        # validate data type: Af01
        if not isinstance(v, Af01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Af01`")
        else:
            match += 1
        # validate data type: Af11
        if not isinstance(v, Af11):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Af11`")
        else:
            match += 1
        # validate data type: Ag01
        if not isinstance(v, Ag01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ag01`")
        else:
            match += 1
        # validate data type: Ag11
        if not isinstance(v, Ag11):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ag11`")
        else:
            match += 1
        # validate data type: Ag21
        if not isinstance(v, Ag21):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ag21`")
        else:
            match += 1
        # validate data type: Ag31
        if not isinstance(v, Ag31):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ag31`")
        else:
            match += 1
        # validate data type: Ap01
        if not isinstance(v, Ap01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ap01`")
        else:
            match += 1
        # validate data type: Av01
        if not isinstance(v, Av01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Av01`")
        else:
            match += 1
        # validate data type: Cb01
        if not isinstance(v, Cb01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Cb01`")
        else:
            match += 1
        # validate data type: Ct01
        if not isinstance(v, Ct01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ct01`")
        else:
            match += 1
        # validate data type: Cw01
        if not isinstance(v, Cw01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Cw01`")
        else:
            match += 1
        # validate data type: Dt01
        if not isinstance(v, Dt01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Dt01`")
        else:
            match += 1
        # validate data type: Dw01
        if not isinstance(v, Dw01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Dw01`")
        else:
            match += 1
        # validate data type: Gv01
        if not isinstance(v, Gv01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Gv01`")
        else:
            match += 1
        # validate data type: Gv02
        if not isinstance(v, Gv02):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Gv02`")
        else:
            match += 1
        # validate data type: Ha01
        if not isinstance(v, Ha01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ha01`")
        else:
            match += 1
        # validate data type: Hf01
        if not isinstance(v, Hf01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Hf01`")
        else:
            match += 1
        # validate data type: Hq01
        if not isinstance(v, Hq01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Hq01`")
        else:
            match += 1
        # validate data type: Ib01
        if not isinstance(v, Ib01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ib01`")
        else:
            match += 1
        # validate data type: If01
        if not isinstance(v, If01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `If01`")
        else:
            match += 1
        # validate data type: If21
        if not isinstance(v, If21):
            error_messages.append(f"Error! Input type `{type(v)}` is not `If21`")
        else:
            match += 1
        # validate data type: If31
        if not isinstance(v, If31):
            error_messages.append(f"Error! Input type `{type(v)}` is not `If31`")
        else:
            match += 1
        # validate data type: If41
        if not isinstance(v, If41):
            error_messages.append(f"Error! Input type `{type(v)}` is not `If41`")
        else:
            match += 1
        # validate data type: Ii01
        if not isinstance(v, Ii01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ii01`")
        else:
            match += 1
        # validate data type: Iv01
        if not isinstance(v, Iv01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Iv01`")
        else:
            match += 1
        # validate data type: Iv11
        if not isinstance(v, Iv11):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Iv11`")
        else:
            match += 1
        # validate data type: Iv21
        if not isinstance(v, Iv21):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Iv21`")
        else:
            match += 1
        # validate data type: Jb01
        if not isinstance(v, Jb01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Jb01`")
        else:
            match += 1
        # validate data type: Jf01
        if not isinstance(v, Jf01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Jf01`")
        else:
            match += 1
        # validate data type: Jf21
        if not isinstance(v, Jf21):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Jf21`")
        else:
            match += 1
        # validate data type: Jf31
        if not isinstance(v, Jf31):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Jf31`")
        else:
            match += 1
        # validate data type: Ji01
        if not isinstance(v, Ji01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ji01`")
        else:
            match += 1
        # validate data type: Jv01
        if not isinstance(v, Jv01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Jv01`")
        else:
            match += 1
        # validate data type: La01
        if not isinstance(v, La01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `La01`")
        else:
            match += 1
        # validate data type: Lf01
        if not isinstance(v, Lf01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Lf01`")
        else:
            match += 1
        # validate data type: Lg01
        if not isinstance(v, Lg01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Lg01`")
        else:
            match += 1
        # validate data type: Lq01
        if not isinstance(v, Lq01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Lq01`")
        else:
            match += 1
        # validate data type: Ng01
        if not isinstance(v, Ng01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Ng01`")
        else:
            match += 1
        # validate data type: Null
        if not isinstance(v, Null):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Null`")
        else:
            match += 1
        # validate data type: Of11
        if not isinstance(v, Of11):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Of11`")
        else:
            match += 1
        # validate data type: Og11
        if not isinstance(v, Og11):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Og11`")
        else:
            match += 1
        # validate data type: Pf01
        if not isinstance(v, Pf01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Pf01`")
        else:
            match += 1
        # validate data type: Pf02
        if not isinstance(v, Pf02):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Pf02`")
        else:
            match += 1
        # validate data type: Pf03
        if not isinstance(v, Pf03):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Pf03`")
        else:
            match += 1
        # validate data type: Rb01
        if not isinstance(v, Rb01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Rb01`")
        else:
            match += 1
        # validate data type: Rf01
        if not isinstance(v, Rf01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Rf01`")
        else:
            match += 1
        # validate data type: Rf31
        if not isinstance(v, Rf31):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Rf31`")
        else:
            match += 1
        # validate data type: Rv01
        if not isinstance(v, Rv01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Rv01`")
        else:
            match += 1
        # validate data type: Sv01
        if not isinstance(v, Sv01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Sv01`")
        else:
            match += 1
        # validate data type: Sv11
        if not isinstance(v, Sv11):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Sv11`")
        else:
            match += 1
        # validate data type: Tb01
        if not isinstance(v, Tb01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Tb01`")
        else:
            match += 1
        # validate data type: Tb02
        if not isinstance(v, Tb02):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Tb02`")
        else:
            match += 1
        # validate data type: Tf01
        if not isinstance(v, Tf01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Tf01`")
        else:
            match += 1
        # validate data type: Tf11
        if not isinstance(v, Tf11):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Tf11`")
        else:
            match += 1
        # validate data type: Tf21
        if not isinstance(v, Tf21):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Tf21`")
        else:
            match += 1
        # validate data type: Tv01
        if not isinstance(v, Tv01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Tv01`")
        else:
            match += 1
        # validate data type: Vb01
        if not isinstance(v, Vb01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Vb01`")
        else:
            match += 1
        # validate data type: Vb02
        if not isinstance(v, Vb02):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Vb02`")
        else:
            match += 1
        # validate data type: Wa01
        if not isinstance(v, Wa01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Wa01`")
        else:
            match += 1
        # validate data type: Wa11
        if not isinstance(v, Wa11):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Wa11`")
        else:
            match += 1
        # validate data type: Wf01
        if not isinstance(v, Wf01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Wf01`")
        else:
            match += 1
        # validate data type: Xa01
        if not isinstance(v, Xa01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Xa01`")
        else:
            match += 1
        # validate data type: Xf01
        if not isinstance(v, Xf01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Xf01`")
        else:
            match += 1
        # validate data type: Xq01
        if not isinstance(v, Xq01):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Xq01`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in LoBericht with oneOf schemas: Af01, Af11, Ag01, Ag11, Ag21, Ag31, Ap01, Av01, Cb01, Ct01, Cw01, Dt01, Dw01, Gv01, Gv02, Ha01, Hf01, Hq01, Ib01, If01, If21, If31, If41, Ii01, Iv01, Iv11, Iv21, Jb01, Jf01, Jf21, Jf31, Ji01, Jv01, La01, Lf01, Lg01, Lq01, Ng01, Null, Of11, Og11, Pf01, Pf02, Pf03, Rb01, Rf01, Rf31, Rv01, Sv01, Sv11, Tb01, Tb02, Tf01, Tf11, Tf21, Tv01, Vb01, Vb02, Wa01, Wa11, Wf01, Xa01, Xf01, Xq01. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in LoBericht with oneOf schemas: Af01, Af11, Ag01, Ag11, Ag21, Ag31, Ap01, Av01, Cb01, Ct01, Cw01, Dt01, Dw01, Gv01, Gv02, Ha01, Hf01, Hq01, Ib01, If01, If21, If31, If41, Ii01, Iv01, Iv11, Iv21, Jb01, Jf01, Jf21, Jf31, Ji01, Jv01, La01, Lf01, Lg01, Lq01, Ng01, Null, Of11, Og11, Pf01, Pf02, Pf03, Rb01, Rf01, Rf31, Rv01, Sv01, Sv11, Tb01, Tb02, Tf01, Tf11, Tf21, Tv01, Vb01, Vb02, Wa01, Wa11, Wf01, Xa01, Xf01, Xq01. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("berichtType")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `berichtType` in the input.")

        # check if data type is `Af01`
        if _data_type == "Af01":
            instance.actual_instance = Af01.from_json(json_str)
            return instance

        # check if data type is `Af11`
        if _data_type == "Af11":
            instance.actual_instance = Af11.from_json(json_str)
            return instance

        # check if data type is `Ag01`
        if _data_type == "Ag01":
            instance.actual_instance = Ag01.from_json(json_str)
            return instance

        # check if data type is `Ag11`
        if _data_type == "Ag11":
            instance.actual_instance = Ag11.from_json(json_str)
            return instance

        # check if data type is `Ag21`
        if _data_type == "Ag21":
            instance.actual_instance = Ag21.from_json(json_str)
            return instance

        # check if data type is `Ag31`
        if _data_type == "Ag31":
            instance.actual_instance = Ag31.from_json(json_str)
            return instance

        # check if data type is `Ap01`
        if _data_type == "Ap01":
            instance.actual_instance = Ap01.from_json(json_str)
            return instance

        # check if data type is `Av01`
        if _data_type == "Av01":
            instance.actual_instance = Av01.from_json(json_str)
            return instance

        # check if data type is `Cb01`
        if _data_type == "Cb01":
            instance.actual_instance = Cb01.from_json(json_str)
            return instance

        # check if data type is `Ct01`
        if _data_type == "Ct01":
            instance.actual_instance = Ct01.from_json(json_str)
            return instance

        # check if data type is `Cw01`
        if _data_type == "Cw01":
            instance.actual_instance = Cw01.from_json(json_str)
            return instance

        # check if data type is `Dt01`
        if _data_type == "Dt01":
            instance.actual_instance = Dt01.from_json(json_str)
            return instance

        # check if data type is `Dw01`
        if _data_type == "Dw01":
            instance.actual_instance = Dw01.from_json(json_str)
            return instance

        # check if data type is `Gv01`
        if _data_type == "Gv01":
            instance.actual_instance = Gv01.from_json(json_str)
            return instance

        # check if data type is `Gv02`
        if _data_type == "Gv02":
            instance.actual_instance = Gv02.from_json(json_str)
            return instance

        # check if data type is `Ha01`
        if _data_type == "Ha01":
            instance.actual_instance = Ha01.from_json(json_str)
            return instance

        # check if data type is `Hf01`
        if _data_type == "Hf01":
            instance.actual_instance = Hf01.from_json(json_str)
            return instance

        # check if data type is `Hq01`
        if _data_type == "Hq01":
            instance.actual_instance = Hq01.from_json(json_str)
            return instance

        # check if data type is `Ib01`
        if _data_type == "Ib01":
            instance.actual_instance = Ib01.from_json(json_str)
            return instance

        # check if data type is `If01`
        if _data_type == "If01":
            instance.actual_instance = If01.from_json(json_str)
            return instance

        # check if data type is `If21`
        if _data_type == "If21":
            instance.actual_instance = If21.from_json(json_str)
            return instance

        # check if data type is `If31`
        if _data_type == "If31":
            instance.actual_instance = If31.from_json(json_str)
            return instance

        # check if data type is `If41`
        if _data_type == "If41":
            instance.actual_instance = If41.from_json(json_str)
            return instance

        # check if data type is `Ii01`
        if _data_type == "Ii01":
            instance.actual_instance = Ii01.from_json(json_str)
            return instance

        # check if data type is `Iv01`
        if _data_type == "Iv01":
            instance.actual_instance = Iv01.from_json(json_str)
            return instance

        # check if data type is `Iv11`
        if _data_type == "Iv11":
            instance.actual_instance = Iv11.from_json(json_str)
            return instance

        # check if data type is `Iv21`
        if _data_type == "Iv21":
            instance.actual_instance = Iv21.from_json(json_str)
            return instance

        # check if data type is `Jb01`
        if _data_type == "Jb01":
            instance.actual_instance = Jb01.from_json(json_str)
            return instance

        # check if data type is `Jf01`
        if _data_type == "Jf01":
            instance.actual_instance = Jf01.from_json(json_str)
            return instance

        # check if data type is `Jf21`
        if _data_type == "Jf21":
            instance.actual_instance = Jf21.from_json(json_str)
            return instance

        # check if data type is `Jf31`
        if _data_type == "Jf31":
            instance.actual_instance = Jf31.from_json(json_str)
            return instance

        # check if data type is `Ji01`
        if _data_type == "Ji01":
            instance.actual_instance = Ji01.from_json(json_str)
            return instance

        # check if data type is `Jv01`
        if _data_type == "Jv01":
            instance.actual_instance = Jv01.from_json(json_str)
            return instance

        # check if data type is `La01`
        if _data_type == "La01":
            instance.actual_instance = La01.from_json(json_str)
            return instance

        # check if data type is `Lf01`
        if _data_type == "Lf01":
            instance.actual_instance = Lf01.from_json(json_str)
            return instance

        # check if data type is `Lg01`
        if _data_type == "Lg01":
            instance.actual_instance = Lg01.from_json(json_str)
            return instance

        # check if data type is `Lq01`
        if _data_type == "Lq01":
            instance.actual_instance = Lq01.from_json(json_str)
            return instance

        # check if data type is `Ng01`
        if _data_type == "Ng01":
            instance.actual_instance = Ng01.from_json(json_str)
            return instance

        # check if data type is `Null`
        if _data_type == "Null":
            instance.actual_instance = Null.from_json(json_str)
            return instance

        # check if data type is `Of11`
        if _data_type == "Of11":
            instance.actual_instance = Of11.from_json(json_str)
            return instance

        # check if data type is `Og11`
        if _data_type == "Og11":
            instance.actual_instance = Og11.from_json(json_str)
            return instance

        # check if data type is `Pf01`
        if _data_type == "Pf01":
            instance.actual_instance = Pf01.from_json(json_str)
            return instance

        # check if data type is `Pf02`
        if _data_type == "Pf02":
            instance.actual_instance = Pf02.from_json(json_str)
            return instance

        # check if data type is `Pf03`
        if _data_type == "Pf03":
            instance.actual_instance = Pf03.from_json(json_str)
            return instance

        # check if data type is `Rb01`
        if _data_type == "Rb01":
            instance.actual_instance = Rb01.from_json(json_str)
            return instance

        # check if data type is `Rf01`
        if _data_type == "Rf01":
            instance.actual_instance = Rf01.from_json(json_str)
            return instance

        # check if data type is `Rf31`
        if _data_type == "Rf31":
            instance.actual_instance = Rf31.from_json(json_str)
            return instance

        # check if data type is `Rv01`
        if _data_type == "Rv01":
            instance.actual_instance = Rv01.from_json(json_str)
            return instance

        # check if data type is `Sv01`
        if _data_type == "Sv01":
            instance.actual_instance = Sv01.from_json(json_str)
            return instance

        # check if data type is `Sv11`
        if _data_type == "Sv11":
            instance.actual_instance = Sv11.from_json(json_str)
            return instance

        # check if data type is `Tb01`
        if _data_type == "Tb01":
            instance.actual_instance = Tb01.from_json(json_str)
            return instance

        # check if data type is `Tb02`
        if _data_type == "Tb02":
            instance.actual_instance = Tb02.from_json(json_str)
            return instance

        # check if data type is `Tf01`
        if _data_type == "Tf01":
            instance.actual_instance = Tf01.from_json(json_str)
            return instance

        # check if data type is `Tf11`
        if _data_type == "Tf11":
            instance.actual_instance = Tf11.from_json(json_str)
            return instance

        # check if data type is `Tf21`
        if _data_type == "Tf21":
            instance.actual_instance = Tf21.from_json(json_str)
            return instance

        # check if data type is `Tv01`
        if _data_type == "Tv01":
            instance.actual_instance = Tv01.from_json(json_str)
            return instance

        # check if data type is `Vb01`
        if _data_type == "Vb01":
            instance.actual_instance = Vb01.from_json(json_str)
            return instance

        # check if data type is `Vb02`
        if _data_type == "Vb02":
            instance.actual_instance = Vb02.from_json(json_str)
            return instance

        # check if data type is `Wa01`
        if _data_type == "Wa01":
            instance.actual_instance = Wa01.from_json(json_str)
            return instance

        # check if data type is `Wa11`
        if _data_type == "Wa11":
            instance.actual_instance = Wa11.from_json(json_str)
            return instance

        # check if data type is `Wf01`
        if _data_type == "Wf01":
            instance.actual_instance = Wf01.from_json(json_str)
            return instance

        # check if data type is `Xa01`
        if _data_type == "Xa01":
            instance.actual_instance = Xa01.from_json(json_str)
            return instance

        # check if data type is `Xf01`
        if _data_type == "Xf01":
            instance.actual_instance = Xf01.from_json(json_str)
            return instance

        # check if data type is `Xq01`
        if _data_type == "Xq01":
            instance.actual_instance = Xq01.from_json(json_str)
            return instance

        # deserialize data into Af01
        try:
            instance.actual_instance = Af01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Af11
        try:
            instance.actual_instance = Af11.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ag01
        try:
            instance.actual_instance = Ag01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ag11
        try:
            instance.actual_instance = Ag11.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ag21
        try:
            instance.actual_instance = Ag21.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ag31
        try:
            instance.actual_instance = Ag31.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ap01
        try:
            instance.actual_instance = Ap01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Av01
        try:
            instance.actual_instance = Av01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Cb01
        try:
            instance.actual_instance = Cb01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ct01
        try:
            instance.actual_instance = Ct01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Cw01
        try:
            instance.actual_instance = Cw01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Dt01
        try:
            instance.actual_instance = Dt01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Dw01
        try:
            instance.actual_instance = Dw01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Gv01
        try:
            instance.actual_instance = Gv01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Gv02
        try:
            instance.actual_instance = Gv02.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ha01
        try:
            instance.actual_instance = Ha01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Hf01
        try:
            instance.actual_instance = Hf01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Hq01
        try:
            instance.actual_instance = Hq01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ib01
        try:
            instance.actual_instance = Ib01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into If01
        try:
            instance.actual_instance = If01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into If21
        try:
            instance.actual_instance = If21.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into If31
        try:
            instance.actual_instance = If31.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into If41
        try:
            instance.actual_instance = If41.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ii01
        try:
            instance.actual_instance = Ii01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Iv01
        try:
            instance.actual_instance = Iv01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Iv11
        try:
            instance.actual_instance = Iv11.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Iv21
        try:
            instance.actual_instance = Iv21.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Jb01
        try:
            instance.actual_instance = Jb01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Jf01
        try:
            instance.actual_instance = Jf01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Jf21
        try:
            instance.actual_instance = Jf21.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Jf31
        try:
            instance.actual_instance = Jf31.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ji01
        try:
            instance.actual_instance = Ji01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Jv01
        try:
            instance.actual_instance = Jv01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into La01
        try:
            instance.actual_instance = La01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Lf01
        try:
            instance.actual_instance = Lf01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Lg01
        try:
            instance.actual_instance = Lg01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Lq01
        try:
            instance.actual_instance = Lq01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Ng01
        try:
            instance.actual_instance = Ng01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Null
        try:
            instance.actual_instance = Null.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Of11
        try:
            instance.actual_instance = Of11.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Og11
        try:
            instance.actual_instance = Og11.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Pf01
        try:
            instance.actual_instance = Pf01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Pf02
        try:
            instance.actual_instance = Pf02.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Pf03
        try:
            instance.actual_instance = Pf03.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Rb01
        try:
            instance.actual_instance = Rb01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Rf01
        try:
            instance.actual_instance = Rf01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Rf31
        try:
            instance.actual_instance = Rf31.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Rv01
        try:
            instance.actual_instance = Rv01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Sv01
        try:
            instance.actual_instance = Sv01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Sv11
        try:
            instance.actual_instance = Sv11.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Tb01
        try:
            instance.actual_instance = Tb01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Tb02
        try:
            instance.actual_instance = Tb02.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Tf01
        try:
            instance.actual_instance = Tf01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Tf11
        try:
            instance.actual_instance = Tf11.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Tf21
        try:
            instance.actual_instance = Tf21.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Tv01
        try:
            instance.actual_instance = Tv01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Vb01
        try:
            instance.actual_instance = Vb01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Vb02
        try:
            instance.actual_instance = Vb02.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Wa01
        try:
            instance.actual_instance = Wa01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Wa11
        try:
            instance.actual_instance = Wa11.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Wf01
        try:
            instance.actual_instance = Wf01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Xa01
        try:
            instance.actual_instance = Xa01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Xf01
        try:
            instance.actual_instance = Xf01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Xq01
        try:
            instance.actual_instance = Xq01.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into LoBericht with oneOf schemas: Af01, Af11, Ag01, Ag11, Ag21, Ag31, Ap01, Av01, Cb01, Ct01, Cw01, Dt01, Dw01, Gv01, Gv02, Ha01, Hf01, Hq01, Ib01, If01, If21, If31, If41, Ii01, Iv01, Iv11, Iv21, Jb01, Jf01, Jf21, Jf31, Ji01, Jv01, La01, Lf01, Lg01, Lq01, Ng01, Null, Of11, Og11, Pf01, Pf02, Pf03, Rb01, Rf01, Rf31, Rv01, Sv01, Sv11, Tb01, Tb02, Tf01, Tf11, Tf21, Tv01, Vb01, Vb02, Wa01, Wa11, Wf01, Xa01, Xf01, Xq01. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into LoBericht with oneOf schemas: Af01, Af11, Ag01, Ag11, Ag21, Ag31, Ap01, Av01, Cb01, Ct01, Cw01, Dt01, Dw01, Gv01, Gv02, Ha01, Hf01, Hq01, Ib01, If01, If21, If31, If41, Ii01, Iv01, Iv11, Iv21, Jb01, Jf01, Jf21, Jf31, Ji01, Jv01, La01, Lf01, Lg01, Lq01, Ng01, Null, Of11, Og11, Pf01, Pf02, Pf03, Rb01, Rf01, Rf31, Rv01, Sv01, Sv11, Tb01, Tb02, Tf01, Tf11, Tf21, Tv01, Vb01, Vb02, Wa01, Wa11, Wf01, Xa01, Xf01, Xq01. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], Af01, Af11, Ag01, Ag11, Ag21, Ag31, Ap01, Av01, Cb01, Ct01, Cw01, Dt01, Dw01, Gv01, Gv02, Ha01, Hf01, Hq01, Ib01, If01, If21, If31, If41, Ii01, Iv01, Iv11, Iv21, Jb01, Jf01, Jf21, Jf31, Ji01, Jv01, La01, Lf01, Lg01, Lq01, Ng01, Null, Of11, Og11, Pf01, Pf02, Pf03, Rb01, Rf01, Rf31, Rv01, Sv01, Sv11, Tb01, Tb02, Tf01, Tf11, Tf21, Tv01, Vb01, Vb02, Wa01, Wa11, Wf01, Xa01, Xf01, Xq01]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


