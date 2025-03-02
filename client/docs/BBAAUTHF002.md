# BBAAUTHF002

Het account is geblokkeerd.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Authenticatiefout | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-AUTH-F002 | 
**detail** | **str** | Het account is geblokkeerd. | 
**status** | **int** | 401 | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbaauthf002 import BBAAUTHF002

# TODO update the JSON string below
json = "{}"
# create an instance of BBAAUTHF002 from a JSON string
bbaauthf002_instance = BBAAUTHF002.from_json(json)
# print the JSON string representation of the object
print(BBAAUTHF002.to_json())

# convert the object into a dict
bbaauthf002_dict = bbaauthf002_instance.to_dict()
# create an instance of BBAAUTHF002 from a dict
bbaauthf002_from_dict = BBAAUTHF002.from_dict(bbaauthf002_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


