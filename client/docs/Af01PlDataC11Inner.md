# Af01PlDataC11Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e3210** | **str** | Een aanduiding die aangeeft wie belast is met het gezag over de minderjarige ingeschrevene. ⦿ Groep: Gezag minderjarige (32) ⦿ Element: Indicatie gezag minderjarige (32.10) | [optional] 
**e3310** | **str** | Een aanduiding dat de ingeschrevene onder curatele is gesteld. ⦿ Groep: Curatele (33) ⦿ Element: Indicatie curateleregister (33.10) | [optional] 
**e8210** | **str** | Een code, opgenomen in Tabel 33, Gemeententabel, die aangeeft in welke gemeente de ontlening aan of de afleiding uit het document heeft plaatsgevonden. ⦿ Groep: Document (82) ⦿ Element: Gemeente document (82.10) | [optional] 
**e8220** | **str** | De datum waarop de ontlening aan of de afleiding uit het document heeft plaatsgevonden. ⦿ Groep: Document (82) ⦿ Element: Datum document (82.20) | [optional] 
**e8230** | **str** | Beschrijving van het document waaraan de gegevens zijn ontleend of waaruit de gegevens zijn afgeleid. ⦿ Groep: Document (82) ⦿ Element: Beschrijving document (82.30) | [optional] 
**e8310** | **str** | Een aanduiding dat in een categorie één of meer gegevens met betrekking tot de onjuistheid of de strijdigheid met de openbare orde zijn of worden onderzocht. In categorie 08 Verblijfplaats kan de aanduiding tevens aangeven dat er is vastgesteld dat betrokkene niet op het geregistreerde adres woont. ⦿ Groep: Procedure (83) ⦿ Element: Aanduiding gegevens in onderzoek (83.10) | [optional] 
**e8320** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is gestart. ⦿ Groep: Procedure (83) ⦿ Element: Datum ingang onderzoek (83.20) | [optional] 
**e8330** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is beéindigd. ⦿ Groep: Procedure (83) ⦿ Element: Datum einde onderzoek (83.30) | [optional] 
**e8410** | **str** | Een aanduiding dat één of meer gegevens onjuist of strijdig zijn met de openbare orde. ⦿ Groep: Onjuist (84) ⦿ Element: Indicatie onjuist, dan wel strijdigheid met de openbare orde (84.10) | [optional] 
**e8510** | **str** | De datum waarop het geheel van gegevens geldig is geworden. ⦿ Groep: Geldigheid (85) ⦿ Element: Ingangsdatum geldigheid (85.10) | [optional] 
**e8610** | **str** | De datum waarop het geheel van gegevens daadwerkelijk in de BRP is opgenomen. ⦿ Groep: Opneming (86) ⦿ Element: Datum van opneming (86.10) | [optional] 
**historie** | [**List[Af01PlDataC11InnerAllOfHistorieInner]**](Af01PlDataC11InnerAllOfHistorieInner.md) |  | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c11_inner import Af01PlDataC11Inner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC11Inner from a JSON string
af01_pl_data_c11_inner_instance = Af01PlDataC11Inner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC11Inner.to_json())

# convert the object into a dict
af01_pl_data_c11_inner_dict = af01_pl_data_c11_inner_instance.to_dict()
# create an instance of Af01PlDataC11Inner from a dict
af01_pl_data_c11_inner_from_dict = Af01PlDataC11Inner.from_dict(af01_pl_data_c11_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


