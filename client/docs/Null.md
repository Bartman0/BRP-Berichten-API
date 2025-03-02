# Null

verwerkbevestiging (Null-bericht) - Bericht dat in bepaalde cycli wordt verstuurd ter bevestiging van de verwerking van de gegevens die opgenomen zijn in het eraan voorafgaande bericht in de cyclus.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**bericht_type** | **str** |  | 

## Example

```python
from berichten_api.models.null import Null

# TODO update the JSON string below
json = "{}"
# create an instance of Null from a JSON string
null_instance = Null.from_json(json)
# print the JSON string representation of the object
print(Null.to_json())

# convert the object into a dict
null_dict = null_instance.to_dict()
# create an instance of Null from a dict
null_from_dict = Null.from_dict(null_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


