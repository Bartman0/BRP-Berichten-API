# BBALISTF001

Ongeldige zoekfilters opgegeven

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | LIST_MESSAGE_REQUEST_INVALID_PARAMETERS | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-LIST-F001 | 
**detail** | **str** | Ongeldige zoekfilters opgegeven | 
**date_time** | **datetime** |  | [optional] 
**invalid_parameters** | [**List[InvalidParametersInner]**](InvalidParametersInner.md) |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbalistf001 import BBALISTF001

# TODO update the JSON string below
json = "{}"
# create an instance of BBALISTF001 from a JSON string
bbalistf001_instance = BBALISTF001.from_json(json)
# print the JSON string representation of the object
print(BBALISTF001.to_json())

# convert the object into a dict
bbalistf001_dict = bbalistf001_instance.to_dict()
# create an instance of BBALISTF001 from a dict
bbalistf001_from_dict = BBALISTF001.from_dict(bbalistf001_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


