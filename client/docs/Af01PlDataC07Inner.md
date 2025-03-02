# Af01PlDataC07Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e6620** | **str** | De datum waarop de gemeente de PL naar een andere gemeente of de RNI stuurt. ⦿ Groep: Blokkering (66) ⦿ Element: Datum ingang blokkering PL (66.20) | [optional] 
**e6710** | **str** | De datum waarop de bijhouding van de PL (gedeeltelijk) is opgeschort. ⦿ Groep: Opschorting (67) ⦿ Element: Datum opschorting bijhouding (67.10) | [optional] 
**e6720** | **str** | Een aanduiding van de reden waarom de bijhouding van de PL geheel of gedeeltelijk is opgeschort. ⦿ Groep: Opschorting (67) ⦿ Element: Omschrijving reden opschorting bijhouding (67.20) | [optional] 
**e6810** | **str** | Dit is de datum vanaf wanneer de persoon is ingeschreven in de BRP. ⦿ Groep: Opname (68) ⦿ Element: Datum eerste inschrijving BRP (68.10) | [optional] 
**e6910** | **str** | Een code, opgenomen in Tabel 33, Gemeententabel, die aangeeft in welke gemeente de PK zich bevindt. ⦿ Groep: Gemeente PK (69) ⦿ Element: Gemeente waar de PK zich bevindt (69.10) | [optional] 
**e7010** | **str** | Een aanduiding die aangeeft dat gegevens wel of niet verstrekt mogen worden. ⦿ Groep: Geheim (70) ⦿ Element: Indicatie geheim (70.10) | [optional] 
**e7110** | **str** | De datum waarop de verificatie van gegevens op de PL in de RNI heeft plaatsgevonden. ⦿ Groep: Verificatie (71) ⦿ Element: Datum verificatie (71.10) | [optional] 
**e7120** | **str** | De omschrijving op welke wijze de verificatie van gegevens op de PL in de RNI heeft plaatsgevonden. ⦿ Groep: Verificatie (71) ⦿ Element: Omschrijving verificatie (71.20) | [optional] 
**e8010** | **str** | Een nummer waarmee de versie van de PL aangegeven wordt. ⦿ Groep: Synchroniciteit (80) ⦿ Element: Versienummer (80.10) | [optional] 
**e8020** | **str** | Dit is de datum en tijd waarop de laatste wijziging of de eerste inschrijving van de PL heeft plaatsgevonden. De op te nemen tijd is Greenwich Mean Time (GMT). ⦿ Groep: Synchroniciteit (80) ⦿ Element: Datumtijdstempel (80.20) | [optional] 
**e8710** | **str** | Een aanduiding dat gegevens over alle kinderen van de PK zijn opgenomen in de BRP. ⦿ Groep: PK-conversie (87) ⦿ Element: PK-gegevens volledig meegeconverteerd (87.10) | [optional] 
**e8810** | **str** | Een code, voorkomend in Tabel 60, RNI-deelnemerstabel, die aangeeft welke RNI-deelnemer (een deel van) de gegevens in de betrokken categorie heeft aangeleverd. ⦿ Groep: RNI-deelnemer (88) ⦿ Element: RNI-deelnemer (88.10) | [optional] 
**e8820** | **str** | Een aanduiding van het verdrag op basis waarvan (een deel van) de gegevens in de betrokken categorie door een buitenlandse zusterorganisatie van een RNI-deelnemer aan die deelnemer zijn aangeleverd. ⦿ Groep: RNI-deelnemer (88) ⦿ Element: Omschrijving verdrag (88.20) | [optional] 
**historie** | [**List[Af01PlDataC07InnerAllOfHistorieInner]**](Af01PlDataC07InnerAllOfHistorieInner.md) |  | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c07_inner import Af01PlDataC07Inner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC07Inner from a JSON string
af01_pl_data_c07_inner_instance = Af01PlDataC07Inner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC07Inner.to_json())

# convert the object into a dict
af01_pl_data_c07_inner_dict = af01_pl_data_c07_inner_instance.to_dict()
# create an instance of Af01PlDataC07Inner from a dict
af01_pl_data_c07_inner_from_dict = Af01PlDataC07Inner.from_dict(af01_pl_data_c07_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


