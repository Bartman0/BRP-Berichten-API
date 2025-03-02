# Af01PlDataC08Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e0910** | **str** | Een code, opgenomen in Tabel 33, Gemeententabel, die aangeeft in welke gemeente de PL zich bevindt of de gemeente waarnaar de PL is uitgeschreven of de gemeente waar de PL voor de eerste keer is opgenomen. In categorie 16 betreft het de gemeente waar zich het tijdelijk verblijfsadres bevindt. ⦿ Groep: Gemeente (09) ⦿ Element: Gemeente van inschrijving (09.10) | [optional] 
**e0920** | **str** | Bij een tijdige aangifte (tussen vier weken voor en vijf dagen na de verhuizing) van vestiging in de gemeente is dit de in de aangifte vermelde datum van adreswijziging. Bij een niet tijdige aangifte is dit de aangiftedatum. Bij inschrijving op grond van een geboorteakte is dit de geboortedatum. Bij ambtshalve inschrijving is dit de datum waarop de betrokkene schriftelijk van het voornemen van ambtshalve opneming mededeling is gedaan. In categorie 16 betreft het de datum waarop betrokkene voor het eerst op het tijdelijk verblijfsadres in deze gemeente is gaan wonen, mits deze adressen in de tijd aaneengesloten zijn. ⦿ Groep: Gemeente (09) ⦿ Element: Datum inschrijving (09.20) | [optional] 
**e1010** | **str** | De aanduiding die aangeeft of het adres de functie heeft van woonadres of briefadres. ⦿ Groep: Adreshouding (10) ⦿ Element: Functie adres (10.10) | [optional] 
**e1020** | **str** | Een geografisch bepaald gebied dat een deel is van het gemeentelijk grondgebied.  Dit element wordt gebruikt als nadere plaatsbepaling van een straat of locatie, indien deze binnen de gemeente niet uniek is. ⦿ Groep: Adreshouding (10) ⦿ Element: Gemeentedeel (10.20) | [optional] 
**e1030** | **str** | De datum van aangifte of ambtshalve melding van verblijf en adres. Bij een tijdige aangifte (tussen vier weken voor en vijf dagen na de verhuizing) van vestiging op het adres is dit de in de aangifte vermelde datum van adreswijziging. Bij een niet tijdige aangifte is dit de aangiftedatum. Bij inschrijving op grond van een geboorteakte is dit de geboortedatum. Bij ambtshalve inschrijving is dit de datum waarop de betrokkene schriftelijk van het voornemen van ambtshalve opneming mededeling is gedaan. ⦿ Groep: Adreshouding (10) ⦿ Element: Datum aanvang adreshouding (10.30) | [optional] 
**e1110** | **str** | De officiële straatnaam zoals door het gemeentebestuur is vastgesteld dan wel een kopie van de inhoud van element 11.15 Naam openbare ruimte,  indien noodzakelijk afgekort volgens de NEN-5825 [2002] norm. ⦿ Groep: Adres (11) ⦿ Element: Straatnaam (11.10) | [optional] 
**e1115** | **str** | Een naam die aan een openbare ruimte is toegekend in een daartoe strekkend formeel gemeentelijk besluit. Een openbare ruimte is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen benaming van een binnen één woonplaats gelegen buitenruimte. Voor &#39;Naam openbare ruimte&#39; mag &#39;officiële straatnaam&#39; gelezen worden. ⦿ Groep: Adres (11) ⦿ Element: Naam openbare ruimte (11.15) | [optional] 
**e1120** | **str** | De numerieke aanduiding zoals deze door het gemeentebestuur aan het object is toegekend dan wel een door of namens het bevoegde gemeentelijke orgaan ten aanzien van een adresseerbaar object toegekende nummering. ⦿ Groep: Adres (11) ⦿ Element: Huisnummer (11.20) | [optional] 
**e1130** | **str** | Een alfabetisch teken achter het huisnummer zoals dit door het gemeentebestuur is toegekend dan wel een door of namens het bevoegde gemeentelijke orgaan ten aanzien van een adresseerbaar object toegekende toevoeging aan een huisnummer in de vorm van een alfabetisch teken. ⦿ Groep: Adres (11) ⦿ Element: Huisletter (11.30) | [optional] 
**e1140** | **str** | Die letters of tekens die noodzakelijk zijn om, naast huisnummer en -letter, de brievenbus te vinden dan wel een door of namens het bevoegde gemeentelijke orgaan ten aanzien van een adresseerbaar object toegekende toevoeging aan een huisnummer of een combinatie van huisletter en huisnummer. ⦿ Groep: Adres (11) ⦿ Element: Huisnummertoevoeging (11.40) | [optional] 
**e1150** | **str** | De aanduiding die wordt gebruikt voor adressen die niet zijn voorzien van de gebruikelijke straatnaam en huisnummeraanduidingen. ⦿ Groep: Adres (11) ⦿ Element: Aanduiding bij huisnummer (11.50) | [optional] 
**e1160** | **str** | De door de PostNL vastgestelde code behorend bij de straatnaam en het huisnummer dan wel de door PostNL vastgestelde code behorende bij een bepaalde combinatie van een naam openbare ruimte en een huisnummer. ⦿ Groep: Adres (11) ⦿ Element: Postcode (11.60) | [optional] 
**e1170** | **str** | Een woonplaatsnaam is de naam van een door het bevoegde gemeentelijke orgaan als zodanig aangewezen gedeelte van het gemeentelijk grondgebied. ⦿ Groep: Adres (11) ⦿ Element: Woonplaatsnaam (11.70) | [optional] 
**e1180** | **str** | Een verblijfplaats kan een ligplaats, een standplaats of een verblijfsobject in een of meerdere panden zijn, waaraan respectievelijk een ligplaatsidentificatie, standplaatsidentificatie of verblijfsobjectidentificatie is toegekend.  De Identificatiecode verblijfplaats is een combinatie van een viercijferige gemeentecode, een tweecijferige objecttypecode die aangeeft of de aanduiding een verblijfsobject (01), ligplaats (02) of standplaats (03) betreft en een voor het betreffende objecttype binnen een gemeente uniek tiencijferig volgnummer. ⦿ Groep: Adres (11) ⦿ Element: Identificatiecode verblijfplaats (11.80) | [optional] 
**e1190** | **str** | De unieke aanduiding van een nummeraanduiding. Een nummeraanduiding is een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een adresseerbaar object.  De Identificatiecode nummeraanduiding is een combinatie van een viercijferige gemeentecode, de tweecijferige objecttypecode 20 die aangeeft dat het om een nummeraanduiding gaat en een voor het betreffende objecttype binnen een gemeente uniek tiencijferig volgnummer. ⦿ Groep: Adres (11) ⦿ Element: Identificatiecode nummeraanduiding (11.90) | [optional] 
**e1210** | **str** | Een geheel of gedeeltelijke omschrijving van de ligging van een object, indien dit niet kan worden aangegeven in de groep 11 Adres. ⦿ Groep: Locatie (12) ⦿ Element: Locatiebeschrijving (12.10) | [optional] 
**e1310** | **str** | Een code, opgenomen in Tabel 34, Landentabel, die het land (buiten Nederland) aangeeft alwaar de ingeschrevene verblijft. In tegenstelling tot bij de gemeente, kan bij de RNI kan de waarde Nederland (6030) wel voorkomen.  Bij het ingaan van een Ministerieel besluit dient hier de standaardwaarde opgenomen te worden. ⦿ Groep: Adres buitenland (13) ⦿ Element: Land adres buitenland (13.10) | [optional] 
**e1320** | **str** | De datum van aangifte of ambtshalve melding van verblijf op het buitenlands adres.  Bij emigratie is dit de datum van vertrek naar het buitenland. Bij ambtshalve uitschrijving is dit de datum waarop de betrokkene schriftelijk van het voornemen tot ambtshalve uitschrijving mededeling is gedaan. Bij uitschrijving wegens het ingaan van een Ministerieel besluit is dit de datum van dat besluit. In alle andere gevallen is dit de datum waarop de aangifte is ontvangen. ⦿ Groep: Adres buitenland (13) ⦿ Element: Datum aanvang adres buitenland (13.20) | [optional] 
**e1330** | **str** | Eerste deel van het adres in het buitenland, met uitzondering van het land. ⦿ Groep: Adres buitenland (13) ⦿ Element: Regel 1 adres buitenland (13.30) | [optional] 
**e1340** | **str** | Tweede deel van het adres in het buitenland, met uitzondering van het land. ⦿ Groep: Adres buitenland (13) ⦿ Element: Regel 2 adres buitenland (13.40) | [optional] 
**e1350** | **str** | Derde deel van het adres in het buitenland, met uitzondering van het land. ⦿ Groep: Adres buitenland (13) ⦿ Element: Regel 3 adres buitenland (13.50) | [optional] 
**e1410** | **str** | Een code, opgenomen in Tabel 34, Landentabel, die het land aangeeft waar de ingeschrevene verblijf hield voor (her)vestiging in Nederland. Bij het opheffen van een Ministerieel besluit dient hier de standaardwaarde opgenomen te worden. ⦿ Groep: Immigratie (14) ⦿ Element: Land vanwaar ingeschreven (14.10) | [optional] 
**e1420** | **str** | De datum van inschrijving in Nederland.  Bij ambtshalve inschrijving is dit de datum waarop de betrokkene schriftelijk van het voornemen tot ambtshalve inschrijving mededeling is gedaan. In alle andere gevallen is dit de datum waarop de aangifte is ontvangen. ⦿ Groep: Immigratie (14) ⦿ Element: Datum vestiging in Nederland (14.20) | [optional] 
**e7210** | **str** | Een aanduiding van de persoon door wie de aangifte van verblijf en adres is gedaan. ⦿ Groep: Adresaangifte (72) ⦿ Element: Omschrijving van de aangifte adreshouding (72.10) | [optional] 
**e7510** | **str** | Een aanduiding dat gedurende de opschorting van de bijhouding van de PL documenten zijn binnengekomen, die na de beëindiging van de opschorting verwerkt moeten worden. ⦿ Groep: Documentindicatie (75) ⦿ Element: Indicatie document (75.10) | [optional] 
**e8310** | **str** | Een aanduiding dat in een categorie één of meer gegevens met betrekking tot de onjuistheid of de strijdigheid met de openbare orde zijn of worden onderzocht. In categorie 08 Verblijfplaats kan de aanduiding tevens aangeven dat er is vastgesteld dat betrokkene niet op het geregistreerde adres woont. ⦿ Groep: Procedure (83) ⦿ Element: Aanduiding gegevens in onderzoek (83.10) | [optional] 
**e8320** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is gestart. ⦿ Groep: Procedure (83) ⦿ Element: Datum ingang onderzoek (83.20) | [optional] 
**e8330** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is beéindigd. ⦿ Groep: Procedure (83) ⦿ Element: Datum einde onderzoek (83.30) | [optional] 
**e8410** | **str** | Een aanduiding dat één of meer gegevens onjuist of strijdig zijn met de openbare orde. ⦿ Groep: Onjuist (84) ⦿ Element: Indicatie onjuist, dan wel strijdigheid met de openbare orde (84.10) | [optional] 
**e8510** | **str** | De datum waarop het geheel van gegevens geldig is geworden. ⦿ Groep: Geldigheid (85) ⦿ Element: Ingangsdatum geldigheid (85.10) | [optional] 
**e8610** | **str** | De datum waarop het geheel van gegevens daadwerkelijk in de BRP is opgenomen. ⦿ Groep: Opneming (86) ⦿ Element: Datum van opneming (86.10) | [optional] 
**e8810** | **str** | Een code, voorkomend in Tabel 60, RNI-deelnemerstabel, die aangeeft welke RNI-deelnemer (een deel van) de gegevens in de betrokken categorie heeft aangeleverd. ⦿ Groep: RNI-deelnemer (88) ⦿ Element: RNI-deelnemer (88.10) | [optional] 
**e8820** | **str** | Een aanduiding van het verdrag op basis waarvan (een deel van) de gegevens in de betrokken categorie door een buitenlandse zusterorganisatie van een RNI-deelnemer aan die deelnemer zijn aangeleverd. ⦿ Groep: RNI-deelnemer (88) ⦿ Element: Omschrijving verdrag (88.20) | [optional] 
**historie** | [**List[Af01PlDataC08InnerAllOfHistorieInner]**](Af01PlDataC08InnerAllOfHistorieInner.md) |  | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c08_inner import Af01PlDataC08Inner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC08Inner from a JSON string
af01_pl_data_c08_inner_instance = Af01PlDataC08Inner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC08Inner.to_json())

# convert the object into a dict
af01_pl_data_c08_inner_dict = af01_pl_data_c08_inner_instance.to_dict()
# create an instance of Af01PlDataC08Inner from a dict
af01_pl_data_c08_inner_from_dict = Af01PlDataC08Inner.from_dict(af01_pl_data_c08_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


