# BBAGETF002

Het bericht is niet langer beschikbaar omdat het verwijderd is.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | GETREQUEST_MESSAGE_CONTENT_DELETED | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-GET-F002 | 
**detail** | **str** | Het bericht is niet langer beschikbaar omdat het verwijderd is. | 
**date_time** | **datetime** |  | [optional] 

## Example

```python
from berichten_api.models.bbagetf002 import BBAGETF002

# TODO update the JSON string below
json = "{}"
# create an instance of BBAGETF002 from a JSON string
bbagetf002_instance = BBAGETF002.from_json(json)
# print the JSON string representation of the object
print(BBAGETF002.to_json())

# convert the object into a dict
bbagetf002_dict = bbagetf002_instance.to_dict()
# create an instance of BBAGETF002 from a dict
bbagetf002_from_dict = BBAGETF002.from_dict(bbagetf002_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


