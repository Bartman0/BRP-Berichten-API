# BBADELETEF004

Het aantal berichten dat in dit verzoek verwijderd dient te worden overschrijft het ingestelde limiet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | DELETEREQUEST_REQUESTED_NUMBER_OF_MESSAGES_EXCEEDS_LIMIT | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-DELETE-F004 | 
**detail** | **str** | Het aantal berichten dat in dit verzoek verwijderd dient te worden overschrijft het ingestelde limiet | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbadeletef004 import BBADELETEF004

# TODO update the JSON string below
json = "{}"
# create an instance of BBADELETEF004 from a JSON string
bbadeletef004_instance = BBADELETEF004.from_json(json)
# print the JSON string representation of the object
print(BBADELETEF004.to_json())

# convert the object into a dict
bbadeletef004_dict = bbadeletef004_instance.to_dict()
# create an instance of BBADELETEF004 from a dict
bbadeletef004_from_dict = BBADELETEF004.from_dict(bbadeletef004_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


