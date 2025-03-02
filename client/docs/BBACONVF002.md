# BBACONVF002

Content-Type header niet aanwezig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Content-Type header niet aanwezig | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-CONV-F002 | 
**detail** | **str** | Er is geen &#39;Content-Type:&#39; header meegegeven waardoor niet bepaald kon worden welk bron formaat er geleverd is. | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbaconvf002 import BBACONVF002

# TODO update the JSON string below
json = "{}"
# create an instance of BBACONVF002 from a JSON string
bbaconvf002_instance = BBACONVF002.from_json(json)
# print the JSON string representation of the object
print(BBACONVF002.to_json())

# convert the object into a dict
bbaconvf002_dict = bbaconvf002_instance.to_dict()
# create an instance of BBACONVF002 from a dict
bbaconvf002_from_dict = BBACONVF002.from_dict(bbaconvf002_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


