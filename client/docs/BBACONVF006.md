# BBACONVF006

Inputbericht is niet valide

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Inputbericht is niet valide | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-CONV-F006 | 
**detail** | **str** | Het aangeleverde bericht kon niet ingenomen worden en voldoet waarschijnlijk niet aan de gestelde vereisten, foutmelding was: [foutmelding] | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.bbaconvf006 import BBACONVF006

# TODO update the JSON string below
json = "{}"
# create an instance of BBACONVF006 from a JSON string
bbaconvf006_instance = BBACONVF006.from_json(json)
# print the JSON string representation of the object
print(BBACONVF006.to_json())

# convert the object into a dict
bbaconvf006_dict = bbaconvf006_instance.to_dict()
# create an instance of BBACONVF006 from a dict
bbaconvf006_from_dict = BBACONVF006.from_dict(bbaconvf006_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


