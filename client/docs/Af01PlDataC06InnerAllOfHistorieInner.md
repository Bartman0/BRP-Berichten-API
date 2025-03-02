# Af01PlDataC06InnerAllOfHistorieInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e0810** | **str** | De datum van overlijden. ⦿ Groep: Overlijden (08) ⦿ Element: Datum overlijden (08.10) | [optional] 
**e0820** | **str** | Een code, opgenomen in Tabel 33, Gemeententabel of een buitenlandse plaats of een plaatsbepaling, die aangeeft waar het overlijden heeft plaatsgevonden. ⦿ Groep: Overlijden (08) ⦿ Element: Plaats overlijden (08.20) | [optional] 
**e0830** | **str** | Een code, opgenomen in Tabel 34, Landentabel, die het land aangeeft waar de persoon is overleden. ⦿ Groep: Overlijden (08) ⦿ Element: Land overlijden (08.30) | [optional] 
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
**e8810** | **str** | Een code, voorkomend in Tabel 60, RNI-deelnemerstabel, die aangeeft welke RNI-deelnemer (een deel van) de gegevens in de betrokken categorie heeft aangeleverd. ⦿ Groep: RNI-deelnemer (88) ⦿ Element: RNI-deelnemer (88.10) | [optional] 
**e8820** | **str** | Een aanduiding van het verdrag op basis waarvan (een deel van) de gegevens in de betrokken categorie door een buitenlandse zusterorganisatie van een RNI-deelnemer aan die deelnemer zijn aangeleverd. ⦿ Groep: RNI-deelnemer (88) ⦿ Element: Omschrijving verdrag (88.20) | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c06_inner_all_of_historie_inner import Af01PlDataC06InnerAllOfHistorieInner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC06InnerAllOfHistorieInner from a JSON string
af01_pl_data_c06_inner_all_of_historie_inner_instance = Af01PlDataC06InnerAllOfHistorieInner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC06InnerAllOfHistorieInner.to_json())

# convert the object into a dict
af01_pl_data_c06_inner_all_of_historie_inner_dict = af01_pl_data_c06_inner_all_of_historie_inner_instance.to_dict()
# create an instance of Af01PlDataC06InnerAllOfHistorieInner from a dict
af01_pl_data_c06_inner_all_of_historie_inner_from_dict = Af01PlDataC06InnerAllOfHistorieInner.from_dict(af01_pl_data_c06_inner_all_of_historie_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


