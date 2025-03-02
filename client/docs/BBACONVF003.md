# BBACONVF003

Er is geen 'Content-Type:' header meegegeven waardoor niet bepaald kon worden welk bron formaat er geleverd is.

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
from berichten_api.models.bbaconvf003 import BBACONVF003

# TODO update the JSON string below
json = "{}"
# create an instance of BBACONVF003 from a JSON string
bbaconvf003_instance = BBACONVF003.from_json(json)
# print the JSON string representation of the object
print(BBACONVF003.to_json())

# convert the object into a dict
bbaconvf003_dict = bbaconvf003_instance.to_dict()
# create an instance of BBACONVF003 from a dict
bbaconvf003_from_dict = BBACONVF003.from_dict(bbaconvf003_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


