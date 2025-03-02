# Af01PlDataC17Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e1610** | **str** | Het telefoonnummer waarop betrokkene bereikbaar is. ⦿ Groep: Telefoon (16) ⦿ Element: Telefoonnummer (16.10) | [optional] 
**e1620** | **str** | Een aanduiding die aangeeft of is vastgesteld dat het een geldig telefoonnummer is en of is vastgesteld dat de betrokken persoon via dit telefoonnummer kan worden bereikt. ⦿ Groep: Telefoon (16) ⦿ Element: Verificatie-indicatie (16.20) | [optional] 
**e1630** | **str** | De datum waarop dit telefoonnummer is geregistreerd. ⦿ Groep: Telefoon (16) ⦿ Element: Geldig vanaf (16.30) | [optional] 
**e1710** | **str** | Het e-mailadres waarop betrokkene bereikbaar is. ⦿ Groep: E-mailadres (17) ⦿ Element: E-mailadres (17.10) | [optional] 
**e1720** | **str** | Een aanduiding die aangeeft of is vastgesteld dat het een geldig e-mailadres is en of is vastgesteld dat de betrokken persoon via dit e-mailadres kan worden bereikt. ⦿ Groep: E-mailadres (17) ⦿ Element: Verificatie-indicatie (17.20) | [optional] 
**e1730** | **str** | De datum waarop dit e-mailadres is geregistreerd. ⦿ Groep: E-mailadres (17) ⦿ Element: Geldig vanaf (17.30) | [optional] 
**e8810** | **str** | Een code, voorkomend in Tabel 60, RNI-deelnemerstabel, die aangeeft welke RNI-deelnemer (een deel van) de gegevens in de betrokken categorie heeft aangeleverd. ⦿ Groep: RNI-deelnemer (88) ⦿ Element: RNI-deelnemer (88.10) | [optional] 
**e8820** | **str** | Een aanduiding van het verdrag op basis waarvan (een deel van) de gegevens in de betrokken categorie door een buitenlandse zusterorganisatie van een RNI-deelnemer aan die deelnemer zijn aangeleverd. ⦿ Groep: RNI-deelnemer (88) ⦿ Element: Omschrijving verdrag (88.20) | [optional] 
**historie** | [**List[Af01PlDataC17InnerAllOfHistorieInner]**](Af01PlDataC17InnerAllOfHistorieInner.md) |  | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c17_inner import Af01PlDataC17Inner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC17Inner from a JSON string
af01_pl_data_c17_inner_instance = Af01PlDataC17Inner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC17Inner.to_json())

# convert the object into a dict
af01_pl_data_c17_inner_dict = af01_pl_data_c17_inner_instance.to_dict()
# create an instance of Af01PlDataC17Inner from a dict
af01_pl_data_c17_inner_from_dict = Af01PlDataC17Inner.from_dict(af01_pl_data_c17_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


