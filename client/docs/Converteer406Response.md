# Converteer406Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Ongeldig doelformaat aangevraagd in &#39;Accept&#39; header | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-CONV-F005 | 
**detail** | **str** | Kon doelformaat niet bepalen a.d.h.v. Accept header: [accept-header] | 
**invalid_parameters** | [**List[InvalidParametersInner]**](InvalidParametersInner.md) |  | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.converteer406_response import Converteer406Response

# TODO update the JSON string below
json = "{}"
# create an instance of Converteer406Response from a JSON string
converteer406_response_instance = Converteer406Response.from_json(json)
# print the JSON string representation of the object
print(Converteer406Response.to_json())

# convert the object into a dict
converteer406_response_dict = converteer406_response_instance.to_dict()
# create an instance of Converteer406Response from a dict
converteer406_response_from_dict = Converteer406Response.from_dict(converteer406_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


