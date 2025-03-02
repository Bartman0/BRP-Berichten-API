# BBAGETF003

Onbekend berichtTransportId

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | GETREQUEST_MESSAGE_NOT_FOUND | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-GET-F003 | 
**detail** | **str** | Onbekend berichtTransportId | 
**date_time** | **datetime** |  | [optional] 

## Example

```python
from berichten_api.models.bbagetf003 import BBAGETF003

# TODO update the JSON string below
json = "{}"
# create an instance of BBAGETF003 from a JSON string
bbagetf003_instance = BBAGETF003.from_json(json)
# print the JSON string representation of the object
print(BBAGETF003.to_json())

# convert the object into a dict
bbagetf003_dict = bbagetf003_instance.to_dict()
# create an instance of BBAGETF003 from a dict
bbagetf003_from_dict = BBAGETF003.from_dict(bbagetf003_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


