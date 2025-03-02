# Converteer415Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Ongeldig bronformaat aangevraagd in &#39;Content-Type&#39; header | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-CONV-F003 | 
**detail** | **str** | Kon bronformaat niet bepalen a.d.h.v. Content-type header [content-type]. | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.converteer415_response import Converteer415Response

# TODO update the JSON string below
json = "{}"
# create an instance of Converteer415Response from a JSON string
converteer415_response_instance = Converteer415Response.from_json(json)
# print the JSON string representation of the object
print(Converteer415Response.to_json())

# convert the object into a dict
converteer415_response_dict = converteer415_response_instance.to_dict()
# create an instance of Converteer415Response from a dict
converteer415_response_from_dict = Converteer415Response.from_dict(converteer415_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


