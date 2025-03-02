# Af01PlData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**c01** | [**List[Af01PlDataC01Inner]**](Af01PlDataC01Inner.md) | Gegevens over de ingeschrevene | [optional] 
**c02** | [**List[Af01PlDataC02Inner]**](Af01PlDataC02Inner.md) | Gegevens over de ouder1 van de ingeschrevene. | [optional] 
**c03** | [**List[Af01PlDataC02Inner]**](Af01PlDataC02Inner.md) | Gegevens over de ouder2 van de ingeschrevene. | [optional] 
**c04** | [**List[Af01PlDataC04Inner]**](Af01PlDataC04Inner.md) | Gegevens over een nationaliteit van de ingeschrevene. | [optional] 
**c05** | [**List[Af01PlDataC05Inner]**](Af01PlDataC05Inner.md) | Gegevens over een gesloten of ontbonden huwelijk/geregistreerd partnerschap van de ingeschrevene. | [optional] 
**c06** | [**List[Af01PlDataC06Inner]**](Af01PlDataC06Inner.md) | Gegevens over het overlijden van de ingeschrevene. | [optional] 
**c07** | [**List[Af01PlDataC07Inner]**](Af01PlDataC07Inner.md) | Gegevens over de opneming en de status van de PL. | [optional] 
**c08** | [**List[Af01PlDataC08Inner]**](Af01PlDataC08Inner.md) | Gegevens over het verblijf en adres van de ingeschrevene. | [optional] 
**c09** | [**List[Af01PlDataC09Inner]**](Af01PlDataC09Inner.md) | Gegevens over een kind van de ingeschrevene. | [optional] 
**c10** | [**List[Af01PlDataC10Inner]**](Af01PlDataC10Inner.md) | Gegevens over de verblijfsrechtelijke status van de ingeschrevene. | [optional] 
**c11** | [**List[Af01PlDataC11Inner]**](Af01PlDataC11Inner.md) | Gegevens betreffende het gezag over de ingeschrevene. | [optional] 
**c12** | [**List[Af01PlDataC12Inner]**](Af01PlDataC12Inner.md) | Gegevens over een reisdocument van de ingeschrevene. | [optional] 
**c13** | [**List[Af01PlDataC13Inner]**](Af01PlDataC13Inner.md) | Gegevens over het kiesrecht van de ingeschrevene. | [optional] 
**c14** | [**List[Af01PlDataC14Inner]**](Af01PlDataC14Inner.md) | persoonslijst is wel of niet meer onderdeel van de doelgroep van een afnemer of derde. | [optional] 
**c15** | [**List[Af01PlDataC15Inner]**](Af01PlDataC15Inner.md) | Gegevens over een aantekening uit vak 6 of vak 23 van de PK van de ingeschrevene. | [optional] 
**c16** | [**List[Af01PlDataC16Inner]**](Af01PlDataC16Inner.md) | Adres waar betrokkene tijdelijk woont tijdens diens verblijf in Nederland. | [optional] 
**c17** | [**List[Af01PlDataC17Inner]**](Af01PlDataC17Inner.md) | Telefoonnummer en/of e-mailadres waarop betrokkene bereikbaar is tijdens diens verblijf in Nederland. | [optional] 
**c21** | [**List[Af01PlDataC21Inner]**](Af01PlDataC21Inner.md) | Telefoonnummer en/of e-mailadres waarop betrokkene bereikbaar is tijdens diens verblijf in Nederland. | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data import Af01PlData

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlData from a JSON string
af01_pl_data_instance = Af01PlData.from_json(json)
# print the JSON string representation of the object
print(Af01PlData.to_json())

# convert the object into a dict
af01_pl_data_dict = af01_pl_data_instance.to_dict()
# create an instance of Af01PlData from a dict
af01_pl_data_from_dict = Af01PlData.from_dict(af01_pl_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


