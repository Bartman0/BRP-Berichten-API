# BBAF999

Onbekende (/technische) fout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | TECHNICAL_ERROR | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-F999 | 
**detail** | **str** | Onbekende (/technische) fout. | [optional] 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbaf999 import BBAF999

# TODO update the JSON string below
json = "{}"
# create an instance of BBAF999 from a JSON string
bbaf999_instance = BBAF999.from_json(json)
# print the JSON string representation of the object
print(BBAF999.to_json())

# convert the object into a dict
bbaf999_dict = bbaf999_instance.to_dict()
# create an instance of BBAF999 from a dict
bbaf999_from_dict = BBAF999.from_dict(bbaf999_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


