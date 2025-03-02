# BBAAUTHF001

Onjuiste of onbekende authenticatie.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Authenticatiefout | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-AUTH-F001 | 
**detail** | **str** | Onjuiste of onbekende authenticatie. | 
**status** | **int** | 401 | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbaauthf001 import BBAAUTHF001

# TODO update the JSON string below
json = "{}"
# create an instance of BBAAUTHF001 from a JSON string
bbaauthf001_instance = BBAAUTHF001.from_json(json)
# print the JSON string representation of the object
print(BBAAUTHF001.to_json())

# convert the object into a dict
bbaauthf001_dict = bbaauthf001_instance.to_dict()
# create an instance of BBAAUTHF001 from a dict
bbaauthf001_from_dict = BBAAUTHF001.from_dict(bbaauthf001_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


