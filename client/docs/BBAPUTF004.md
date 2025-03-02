# BBAPUTF004

Het bericht kon niet verzonden worden, uw account is niet beschikbaar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | PUTREQUEST_SENDER_ACCOUNT_NOT_AVAILABLE | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-PUT-F004 | 
**detail** | **str** | Het bericht kon niet verzonden worden, uw account is niet beschikbaar | 
**date_time** | **datetime** |  | [optional] 

## Example

```python
from berichten_api.models.bbaputf004 import BBAPUTF004

# TODO update the JSON string below
json = "{}"
# create an instance of BBAPUTF004 from a JSON string
bbaputf004_instance = BBAPUTF004.from_json(json)
# print the JSON string representation of the object
print(BBAPUTF004.to_json())

# convert the object into a dict
bbaputf004_dict = bbaputf004_instance.to_dict()
# create an instance of BBAPUTF004 from a dict
bbaputf004_from_dict = BBAPUTF004.from_dict(bbaputf004_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


