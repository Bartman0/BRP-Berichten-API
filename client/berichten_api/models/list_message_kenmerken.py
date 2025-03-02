# coding: utf-8

"""
    BRP Berichten API

    Een REST API voor het a-synchroon uitwisselen van berichten welke in het Logisch Ontwerp gedefinieerd zijn.  # Wijzigingshistorie:  ## 0.6.2 Januari 2025 - OAuth endpoint demo omgeving gecorrigeerd.  ## 0.6.1 Januari 2025 - Ping endpoints zijn niet langer bereikbaar zonder eerst te authenticeren.  ## 0.6.0 Januari 2025 - Servers toegevoegd.   - Hiervoor moesten de paden van de endpoints aangepast worden. Hierdoor is '/api/v1' komen te vervallen bij de endpoints. Dit is verhuist naar de base-url's van de genoemde servers. - Authenticatie details toegevoegd. - Foutmeldingen bij het conversie endpoint bijgewerkt. - Alle namespace paden van de foutmeldingen nagelopen en gecorrigeerd daar waar nodig. Dit zodat ze consistent starten met: \"https://www.rvig.nl/brp/berichten-api/probleem/\".  ## 0.5.5 November 2024 - 'berichtVolgnummer' en 'afzender' required gemaakt in ListMessageKenmerken (en daardoor ook in GetMessageKenmerken). - De GET en DELETE foutsituaties zijn voorzien van discriminators ten behoeve van het onderscheiden van foutsituatie subtypes door de gegenereerde client.  ## 0.5.4 November 2024 - Properties van PagineringResultaat en PagineerbaarResultaat welke altijd aanwezig zullen zijn bij een list-request required gemaakt. - Required properties van put-message-antwoord gecorrigeerd. - Schema van het Null bericht gecorrigeerd.  ## 0.5.3 November 2024 - Het Sv11 bericht is qua schema aangepast aangezien deze onterecht de property plData bevatte. Deze property is verwijderd uit dit bericht. - Foutsituaties zijn voorzien van discriminators ten behoeve van het onderscheiden van foutsituatie subtypes door de gegenereerde client.  ## 0.5.2 Oktober 2024 - De request die volledig afgekeurd worden en een statuscode 4xx of 5xx retourneren, doen dit nu met de response header 'Content-Type: application/problem+json'. - Requests die een 2xx response in JSON formaat retourneren, doen dit met \"Content-Type: application/json\" ipv \"Content-Type: application/json: charset=utf-8\". Conform rfc8259 (https://www.rfc-editor.org/rfc/rfc8259) is JSON altijd in UTF-8 formaat en heeft dit type geen charset parameter.  ## 0.5.1 Oktober 2024  - De fout BBA-PUT-F002 is aangepast naar een algemene fout voor onjuiste velden in een PutMessage, via het veld \"invalidParams\" in de response word aangegeven welke velden onjuist zijn en waarom.  ## 0.5.0 September 2024  - Het veld berichtId en verwijzingBerichtId zijn omgezet van type 'integer' naar type 'string' om beter aan te sluiten op de bestaande voorziening.  - Het probleem-antwoord response object is overal vervangen met de algemene Foutmelding response welke zich conformeert aan RFC7807.  - De velden 'foutTitel', 'foutType', 'foutDetail' zijn aangepast naar 'title, 'type', 'detail' zodat zij zich conformeren aan de RFC7807.  - De afhankelijkheid op 'openapi-problem-detail-v1.yml' is komen te vervallen (https://github.com/rvig-brp/BRP-Berichten-API/issues/3).  ## 0.4.1 Juli 2024  - Het json-schema voor de autorisatieberichten Ct01, Cw01 en Cb01 is toegevoegd.  - De ontvanger is opgenomen in de response bij het verzenden van een bericht. Dit is met name relevant wanneer er een bericht naar een berichtgroep gestuurd wordt. In dat geval weet de verzender wie de uiteindelijke ontvangers zijn. Bij het versturen van een bericht naar de een regulier account zal dit nummer 1:1 overeenkomen met de ontvanger die bij het te verzenden bericht is opgegeven.  ## 0.4.0 Juni 2024 - De json-schema's van de berichtsoorten zijn opgenomen in de OpenAPI Specificatie. Voor elke berichtsoort die het LO beschrijft, is opgenomen hoe dit bericht gestructureerd is.   - Houdt er rekening mee dat het weergeven van de OpenAPI specificatie in de web-versie va SwaggerUI hierdoor trager geworden is. Het is aan te raden om de alternatieve (redocly) weergave te gebruiken:     - https://brp-berichten-api.dictua.ictu-sr.nl/openapi/berichten-api.html     - De JSON schema's zijn tevens te vinden op onze Github pagina. - De JSON-response van het conversie endpoint is iets aangepast zodat naast het geconverteerde bericht tevens validatiefouten opgenomen kunnen worden.  ## 0.3.0 - Mei 2024 - Conversie endpoints   - Introductie bericht-conversie (/berichten/conversie) endpoint. Houdt er rekening mee dat de conversie naar JSON opgenomen is, maar nog niet geïmplementeerd is in de demo omgeving. - Het limiet van het aantal berichten dat verwijderd kan worden is gelijkgesteld aan dat wat gelijktijdig opgehaald kan worden (100). - De API is hernoemd van \"BRP A-Synchrone berichten API\" naar \"BRP berichten API\".   - Nieuwe URL's demo omgeving:     - https://brp-berichten-api.dictua.ictu-sr.nl/api/v1/berichten     - https://brp-berichten-api.dictua.ictu-sr.nl/openapi/berichten-api.html     - https://brp-berichten-api.dictua.ictu-sr.nl/swagger-ui/index.html - Beschikbaarheid endpoint(s)   - Er is een tweede ping endpoint bijgekomen waardoor en nu een HEAD of een GET gedaan kan worden. De response blijft hetzelfde. U kunt zelf kiezen welke van deze twee u hanteert.   - De noodzaak voor authenticatie op het `ping` endpoint is komen te vervallen. U kunt dus zonder noodzaak van authenticatie vaststellen of de dienst beschikbaar is.  ## 0.2.2 - April 2024 - Ping operatie toegevoegd t.b.v. het verifiëren dat er communicatie met de berichtendienst mogelijks is. - De standaard sortering bij een LIST operatie is op dit moment:   1. `Datum + tijdstip van ontvangst` waarbij geldt dat het oudste bericht als eerste wordt weergegeven in de lijst met beschikbare berichten (rationale deze dient als eerste verwerkt worden door de ontvanger).   2. Indien `datum + tijdstip van ontvangst` gelijk zijn (wat kan voorkomen aangezien er meerdere berichten tegelijk ingestuurd kunnen worden), dan worden `afzender` en het `messageId` meegenomen in de sortering. De volgorde die de afzender toegekend heen via de messageId is op dat moment dus bepalend.  ## 0.2.1 - April 2024 - Mogelijkheden tot sortering bij een list operatie zijn verwijderd. De standaard sortering wordt nog bepaald. - Demo omgeving is toegevoegd aan de lijst met servers.   - API te benaderen via https://brp-berichten-api.dictua.ictu-sr.nl/api/v1/berichten   - Swagger UI via: https://brp-berichten-api.dictua.ictu-sr.nl/swagger-ui/index.html   - De OpenAPI specificatie via: https://brp-berichten-api.dictua.ictu-sr.nl/openapi.brp-berichten-api-v1.yaml - Wachtwoord wijzigingen optie is verwijderd. - Het `berichtFormaat` attribuut is komen te vervallen. Alle berichten zijn nu per definitie in JSON formaat. De eis om de berichtInhoud Base64 te   encoderen komt daarmee te vervallen. - Voorbeelddata verbeterd. - Tellingen endpoint toegevoegd welke invulling geeft aan de mailbox Summarize tegenhanger. - Delete endpoint gecorrigeerd. De collectie `succesvolVerwijderdeBerichten` was van het type string i.p.v. berichtTransportId. - Limieten zijn gewijzigd:   - Het aantal berichten dat via een PUT verstuurd kan worden is verhoogd naar 25. Uitgaande van een gemiddelde berichtgrootte van 40kb geeft dat een request van 1MB groot.   - Het aantal berichten dat via een LIST opgevraagd kan worden is vergroot naar 2000. Daarbij krijgt u de mogelijkheid om dit aantal te beperken.     - 2000 berichten in een LIST operatie komt neer op ongeveer 600KB response grootte.   - Het aantal berichten dat via een GET ontvangen kan worden is verhoogd naar 100. Dit heeft te maken met de gangbare (veilige) restricties van een URL qua lengte (2KB).     - Voor de URL worden 256 bytes gereserveerd.       - Voor de UUID blijven dan 1.792 bytes over.     - Een BerichtTransportId is 17 bytes groot (UUID + separatie-karakter ',')       - Uitgaande van 17 bytes, zou dit 105 keer herhaald kunnen worden. Om aan de veilige kan te zitten en om op een mooi rond getal uit te komen kiezen wij voor 100 als limiet.     - Uitgaande van een gemiddelde berichtgrootte van 40KB komt je met 100 berichten uit op 4MB qua response-grootte. - \"aantalKeerOpgehaald\" en \"dtLaatstOpgehaald\" zijn verwijderd uit response van LIST (ListMessageKenmerken schema). Wij zien hierin geen meerwaarde voor de aansluitende partijen. Wel kunt u blijven zien OF het bericht is opgehaald (boolean waarde).  ## 0.2.0 - April 2024 - \"List\" verzoek is verhuisd van \"/berichten/lijst\" --> \"/berichten\" - \"GET\" van meerdere berichten wordt gedaan middels path-parameters i.p.v. query-parameters en is samengevoegd met het endpoint voor het ophalen van een enkel bericht.<br/>   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID])   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID]) - \"DELETE\" van meerdere berichten wordt gedaan middels path-parameters i.p.v. query-parameters en is samengevoegd met het endpoint voor het verwijderen van een enkel bericht.<br/>   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID]) - Het \"berichtId\" wat correspondeert met het \"MessageId\" veld van de mailboxserver is qua type gewijzigd van String naar Integer. Maximale lengte 12.   - Beschrijving LO: MessageId, lengte: 12, Het unieke volgnummer dat aan het uitgaande bericht wordt toegekend. - Het veld \"verwijzingBerichtId\" wat correspondeert met het \"CrossReference\" veld van de mailboxserver:   - is qua type gewijzigd van String naar Integer. Maximale lengte 12.   - kan of weggelaten worden, of gevuld worden met 0 indien het bericht een eerste bericht in de cyclus betreft. - \"aantalKeerOpgehaald\" is toegevoegd aan de ListMessageKenmerken.  ## 0.1.0 - Maart 2024 Initiële versie.  # In ontwikkeling: - Bepalen of het een checksum op de berichtinhoud van meerwaarde kan zijn.  # Voorlopige limieten: | Waarde | Omschrijving | |--------|--------------| | 1      | Aantal ontvangers per bericht. | | 25     | Maximum aantal berichten dat in één PUT request verstuurd mag worden. | | 100     | Maximum aantal berichten dat in één DELETE request verwijderd mag worden | | 2000   | Maximum aantal berichten dat in één LIST request getoond zal worden. Indien wenselijk kunt u dit aantal middels een query-parameter beperken. | | 100    | Maximum aantal berichten dat in één GET request ontvangen mag worden. | | 64kb   | Maximum grootte van één enkel bericht. Één request zal qua grootte dan uitkomen op ((maximale-grootte-enkel-bericht * maximaal-aantal-berichten) + overhead). Houdt er rekening mee dat dit een waarde is die in te toekomst kan gaan groeien. Beperk uw oplossing dus niet op deze waarde! | 

    The version of the OpenAPI document: 0.6.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ListMessageKenmerken(BaseModel):
    """
    ListMessageKenmerken
    """ # noqa: E501
    bericht_id: Annotated[str, Field(strict=True, max_length=12)] = Field(description="Het unieke volgnummer dat aan het uitgaande bericht wordt toegekend door de afzender. De \"BRP berichten API\" voert geen inhoudelijke controles uit op dit BerichtId. Maximaal 12 posities. ", alias="berichtId")
    verwijzing_bericht_id: Optional[Annotated[str, Field(strict=True, max_length=12)]] = Field(default=None, description="Indien het bericht een antwoord is op een eerder door het eindsysteem ontvangen bericht: het `berichtId` van het eerder ontvangen bericht. Het veld correspondeert met het \"CrossReference\" veld van de mailboxserver.  Het volgnummer van het bericht, waarop dit uitgaande bericht een reactie is. Dit volgnummer is het MessageId van het voorgaande bericht uit de cyclus. Is het bericht het eerste van een cyclus dan kan dit veld of weggelaten worden, of gevuld worden met 0; ", alias="verwijzingBerichtId")
    bericht_type: Annotated[str, Field(strict=True, max_length=4)] = Field(description="Het soort bericht (zoals gedefinieerd in het berichtenboek in het Logisch Ontwerp).  * Berichten ten behoeve van de bijhouding en de consistentie van de BRP   * Berichten tussen bijhouders onderling     * Berichten in verband met de vervolginschrijving tussen gemeenten:       * Ii01 Initiatie intergemeentelijke verhuizing       * Ib01 Verhuizen PL intergemeentelijk       * Iv01 Verwijsgegevens       * If01 Fout: PL niet te verzenden       * If21 Fout: de ontvangen PL is niet de aangevraagde       * If31 Fout: de verwijsgegevens zijn niet correct     * Berichten in verband met de vervolginschrijving van de gemeente naar de RNI:       * Rb01 Verhuizen PL van gemeente naar RNI       * Rv01 Verwijsgegevens       * Rf01 Fout: de ontvangen PL kan niet worden opgenomen       * Rf31 Fout: de verwijsgegevens zijn niet correct     * Berichten in verband met de vervolginschrijving van de RNI naar de gemeente:       * Ji01 Initiatie verhuizing PL van RNI naar gemeente       * Jb01 Verhuizen PL van RNI naar gemeente       * Jv01 Verwijsgegevens       * Jf01 Fout: PL niet te verzenden       * Jf21 Fout: de ontvangen PL is niet de aangevraagde       * Jf31 Fout: de verwijsgegevens zijn niet correct     * Berichten in verband met een toevallige geboorte:       * Tb01 Toevallige geboorte       * Tv01 Verwijsgegevens       * Tf01 Fout: persoon niet in te schrijven       * Tf11 Fout: de verwijsgegevens zijn niet correct     * Berichten in verband met een toevallige gebeurtenis:       * Tb02 Toevallige gebeurtenis       * Tf21 Fout: gebeurtenisgegevens niet te verwerken     * Berichten in verband met het opnemen van verwijsgegevens:       * Iv11 Verwijsgegevens       * Iv21 Verificatie verwijsgegevens       * If41 Fout: verwijsgegevens kunnen niet worden opgenomen     * Berichten in verband met wijzigen A-nummer in de verwijsgegevens bij gemeenten en bij de RNI:       * Wa01 Wijziging A-nummer       * Wf01 Fout: A-nummerwijziging niet te verwerken   * Berichten ten behoeve van de bijhouding     * Berichten in verband met verblijfstitel:       * Og11 Opnemen gegevens verblijfstitel       * Of11 Fout: opnemen/wijzigen verblijfstitel niet mogelijk   * Berichten ten behoeve van het bijhouden van de persoonsgegevens in BRP-V     * Berichten in verband met synchronisatie met BRP-V:       * Lg01 Synchronisatiebericht       * Lq01 Synchronisatievraag       * La01 Synchronisatieantwoord       * Lf01 Fout: synchronisatievraag niet te beantwoorden     * Berichten in verband met synchroniciteitsselecties:       * Lg01 Synchronisatiebericht * Berichten ten behoeve van de gegevensverstrekkingen   * Berichten in verband met spontane gegevensverstrekkingen als gevolg van afnemersindicaties op persoonslijsten:     * Gv01 Spontane mutatie     * Gv02 Spontane mutatie: infrastructurele wijziging     * Wa11 Wijziging A-nummer ten behoeve van afnemers     * Ng01 Afvoeren PL     * Ag11 Vulbericht     * Ag21 Conditionele gegevensverstrekking     * Ag31 Foutherstelbericht   * Berichten in verband met selecties:     * Sv01 Selectieverstrekking     * Sv11 Niemand geselecteerd   * Berichten in verband met ad hoc vragen:     * Hq01 Ad hoc vraag     * Ha01 Ad hoc antwoord     * Hf01 Fout: ad hoc vraag niet te beantwoorden   * Berichten in verband met ad hoc adresvragen:     * Xq01 Ad hoc adresvraag     * Xa01 Ad hoc adresantwoord     * Xf01 Fout: ad hoc adresvraag niet te beantwoorden   * Berichten in verband met het muteren van afnemersindicaties op persoonslijsten:     * Ap01 Plaatsen afnemersindicatie op persoonslijst     * Ag01 Gegevensverstrekking als gevolg van ad hoc plaatsing afnemersindicatie op persoonslijst     * Af01 Fout: plaatsen afnemersindicatie op persoonslijst onmogelijk     * Av01 Verwijderen afnemersindicatie van persoonslijst     * Af11 Fout: verwijderen afnemersindicatie van persoonslijst onmogelijk * Overige berichten   * Berichten ten behoeve van het onderhouden van de autorisatietabel     * Berichten in verband met het onderhoud van de autorisatietabel:       * Ct01 Toevoegen tabelregel aan Autorisatietabel       * Cw01 Wijzigen tabelregel in Autorisatietabel       * Cb01 Beëindigen tabelregel in Autorisatietabel     * Berichten ten behoeve van het onderhouden van de overige landelijke tabellen       * Dt01 Toevoegen tabelregel       * Dw01 Wijzigen tabelregel     * De protocolfouten       * Berichten om niet voorziene fouten in ontvangen berichten te melden:         * Pf01 Fout: cyclus         * Pf02 Fout: syntax         * Pf03 Fout: inhoudelijk     * Het vrije bericht       * Bericht, vergelijkbaar met een mededeling op papier en als zodanig te gebruiken:         * Vb01 Vrij bericht         * Vb02 Vrij bericht via webservice     * De verwerkbevestiging       * Bericht om de verwerking van bepaalde gegevens te bevestigen:         * Null Verwerkbevestiging (Null-bericht) ", alias="berichtType")
    bericht_transport_id: StrictStr = Field(description="De is de referentie naar het bericht zoals deze bekend is bij de `BRP berichten API` (UUID). Bij elke interactie met deze dienst omtrent een bericht, wordt deze waarde gebruikt. Het mag, net zoals `berichtVolgnummer` gebruikt worden om het bericht uniek te identificeren.", alias="berichtTransportId")
    bericht_volgnummer: StrictInt = Field(description="Dit volgnummer is het equivalent van het 'Dispatch sequence number'/'MSSequenceNumber' van de mailboxserver. Hiermee kan over verschillende media worden vastgesteld of dit bericht al eerder verwerkt is. Het nummer wordt door deze dienst uniek toegekend aan het bericht.", alias="berichtVolgnummer")
    afzender: Annotated[int, Field(le=9999999, strict=True)] = Field(description="Het unieke nummer van een verzender/ontvanger.")
    dt_ontvangen: datetime = Field(description="Het tijdstip waarop het bericht door de berichten API ontvangen is", alias="dtOntvangen")
    opgehaald: StrictBool = Field(description="Geeft aan of dit bericht al eens eerder opgehaald is.")
    dt_bewaard_tot: datetime = Field(description="Tot dit moment zal het bericht beschikbaar zijn op de berichten API.", alias="dtBewaardTot")
    __properties: ClassVar[List[str]] = ["berichtId", "verwijzingBerichtId", "berichtType", "berichtTransportId", "berichtVolgnummer", "afzender", "dtOntvangen", "opgehaald", "dtBewaardTot"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ListMessageKenmerken from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListMessageKenmerken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "berichtId": obj.get("berichtId"),
            "verwijzingBerichtId": obj.get("verwijzingBerichtId"),
            "berichtType": obj.get("berichtType"),
            "berichtTransportId": obj.get("berichtTransportId"),
            "berichtVolgnummer": obj.get("berichtVolgnummer"),
            "afzender": obj.get("afzender"),
            "dtOntvangen": obj.get("dtOntvangen"),
            "opgehaald": obj.get("opgehaald"),
            "dtBewaardTot": obj.get("dtBewaardTot")
        })
        return _obj


