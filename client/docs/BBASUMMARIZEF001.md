# BBASUMMARIZEF001

Het verzoek is onjuist controleer de zoekparameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | SUMMARIZEREQUEST_INVALID_REQUEST_ERROR | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-SUMMARIZE-F001 | 
**detail** | **str** | Het verzoek is onjuist controleer de zoekparameters. | [optional] 
**date_time** | **datetime** |  | [optional] 
**invalid_parameters** | [**List[InvalidParametersInner]**](InvalidParametersInner.md) |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbasummarizef001 import BBASUMMARIZEF001

# TODO update the JSON string below
json = "{}"
# create an instance of BBASUMMARIZEF001 from a JSON string
bbasummarizef001_instance = BBASUMMARIZEF001.from_json(json)
# print the JSON string representation of the object
print(BBASUMMARIZEF001.to_json())

# convert the object into a dict
bbasummarizef001_dict = bbasummarizef001_instance.to_dict()
# create an instance of BBASUMMARIZEF001 from a dict
bbasummarizef001_from_dict = BBASUMMARIZEF001.from_dict(bbasummarizef001_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


