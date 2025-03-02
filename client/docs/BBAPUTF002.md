# BBAPUTF002

Een of meerdere velden in het bericht voldoen niet aan de gestelde eisen

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | PUTREQUEST_INVALID_FIELD_ERROR | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-PUT-F002 | 
**detail** | **str** | Een of meerdere velden in het bericht voldoen niet aan de gestelde eisen | 
**date_time** | **datetime** |  | [optional] 
**invalid_parameters** | [**List[InvalidParametersInner]**](InvalidParametersInner.md) |  | 

## Example

```python
from berichten_api.models.bbaputf002 import BBAPUTF002

# TODO update the JSON string below
json = "{}"
# create an instance of BBAPUTF002 from a JSON string
bbaputf002_instance = BBAPUTF002.from_json(json)
# print the JSON string representation of the object
print(BBAPUTF002.to_json())

# convert the object into a dict
bbaputf002_dict = bbaputf002_instance.to_dict()
# create an instance of BBAPUTF002 from a dict
bbaputf002_from_dict = BBAPUTF002.from_dict(bbaputf002_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


