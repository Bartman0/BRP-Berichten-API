# BBADELETEF003

Onbekend berichtTransportId

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | DELETEREQUEST_MESSAGE_NOT_FOUND | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-DELETE-F003 | 
**detail** | **str** | Onbekend berichtTransportId | 
**date_time** | **datetime** |  | [optional] 

## Example

```python
from berichten_api.models.bbadeletef003 import BBADELETEF003

# TODO update the JSON string below
json = "{}"
# create an instance of BBADELETEF003 from a JSON string
bbadeletef003_instance = BBADELETEF003.from_json(json)
# print the JSON string representation of the object
print(BBADELETEF003.to_json())

# convert the object into a dict
bbadeletef003_dict = bbadeletef003_instance.to_dict()
# create an instance of BBADELETEF003 from a dict
bbadeletef003_from_dict = BBADELETEF003.from_dict(bbadeletef003_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


