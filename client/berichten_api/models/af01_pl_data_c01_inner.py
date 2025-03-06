# coding: utf-8

"""
    BRP Berichten API

    Een REST API voor het a-synchroon uitwisselen van berichten welke in het Logisch Ontwerp gedefinieerd zijn.  # Wijzigingshistorie:  ## 0.6.3 Januari 2025 - Tekstuele verwijzing naar '/berichten/list' vervangen door '/berichten'.  ## 0.6.2 Januari 2025 - OAuth endpoint demo omgeving gecorrigeerd.  ## 0.6.1 Januari 2025 - Ping endpoints zijn niet langer bereikbaar zonder eerst te authenticeren.  ## 0.6.0 Januari 2025 - Servers toegevoegd.   - Hiervoor moesten de paden van de endpoints aangepast worden. Hierdoor is '/api/v1' komen te vervallen bij de endpoints. Dit is verhuist naar de base-url's van de genoemde servers. - Authenticatie details toegevoegd. - Foutmeldingen bij het conversie endpoint bijgewerkt. - Alle namespace paden van de foutmeldingen nagelopen en gecorrigeerd daar waar nodig. Dit zodat ze consistent starten met: \"https://www.rvig.nl/brp/berichten-api/probleem/\".  ## 0.5.5 November 2024 - 'berichtVolgnummer' en 'afzender' required gemaakt in ListMessageKenmerken (en daardoor ook in GetMessageKenmerken). - De GET en DELETE foutsituaties zijn voorzien van discriminators ten behoeve van het onderscheiden van foutsituatie subtypes door de gegenereerde client.  ## 0.5.4 November 2024 - Properties van PagineringResultaat en PagineerbaarResultaat welke altijd aanwezig zullen zijn bij een list-request required gemaakt. - Required properties van put-message-antwoord gecorrigeerd. - Schema van het Null bericht gecorrigeerd.  ## 0.5.3 November 2024 - Het Sv11 bericht is qua schema aangepast aangezien deze onterecht de property plData bevatte. Deze property is verwijderd uit dit bericht. - Foutsituaties zijn voorzien van discriminators ten behoeve van het onderscheiden van foutsituatie subtypes door de gegenereerde client.  ## 0.5.2 Oktober 2024 - De request die volledig afgekeurd worden en een statuscode 4xx of 5xx retourneren, doen dit nu met de response header 'Content-Type: application/problem+json'. - Requests die een 2xx response in JSON formaat retourneren, doen dit met \"Content-Type: application/json\" ipv \"Content-Type: application/json: charset=utf-8\". Conform rfc8259 (https://www.rfc-editor.org/rfc/rfc8259) is JSON altijd in UTF-8 formaat en heeft dit type geen charset parameter.  ## 0.5.1 Oktober 2024  - De fout BBA-PUT-F002 is aangepast naar een algemene fout voor onjuiste velden in een PutMessage, via het veld \"invalidParams\" in de response word aangegeven welke velden onjuist zijn en waarom.  ## 0.5.0 September 2024  - Het veld berichtId en verwijzingBerichtId zijn omgezet van type 'integer' naar type 'string' om beter aan te sluiten op de bestaande voorziening.  - Het probleem-antwoord response object is overal vervangen met de algemene Foutmelding response welke zich conformeert aan RFC7807.  - De velden 'foutTitel', 'foutType', 'foutDetail' zijn aangepast naar 'title, 'type', 'detail' zodat zij zich conformeren aan de RFC7807.  - De afhankelijkheid op 'openapi-problem-detail-v1.yml' is komen te vervallen (https://github.com/rvig-brp/BRP-Berichten-API/issues/3).  ## 0.4.1 Juli 2024  - Het json-schema voor de autorisatieberichten Ct01, Cw01 en Cb01 is toegevoegd.  - De ontvanger is opgenomen in de response bij het verzenden van een bericht. Dit is met name relevant wanneer er een bericht naar een berichtgroep gestuurd wordt. In dat geval weet de verzender wie de uiteindelijke ontvangers zijn. Bij het versturen van een bericht naar de een regulier account zal dit nummer 1:1 overeenkomen met de ontvanger die bij het te verzenden bericht is opgegeven.  ## 0.4.0 Juni 2024 - De json-schema's van de berichtsoorten zijn opgenomen in de OpenAPI Specificatie. Voor elke berichtsoort die het LO beschrijft, is opgenomen hoe dit bericht gestructureerd is.   - Houdt er rekening mee dat het weergeven van de OpenAPI specificatie in de web-versie va SwaggerUI hierdoor trager geworden is. Het is aan te raden om de alternatieve (redocly) weergave te gebruiken:     - https://brp-berichten-api.dictua.ictu-sr.nl/openapi/berichten-api.html     - De JSON schema's zijn tevens te vinden op onze Github pagina. - De JSON-response van het conversie endpoint is iets aangepast zodat naast het geconverteerde bericht tevens validatiefouten opgenomen kunnen worden.  ## 0.3.0 - Mei 2024 - Conversie endpoints   - Introductie bericht-conversie (/berichten/conversie) endpoint. Houdt er rekening mee dat de conversie naar JSON opgenomen is, maar nog niet geïmplementeerd is in de demo omgeving. - Het limiet van het aantal berichten dat verwijderd kan worden is gelijkgesteld aan dat wat gelijktijdig opgehaald kan worden (100). - De API is hernoemd van \"BRP A-Synchrone berichten API\" naar \"BRP berichten API\".   - Nieuwe URL's demo omgeving:     - https://brp-berichten-api.dictua.ictu-sr.nl/api/v1/berichten     - https://brp-berichten-api.dictua.ictu-sr.nl/openapi/berichten-api.html     - https://brp-berichten-api.dictua.ictu-sr.nl/swagger-ui/index.html - Beschikbaarheid endpoint(s)   - Er is een tweede ping endpoint bijgekomen waardoor en nu een HEAD of een GET gedaan kan worden. De response blijft hetzelfde. U kunt zelf kiezen welke van deze twee u hanteert.   - De noodzaak voor authenticatie op het `ping` endpoint is komen te vervallen. U kunt dus zonder noodzaak van authenticatie vaststellen of de dienst beschikbaar is.  ## 0.2.2 - April 2024 - Ping operatie toegevoegd t.b.v. het verifiëren dat er communicatie met de berichtendienst mogelijks is. - De standaard sortering bij een LIST operatie is op dit moment:   1. `Datum + tijdstip van ontvangst` waarbij geldt dat het oudste bericht als eerste wordt weergegeven in de lijst met beschikbare berichten (rationale deze dient als eerste verwerkt worden door de ontvanger).   2. Indien `datum + tijdstip van ontvangst` gelijk zijn (wat kan voorkomen aangezien er meerdere berichten tegelijk ingestuurd kunnen worden), dan worden `afzender` en het `messageId` meegenomen in de sortering. De volgorde die de afzender toegekend heen via de messageId is op dat moment dus bepalend.  ## 0.2.1 - April 2024 - Mogelijkheden tot sortering bij een list operatie zijn verwijderd. De standaard sortering wordt nog bepaald. - Demo omgeving is toegevoegd aan de lijst met servers.   - API te benaderen via https://brp-berichten-api.dictua.ictu-sr.nl/api/v1/berichten   - Swagger UI via: https://brp-berichten-api.dictua.ictu-sr.nl/swagger-ui/index.html   - De OpenAPI specificatie via: https://brp-berichten-api.dictua.ictu-sr.nl/openapi.brp-berichten-api-v1.yaml - Wachtwoord wijzigingen optie is verwijderd. - Het `berichtFormaat` attribuut is komen te vervallen. Alle berichten zijn nu per definitie in JSON formaat. De eis om de berichtInhoud Base64 te   encoderen komt daarmee te vervallen. - Voorbeelddata verbeterd. - Tellingen endpoint toegevoegd welke invulling geeft aan de mailbox Summarize tegenhanger. - Delete endpoint gecorrigeerd. De collectie `succesvolVerwijderdeBerichten` was van het type string i.p.v. berichtTransportId. - Limieten zijn gewijzigd:   - Het aantal berichten dat via een PUT verstuurd kan worden is verhoogd naar 25. Uitgaande van een gemiddelde berichtgrootte van 40kb geeft dat een request van 1MB groot.   - Het aantal berichten dat via een LIST opgevraagd kan worden is vergroot naar 2000. Daarbij krijgt u de mogelijkheid om dit aantal te beperken.     - 2000 berichten in een LIST operatie komt neer op ongeveer 600KB response grootte.   - Het aantal berichten dat via een GET ontvangen kan worden is verhoogd naar 100. Dit heeft te maken met de gangbare (veilige) restricties van een URL qua lengte (2KB).     - Voor de URL worden 256 bytes gereserveerd.       - Voor de UUID blijven dan 1.792 bytes over.     - Een BerichtTransportId is 17 bytes groot (UUID + separatie-karakter ',')       - Uitgaande van 17 bytes, zou dit 105 keer herhaald kunnen worden. Om aan de veilige kan te zitten en om op een mooi rond getal uit te komen kiezen wij voor 100 als limiet.     - Uitgaande van een gemiddelde berichtgrootte van 40KB komt je met 100 berichten uit op 4MB qua response-grootte. - \"aantalKeerOpgehaald\" en \"dtLaatstOpgehaald\" zijn verwijderd uit response van LIST (ListMessageKenmerken schema). Wij zien hierin geen meerwaarde voor de aansluitende partijen. Wel kunt u blijven zien OF het bericht is opgehaald (boolean waarde).  ## 0.2.0 - April 2024 - \"List\" verzoek is verhuisd van \"/berichten/lijst\" --> \"/berichten\" - \"GET\" van meerdere berichten wordt gedaan middels path-parameters i.p.v. query-parameters en is samengevoegd met het endpoint voor het ophalen van een enkel bericht.<br/>   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID])   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID]) - \"DELETE\" van meerdere berichten wordt gedaan middels path-parameters i.p.v. query-parameters en is samengevoegd met het endpoint voor het verwijderen van een enkel bericht.<br/>   (/berichten/?berichtTransportIds=[UUID],[UUID] --> /berichten/[UUID],[UUID]) - Het \"berichtId\" wat correspondeert met het \"MessageId\" veld van de mailboxserver is qua type gewijzigd van String naar Integer. Maximale lengte 12.   - Beschrijving LO: MessageId, lengte: 12, Het unieke volgnummer dat aan het uitgaande bericht wordt toegekend. - Het veld \"verwijzingBerichtId\" wat correspondeert met het \"CrossReference\" veld van de mailboxserver:   - is qua type gewijzigd van String naar Integer. Maximale lengte 12.   - kan of weggelaten worden, of gevuld worden met 0 indien het bericht een eerste bericht in de cyclus betreft. - \"aantalKeerOpgehaald\" is toegevoegd aan de ListMessageKenmerken.  ## 0.1.0 - Maart 2024 Initiële versie.  # In ontwikkeling: - Bepalen of het een checksum op de berichtinhoud van meerwaarde kan zijn.  # Voorlopige limieten: | Waarde | Omschrijving | |--------|--------------| | 1      | Aantal ontvangers per bericht. | | 25     | Maximum aantal berichten dat in één PUT request verstuurd mag worden. | | 100     | Maximum aantal berichten dat in één DELETE request verwijderd mag worden | | 2000   | Maximum aantal berichten dat in één LIST request getoond zal worden. Indien wenselijk kunt u dit aantal middels een query-parameter beperken. | | 100    | Maximum aantal berichten dat in één GET request ontvangen mag worden. | | 64kb   | Maximum grootte van één enkel bericht. Één request zal qua grootte dan uitkomen op ((maximale-grootte-enkel-bericht * maximaal-aantal-berichten) + overhead). Houdt er rekening mee dat dit een waarde is die in te toekomst kan gaan groeien. Beperk uw oplossing dus niet op deze waarde! | 

    The version of the OpenAPI document: 0.6.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from berichten_api.models.af01_pl_data_c01_inner_all_of_historie_inner import Af01PlDataC01InnerAllOfHistorieInner
from typing import Optional, Set
from typing_extensions import Self

class Af01PlDataC01Inner(BaseModel):
    """
    Af01PlDataC01Inner
    """ # noqa: E501
    e0110: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Het administratienummer, bedoeld in artikel 4.9 van de Wet BRP. ⦿ Groep: Identificatienummers (01) ⦿ Element: A-nummer (01.10)")
    e0120: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Het burgerservicenummer, bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer. ⦿ Groep: Identificatienummers (01) ⦿ Element: Burgerservicenummer (01.20)")
    e0210: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=200)]] = Field(default=None, description="De verzameling namen die, gescheiden door spaties, aan de geslachtsnaam voorafgaat. Indien aanwezig, wordt het predicaat (tabel 38) afgesplitst. ⦿ Groep: Naam (02) ⦿ Element: Voornamen (02.10)")
    e0220: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Een code, voorkomend in Tabel 38, Tabel Adellijke titel/predicaat, die aangeeft welke titel of welk predicaat behoort tot de naam (bij adellijke titel geslachtsnaam, bij predicaat voornaam). ⦿ Groep: Naam (02) ⦿ Element: Adellijke titel/predicaat (02.20)")
    e0230: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=10)]] = Field(default=None, description="Dat deel van de geslachtsnaam dat voorkomt in Tabel 36, Voorvoegseltabel en, gescheiden door een spatie, voorafgaat aan de rest van de geslachtsnaam. ⦿ Groep: Naam (02) ⦿ Element: Voorvoegsel geslachtsnaam (02.30)")
    e0240: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=200)]] = Field(default=None, description="De (geslachts)naam waarvan de eventueel aanwezige voorvoegsels (tabel 36) en adellijke titel/predicaat (tabel 38) zijn afgesplitst. ⦿ Groep: Naam (02) ⦿ Element: Geslachtsnaam (02.40)")
    e0310: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="De datum waarop de persoon is geboren. ⦿ Groep: Geboorte (03) ⦿ Element: Geboortedatum (03.10)")
    e0320: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=40)]] = Field(default=None, description="Een code, opgenomen in Tabel 33, Gemeententabel of een buitenlandse plaats of een plaatsbepaling, die aangeeft waar de persoon is geboren. ⦿ Groep: Geboorte (03) ⦿ Element: Geboorteplaats (03.20)")
    e0330: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4)]] = Field(default=None, description="Een code, opgenomen in Tabel 34, Landentabel, die het land aangeeft waar de persoon is geboren. ⦿ Groep: Geboorte (03) ⦿ Element: Geboorteland (03.30)")
    e0410: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1)]] = Field(default=None, description="Een aanduiding die aangeeft dat de ingeschrevene een man of een vrouw is, of dat het geslacht (nog) onbekend is. ⦿ Groep: Geslacht (04) ⦿ Element: Geslachtsaanduiding (04.10)")
    e2010: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Het administratienummer dat eerder aan de betrokken persoon is toegekend geweest. ⦿ Groep: A-nummerverwijzingen (20) ⦿ Element: Vorig A-nummer (20.10)")
    e2020: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Het administratienummer dat nadien aan de betrokken persoon is toegekend. ⦿ Groep: A-nummerverwijzingen (20) ⦿ Element: Volgend A-nummer (20.20)")
    e6110: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1)]] = Field(default=None, description="Een aanduiding voor de wijze van aanschrijving van de ingeschrevene. ⦿ Groep: Naamgebruik (61) ⦿ Element: Aanduiding naamgebruik (61.10)")
    e8110: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4)]] = Field(default=None, description="Een code, opgenomen in Tabel 33, Gemeententabel, die aangeeft in welke gemeente de akte in de registers van de burgerlijke stand in Nederland is opgenomen. ⦿ Groep: Akte (81) ⦿ Element: Registergemeente akte (81.10)")
    e8120: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=7)]] = Field(default=None, description="Een aanduiding van de akte die is opgenomen in de registers van de burgerlijke stand in Nederland.  De eerste drie posities van het aktenummer dienen conform Tabel 39, Tabel Akteaanduiding te zijn. De laatste 4 posities bevatten een volgnummer van de akte. ⦿ Groep: Akte (81) ⦿ Element: Aktenummer (81.20)")
    e8210: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4)]] = Field(default=None, description="Een code, opgenomen in Tabel 33, Gemeententabel, die aangeeft in welke gemeente de ontlening aan of de afleiding uit het document heeft plaatsgevonden. ⦿ Groep: Document (82) ⦿ Element: Gemeente document (82.10)")
    e8220: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="De datum waarop de ontlening aan of de afleiding uit het document heeft plaatsgevonden. ⦿ Groep: Document (82) ⦿ Element: Datum document (82.20)")
    e8230: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=40)]] = Field(default=None, description="Beschrijving van het document waaraan de gegevens zijn ontleend of waaruit de gegevens zijn afgeleid. ⦿ Groep: Document (82) ⦿ Element: Beschrijving document (82.30)")
    e8310: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=6)]] = Field(default=None, description="Een aanduiding dat in een categorie één of meer gegevens met betrekking tot de onjuistheid of de strijdigheid met de openbare orde zijn of worden onderzocht. In categorie 08 Verblijfplaats kan de aanduiding tevens aangeven dat er is vastgesteld dat betrokkene niet op het geregistreerde adres woont. ⦿ Groep: Procedure (83) ⦿ Element: Aanduiding gegevens in onderzoek (83.10)")
    e8320: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is gestart. ⦿ Groep: Procedure (83) ⦿ Element: Datum ingang onderzoek (83.20)")
    e8330: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is beéindigd. ⦿ Groep: Procedure (83) ⦿ Element: Datum einde onderzoek (83.30)")
    e8410: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1)]] = Field(default=None, description="Een aanduiding dat één of meer gegevens onjuist of strijdig zijn met de openbare orde. ⦿ Groep: Onjuist (84) ⦿ Element: Indicatie onjuist, dan wel strijdigheid met de openbare orde (84.10)")
    e8510: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="De datum waarop het geheel van gegevens geldig is geworden. ⦿ Groep: Geldigheid (85) ⦿ Element: Ingangsdatum geldigheid (85.10)")
    e8610: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="De datum waarop het geheel van gegevens daadwerkelijk in de BRP is opgenomen. ⦿ Groep: Opneming (86) ⦿ Element: Datum van opneming (86.10)")
    e8810: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4)]] = Field(default=None, description="Een code, voorkomend in Tabel 60, RNI-deelnemerstabel, die aangeeft welke RNI-deelnemer (een deel van) de gegevens in de betrokken categorie heeft aangeleverd. ⦿ Groep: RNI-deelnemer (88) ⦿ Element: RNI-deelnemer (88.10)")
    e8820: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Een aanduiding van het verdrag op basis waarvan (een deel van) de gegevens in de betrokken categorie door een buitenlandse zusterorganisatie van een RNI-deelnemer aan die deelnemer zijn aangeleverd. ⦿ Groep: RNI-deelnemer (88) ⦿ Element: Omschrijving verdrag (88.20)")
    historie: Optional[Annotated[List[Af01PlDataC01InnerAllOfHistorieInner], Field(min_length=1)]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["e0110", "e0120", "e0210", "e0220", "e0230", "e0240", "e0310", "e0320", "e0330", "e0410", "e2010", "e2020", "e6110", "e8110", "e8120", "e8210", "e8220", "e8230", "e8310", "e8320", "e8330", "e8410", "e8510", "e8610", "e8810", "e8820", "historie"]

    @field_validator('e0110')
    def e0110_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(|[0-9]{10})$", value):
            raise ValueError(r"must validate the regular expression /^(|[0-9]{10})$/")
        return value

    @field_validator('e0120')
    def e0120_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(|[0-9]{9})$", value):
            raise ValueError(r"must validate the regular expression /^(|[0-9]{9})$/")
        return value

    @field_validator('e0220')
    def e0220_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^$|^[a-zA-Z]{1,2}$", value):
            raise ValueError(r"must validate the regular expression /^$|^[a-zA-Z]{1,2}$/")
        return value

    @field_validator('e0310')
    def e0310_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(|[0-9]{8})$", value):
            raise ValueError(r"must validate the regular expression /^(|[0-9]{8})$/")
        return value

    @field_validator('e2010')
    def e2010_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(|[0-9]{10})$", value):
            raise ValueError(r"must validate the regular expression /^(|[0-9]{10})$/")
        return value

    @field_validator('e2020')
    def e2020_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(|[0-9]{10})$", value):
            raise ValueError(r"must validate the regular expression /^(|[0-9]{10})$/")
        return value

    @field_validator('e8220')
    def e8220_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(|[0-9]{8})$", value):
            raise ValueError(r"must validate the regular expression /^(|[0-9]{8})$/")
        return value

    @field_validator('e8320')
    def e8320_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(|[0-9]{8})$", value):
            raise ValueError(r"must validate the regular expression /^(|[0-9]{8})$/")
        return value

    @field_validator('e8330')
    def e8330_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(|[0-9]{8})$", value):
            raise ValueError(r"must validate the regular expression /^(|[0-9]{8})$/")
        return value

    @field_validator('e8510')
    def e8510_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(|[0-9]{8})$", value):
            raise ValueError(r"must validate the regular expression /^(|[0-9]{8})$/")
        return value

    @field_validator('e8610')
    def e8610_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(|[0-9]{8})$", value):
            raise ValueError(r"must validate the regular expression /^(|[0-9]{8})$/")
        return value

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
        """Create an instance of Af01PlDataC01Inner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in historie (list)
        _items = []
        if self.historie:
            for _item_historie in self.historie:
                if _item_historie:
                    _items.append(_item_historie.to_dict())
            _dict['historie'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Af01PlDataC01Inner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "e0110": obj.get("e0110"),
            "e0120": obj.get("e0120"),
            "e0210": obj.get("e0210"),
            "e0220": obj.get("e0220"),
            "e0230": obj.get("e0230"),
            "e0240": obj.get("e0240"),
            "e0310": obj.get("e0310"),
            "e0320": obj.get("e0320"),
            "e0330": obj.get("e0330"),
            "e0410": obj.get("e0410"),
            "e2010": obj.get("e2010"),
            "e2020": obj.get("e2020"),
            "e6110": obj.get("e6110"),
            "e8110": obj.get("e8110"),
            "e8120": obj.get("e8120"),
            "e8210": obj.get("e8210"),
            "e8220": obj.get("e8220"),
            "e8230": obj.get("e8230"),
            "e8310": obj.get("e8310"),
            "e8320": obj.get("e8320"),
            "e8330": obj.get("e8330"),
            "e8410": obj.get("e8410"),
            "e8510": obj.get("e8510"),
            "e8610": obj.get("e8610"),
            "e8810": obj.get("e8810"),
            "e8820": obj.get("e8820"),
            "historie": [Af01PlDataC01InnerAllOfHistorieInner.from_dict(_item) for _item in obj["historie"]] if obj.get("historie") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


