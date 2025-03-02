# BBAGETF001

Het bericht is niet langer beschikbaar omdat de retentietijd verstreken is.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | GETREQUEST_MESSAGE_CONTENT_EXPIRED | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-GET-F001 | 
**detail** | **str** | Het bericht is niet langer beschikbaar omdat de retentietijd verstreken is. | 
**date_time** | **datetime** |  | [optional] 

## Example

```python
from berichten_api.models.bbagetf001 import BBAGETF001

# TODO update the JSON string below
json = "{}"
# create an instance of BBAGETF001 from a JSON string
bbagetf001_instance = BBAGETF001.from_json(json)
# print the JSON string representation of the object
print(BBAGETF001.to_json())

# convert the object into a dict
bbagetf001_dict = bbagetf001_instance.to_dict()
# create an instance of BBAGETF001 from a dict
bbagetf001_from_dict = BBAGETF001.from_dict(bbagetf001_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


