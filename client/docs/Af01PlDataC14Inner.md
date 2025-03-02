# Af01PlDataC14Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e4010** | **str** | Een code, opgenomen in Tabel 35, Autorisatietabel, die het nummer aangeeft dat door RvIG wordt toegekend aan een geautoriseerde afnemer of derde die recht heeft op verstrekking van spontane mutaties. ⦿ Groep: Afnemer (40) ⦿ Element: Afnemersindicatie (40.10) | [optional] 
**e8510** | **str** | De datum waarop het geheel van gegevens geldig is geworden. ⦿ Groep: Geldigheid (85) ⦿ Element: Ingangsdatum geldigheid (85.10) | [optional] 
**historie** | [**List[Af01PlDataC14InnerAllOfHistorieInner]**](Af01PlDataC14InnerAllOfHistorieInner.md) |  | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c14_inner import Af01PlDataC14Inner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC14Inner from a JSON string
af01_pl_data_c14_inner_instance = Af01PlDataC14Inner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC14Inner.to_json())

# convert the object into a dict
af01_pl_data_c14_inner_dict = af01_pl_data_c14_inner_instance.to_dict()
# create an instance of Af01PlDataC14Inner from a dict
af01_pl_data_c14_inner_from_dict = Af01PlDataC14Inner.from_dict(af01_pl_data_c14_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


