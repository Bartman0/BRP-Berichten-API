# Af01PlDataC02Inner


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
**e0410** | **str** | Een aanduiding die aangeeft dat de ingeschrevene een man of een vrouw is, of dat het geslacht (nog) onbekend is. ⦿ Groep: Geslacht (04) ⦿ Element: Geslachtsaanduiding (04.10) | [optional] 
**e6210** | **str** | De datum waarop de familierechtelijke betrekking is ontstaan. ⦿ Groep: Familierechtelijke betrekking (62) ⦿ Element: Datum ingang familierechtelijke betrekking (62.10) | [optional] 
**e8110** | **str** | Een code, opgenomen in Tabel 33, Gemeententabel, die aangeeft in welke gemeente de akte in de registers van de burgerlijke stand in Nederland is opgenomen. ⦿ Groep: Akte (81) ⦿ Element: Registergemeente akte (81.10) | [optional] 
**e8120** | **str** | Een aanduiding van de akte die is opgenomen in de registers van de burgerlijke stand in Nederland.  De eerste drie posities van het aktenummer dienen conform Tabel 39, Tabel Akteaanduiding te zijn. De laatste 4 posities bevatten een volgnummer van de akte. ⦿ Groep: Akte (81) ⦿ Element: Aktenummer (81.20) | [optional] 
**e8210** | **str** | Een code, opgenomen in Tabel 33, Gemeententabel, die aangeeft in welke gemeente de ontlening aan of de afleiding uit het document heeft plaatsgevonden. ⦿ Groep: Document (82) ⦿ Element: Gemeente document (82.10) | [optional] 
**e8220** | **str** | De datum waarop de ontlening aan of de afleiding uit het document heeft plaatsgevonden. ⦿ Groep: Document (82) ⦿ Element: Datum document (82.20) | [optional] 
**e8230** | **str** | Beschrijving van het document waaraan de gegevens zijn ontleend of waaruit de gegevens zijn afgeleid. ⦿ Groep: Document (82) ⦿ Element: Beschrijving document (82.30) | [optional] 
**e8310** | **str** | Een aanduiding dat in een categorie één of meer gegevens met betrekking tot de onjuistheid of de strijdigheid met de openbare orde zijn of worden onderzocht. In categorie 08 Verblijfplaats kan de aanduiding tevens aangeven dat er is vastgesteld dat betrokkene niet op het geregistreerde adres woont. ⦿ Groep: Procedure (83) ⦿ Element: Aanduiding gegevens in onderzoek (83.10) | [optional] 
**e8320** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is gestart. ⦿ Groep: Procedure (83) ⦿ Element: Datum ingang onderzoek (83.20) | [optional] 
**e8330** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is beéindigd. ⦿ Groep: Procedure (83) ⦿ Element: Datum einde onderzoek (83.30) | [optional] 
**e8410** | **str** | Een aanduiding dat één of meer gegevens onjuist of strijdig zijn met de openbare orde. ⦿ Groep: Onjuist (84) ⦿ Element: Indicatie onjuist, dan wel strijdigheid met de openbare orde (84.10) | [optional] 
**e8510** | **str** | De datum waarop het geheel van gegevens geldig is geworden. ⦿ Groep: Geldigheid (85) ⦿ Element: Ingangsdatum geldigheid (85.10) | [optional] 
**e8610** | **str** | De datum waarop het geheel van gegevens daadwerkelijk in de BRP is opgenomen. ⦿ Groep: Opneming (86) ⦿ Element: Datum van opneming (86.10) | [optional] 
**historie** | [**List[Af01PlDataC02InnerAllOfHistorieInner]**](Af01PlDataC02InnerAllOfHistorieInner.md) |  | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c02_inner import Af01PlDataC02Inner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC02Inner from a JSON string
af01_pl_data_c02_inner_instance = Af01PlDataC02Inner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC02Inner.to_json())

# convert the object into a dict
af01_pl_data_c02_inner_dict = af01_pl_data_c02_inner_instance.to_dict()
# create an instance of Af01PlDataC02Inner from a dict
af01_pl_data_c02_inner_from_dict = Af01PlDataC02Inner.from_dict(af01_pl_data_c02_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


