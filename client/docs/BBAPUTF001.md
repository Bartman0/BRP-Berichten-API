# BBAPUTF001

Het aantal berichten in het verzoek overschrijd het ingestelde limiet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | PUTREQUEST_NUMBER_OF_MESSAGES_IN_REQUEST_EXCEEDS_LIMITS | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-PUT-F001 | 
**detail** | **str** | Het aantal berichten in het verzoek overschrijd het ingestelde limiet | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbaputf001 import BBAPUTF001

# TODO update the JSON string below
json = "{}"
# create an instance of BBAPUTF001 from a JSON string
bbaputf001_instance = BBAPUTF001.from_json(json)
# print the JSON string representation of the object
print(BBAPUTF001.to_json())

# convert the object into a dict
bbaputf001_dict = bbaputf001_instance.to_dict()
# create an instance of BBAPUTF001 from a dict
bbaputf001_from_dict = BBAPUTF001.from_dict(bbaputf001_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


