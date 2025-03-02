# Converteer400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | TECHNICAL_ERROR | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-F999 | 
**detail** | **str** | Onbekende (/technische) fout. | 
**invalid_parameters** | [**List[InvalidParametersInner]**](InvalidParametersInner.md) |  | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.converteer400_response import Converteer400Response

# TODO update the JSON string below
json = "{}"
# create an instance of Converteer400Response from a JSON string
converteer400_response_instance = Converteer400Response.from_json(json)
# print the JSON string representation of the object
print(Converteer400Response.to_json())

# convert the object into a dict
converteer400_response_dict = converteer400_response_instance.to_dict()
# create an instance of Converteer400Response from a dict
converteer400_response_from_dict = Converteer400Response.from_dict(converteer400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


