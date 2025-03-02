# BBAGETF004

Het aantal opgevraagde berichten overschreed het ingestelde limiet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | GETREQUEST_REQUESTED_NUMBER_OF_MESSAGES_EXCEEDS_LIMIT | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-GET-F004 | 
**detail** | **str** | Het aantal opgevraagde berichten overschreed het ingestelde limiet | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbagetf004 import BBAGETF004

# TODO update the JSON string below
json = "{}"
# create an instance of BBAGETF004 from a JSON string
bbagetf004_instance = BBAGETF004.from_json(json)
# print the JSON string representation of the object
print(BBAGETF004.to_json())

# convert the object into a dict
bbagetf004_dict = bbagetf004_instance.to_dict()
# create an instance of BBAGETF004 from a dict
bbagetf004_from_dict = BBAGETF004.from_dict(bbagetf004_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


