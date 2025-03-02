# Af01PlDataC15Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e4210** | **str** | Een uit vak 6 of vak 23 van de PK afkomstige afnemersaantekening. ⦿ Groep: Aantekening (42) ⦿ Element: Aantekening (42.10) | [optional] 
**historie** | [**List[Af01PlDataC15InnerAllOfHistorieInner]**](Af01PlDataC15InnerAllOfHistorieInner.md) |  | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c15_inner import Af01PlDataC15Inner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC15Inner from a JSON string
af01_pl_data_c15_inner_instance = Af01PlDataC15Inner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC15Inner.to_json())

# convert the object into a dict
af01_pl_data_c15_inner_dict = af01_pl_data_c15_inner_instance.to_dict()
# create an instance of Af01PlDataC15Inner from a dict
af01_pl_data_c15_inner_from_dict = Af01PlDataC15Inner.from_dict(af01_pl_data_c15_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


