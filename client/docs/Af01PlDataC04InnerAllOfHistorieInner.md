# Af01PlDataC04InnerAllOfHistorieInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e0510** | **str** | Een code, opgenomen in Tabel 32, Nationaliteitentabel, die aangeeft welke nationaliteit de ingeschrevene bezit. ⦿ Groep: Nationaliteit (05) ⦿ Element: Nationaliteit (05.10) | [optional] 
**e6310** | **str** | Een code, opgenomen in Tabel 37, Tabel Reden opnemen/beëindigen nationaliteit, die aanduidt op grond waarvan de ingeschrevene de Nederlandse nationaliteit verkregen heeft dan wel de reden waarom een niet-Nederlandse nationaliteit is opgenomen, dan wel dat het een persoon is waarop het bijzonder Nederlanderschap van toepassing is. ⦿ Groep: Opnemen nationaliteit (63) ⦿ Element: Reden opname nationaliteit (63.10) | [optional] 
**e6410** | **str** | Een code, opgenomen in Tabel 37, Tabel Reden opnemen/beëindigen nationaliteit, die aanduidt op grond waarvan de ingeschrevene de Nederlandse nationaliteit verloren heeft dan wel de reden waarom een niet-Nederlandse nationaliteit is beëindigd, dan wel dat voor een persoon het bijzonder Nederlanderschap niet langer van toepassing is. ⦿ Groep: Beëindigen nationaliteit (64) ⦿ Element: Reden beëindigen nationaliteit (64.10) | [optional] 
**e6510** | **str** | Een aanduiding die of aangeeft dat de ingeschrevene behandeld wordt als Nederlander, of dat door de rechter is vastgesteld dat de ingeschrevene niet de Nederlandse nationaliteit bezit. ⦿ Groep: Bijzonder Nederlanderschap (65) ⦿ Element: Aanduiding bijzonder Nederlanderschap (65.10) | [optional] 
**e7310** | **str** | Het persoonsnummer dat door een EU-land is afgegeven aan een onderdaan en dat van het overgelegde reisdocument is afgeleid. ⦿ Groep: Buitenlands persoonsnummer (73) ⦿ Element: EU-persoonsnummer (73.10) | [optional] 
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
from berichten_api.models.af01_pl_data_c04_inner_all_of_historie_inner import Af01PlDataC04InnerAllOfHistorieInner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC04InnerAllOfHistorieInner from a JSON string
af01_pl_data_c04_inner_all_of_historie_inner_instance = Af01PlDataC04InnerAllOfHistorieInner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC04InnerAllOfHistorieInner.to_json())

# convert the object into a dict
af01_pl_data_c04_inner_all_of_historie_inner_dict = af01_pl_data_c04_inner_all_of_historie_inner_instance.to_dict()
# create an instance of Af01PlDataC04InnerAllOfHistorieInner from a dict
af01_pl_data_c04_inner_all_of_historie_inner_from_dict = Af01PlDataC04InnerAllOfHistorieInner.from_dict(af01_pl_data_c04_inner_all_of_historie_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


