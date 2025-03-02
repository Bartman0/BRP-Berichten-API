# BBACONVF001

Bronformaat en doelformaat zijn gelijk aan elkaar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Bronformaat en doelformaat zijn gelijk aan elkaar | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-CONV-F001 | 
**detail** | **str** | bronformaat &#39;[bronformaat]&#39; is gelijk aan doelformaat &#39;[doelformaat]&#39; | 
**invalid_parameters** | [**List[InvalidParametersInner]**](InvalidParametersInner.md) |  | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbaconvf001 import BBACONVF001

# TODO update the JSON string below
json = "{}"
# create an instance of BBACONVF001 from a JSON string
bbaconvf001_instance = BBACONVF001.from_json(json)
# print the JSON string representation of the object
print(BBACONVF001.to_json())

# convert the object into a dict
bbaconvf001_dict = bbaconvf001_instance.to_dict()
# create an instance of BBACONVF001 from a dict
bbaconvf001_from_dict = BBACONVF001.from_dict(bbaconvf001_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


