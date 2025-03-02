# Af01PlDataC21InnerAllOfHistorieInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e0110** | **str** | Het administratienummer, bedoeld in artikel 4.9 van de Wet BRP. ⦿ Groep: Identificatienummers (01) ⦿ Element: A-nummer (01.10) | [optional] 
**e0120** | **str** | Het burgerservicenummer, bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer. ⦿ Groep: Identificatienummers (01) ⦿ Element: Burgerservicenummer (01.20) | [optional] 
**e0210** | **str** | De verzameling namen die, gescheiden door spaties, aan de geslachtsnaam voorafgaat. Indien aanwezig, wordt het predicaat (tabel 38) afgesplitst. ⦿ Groep: Naam (02) ⦿ Element: Voornamen (02.10) | [optional] 
**e0220** | **str** | Een code, voorkomend in Tabel 38, Tabel Adellijke titel/predicaat, die aangeeft welke titel of welk predicaat behoort tot de naam (bij adellijke titel geslachtsnaam, bij predicaat voornaam). ⦿ Groep: Naam (02) ⦿ Element: Adellijke titel/predicaat (02.20) | [optional] 
**e0230** | **str** | Dat deel van de geslachtsnaam dat voorkomt in Tabel 36, Voorvoegseltabel en, gescheiden door een spatie, voorafgaat aan de rest van de geslachtsnaam. ⦿ Groep: Naam (02) ⦿ Element: Voorvoegsel geslachtsnaam (02.30) | [optional] 
**e0240** | **str** | De (geslachts)naam waarvan de eventueel aanwezige voorvoegsels (tabel 36) en adellijke titel/predicaat (tabel 38) zijn afgesplitst. ⦿ Groep: Naam (02) ⦿ Element: Geslachtsnaam (02.40) | [optional] 
**e0310** | **str** | De datum waarop de persoon is geboren. ⦿ Groep: Geboorte (03) ⦿ Element: Geboortedatum (03.10) | [optional] 
**e0320** | **str** | Een code, opgenomen in Tabel 33, Gemeententabel of een buitenlandse plaats of een plaatsbepaling, die aangeeft waar de persoon is geboren. ⦿ Groep: Geboorte (03) ⦿ Element: Geboorteplaats (03.20) | [optional] 
**e0330** | **str** | Een code, opgenomen in Tabel 34, Landentabel, die het land aangeeft waar de persoon is geboren. ⦿ Groep: Geboorte (03) ⦿ Element: Geboorteland (03.30) | [optional] 
**e0910** | **str** | Een code, opgenomen in Tabel 33, Gemeententabel, die aangeeft in welke gemeente de PL zich bevindt of de gemeente waarnaar de PL is uitgeschreven of de gemeente waar de PL voor de eerste keer is opgenomen. In categorie 16 betreft het de gemeente waar zich het tijdelijk verblijfsadres bevindt. ⦿ Groep: Gemeente (09) ⦿ Element: Gemeente van inschrijving (09.10) | [optional] 
**e0920** | **str** | Bij een tijdige aangifte (tussen vier weken voor en vijf dagen na de verhuizing) van vestiging in de gemeente is dit de in de aangifte vermelde datum van adreswijziging. Bij een niet tijdige aangifte is dit de aangiftedatum. Bij inschrijving op grond van een geboorteakte is dit de geboortedatum. Bij ambtshalve inschrijving is dit de datum waarop de betrokkene schriftelijk van het voornemen van ambtshalve opneming mededeling is gedaan. In categorie 16 betreft het de datum waarop betrokkene voor het eerst op het tijdelijk verblijfsadres in deze gemeente is gaan wonen, mits deze adressen in de tijd aaneengesloten zijn. ⦿ Groep: Gemeente (09) ⦿ Element: Datum inschrijving (09.20) | [optional] 
**e7010** | **str** | Een aanduiding die aangeeft dat gegevens wel of niet verstrekt mogen worden. ⦿ Groep: Geheim (70) ⦿ Element: Indicatie geheim (70.10) | [optional] 
**e8310** | **str** | Een aanduiding dat in een categorie één of meer gegevens met betrekking tot de onjuistheid of de strijdigheid met de openbare orde zijn of worden onderzocht. In categorie 08 Verblijfplaats kan de aanduiding tevens aangeven dat er is vastgesteld dat betrokkene niet op het geregistreerde adres woont. ⦿ Groep: Procedure (83) ⦿ Element: Aanduiding gegevens in onderzoek (83.10) | [optional] 
**e8320** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is gestart. ⦿ Groep: Procedure (83) ⦿ Element: Datum ingang onderzoek (83.20) | [optional] 
**e8330** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is beéindigd. ⦿ Groep: Procedure (83) ⦿ Element: Datum einde onderzoek (83.30) | [optional] 
**e8410** | **str** | Een aanduiding dat één of meer gegevens onjuist of strijdig zijn met de openbare orde. ⦿ Groep: Onjuist (84) ⦿ Element: Indicatie onjuist, dan wel strijdigheid met de openbare orde (84.10) | [optional] 
**e8510** | **str** | De datum waarop het geheel van gegevens geldig is geworden. ⦿ Groep: Geldigheid (85) ⦿ Element: Ingangsdatum geldigheid (85.10) | [optional] 
**e8610** | **str** | De datum waarop het geheel van gegevens daadwerkelijk in de BRP is opgenomen. ⦿ Groep: Opneming (86) ⦿ Element: Datum van opneming (86.10) | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c21_inner_all_of_historie_inner import Af01PlDataC21InnerAllOfHistorieInner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC21InnerAllOfHistorieInner from a JSON string
af01_pl_data_c21_inner_all_of_historie_inner_instance = Af01PlDataC21InnerAllOfHistorieInner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC21InnerAllOfHistorieInner.to_json())

# convert the object into a dict
af01_pl_data_c21_inner_all_of_historie_inner_dict = af01_pl_data_c21_inner_all_of_historie_inner_instance.to_dict()
# create an instance of Af01PlDataC21InnerAllOfHistorieInner from a dict
af01_pl_data_c21_inner_all_of_historie_inner_from_dict = Af01PlDataC21InnerAllOfHistorieInner.from_dict(af01_pl_data_c21_inner_all_of_historie_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


