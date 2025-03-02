# BBACONVF005

Ongeldig doelformaat aangevraagd in 'Accept' header

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Ongeldig doelformaat aangevraagd in &#39;Accept&#39; header | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-CONV-F005 | 
**detail** | **str** | Kon doelformaat niet bepalen a.d.h.v. Accept header: [accept-header] | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbaconvf005 import BBACONVF005

# TODO update the JSON string below
json = "{}"
# create an instance of BBACONVF005 from a JSON string
bbaconvf005_instance = BBACONVF005.from_json(json)
# print the JSON string representation of the object
print(BBACONVF005.to_json())

# convert the object into a dict
bbaconvf005_dict = bbaconvf005_instance.to_dict()
# create an instance of BBACONVF005 from a dict
bbaconvf005_from_dict = BBACONVF005.from_dict(bbaconvf005_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


