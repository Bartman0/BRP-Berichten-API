# BBADELETEF001

Het bericht is niet langer beschikbaar omdat de retentietijd verstreken is.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | DELETEREQUEST_MESSAGE_EXPIRED | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-DELETE-F001 | 
**detail** | **str** | Het bericht is niet langer beschikbaar omdat de retentietijd verstreken is. | 
**date_time** | **datetime** |  | [optional] 

## Example

```python
from berichten_api.models.bbadeletef001 import BBADELETEF001

# TODO update the JSON string below
json = "{}"
# create an instance of BBADELETEF001 from a JSON string
bbadeletef001_instance = BBADELETEF001.from_json(json)
# print the JSON string representation of the object
print(BBADELETEF001.to_json())

# convert the object into a dict
bbadeletef001_dict = bbadeletef001_instance.to_dict()
# create an instance of BBADELETEF001 from a dict
bbadeletef001_from_dict = BBADELETEF001.from_dict(bbadeletef001_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


