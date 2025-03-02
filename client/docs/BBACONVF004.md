# BBACONVF004

Accept header niet aanwezig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Accept header niet aanwezig | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-CONV-F004 | 
**detail** | **str** | Er is geen &#39;Accept:&#39; header meegegeven waardoor niet bepaald kon worden welk doelformaat er gevraagd is. | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbaconvf004 import BBACONVF004

# TODO update the JSON string below
json = "{}"
# create an instance of BBACONVF004 from a JSON string
bbaconvf004_instance = BBACONVF004.from_json(json)
# print the JSON string representation of the object
print(BBACONVF004.to_json())

# convert the object into a dict
bbaconvf004_dict = bbaconvf004_instance.to_dict()
# create an instance of BBACONVF004 from a dict
bbaconvf004_from_dict = BBACONVF004.from_dict(bbaconvf004_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


