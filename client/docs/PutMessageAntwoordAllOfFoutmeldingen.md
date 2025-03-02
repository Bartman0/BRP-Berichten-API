# PutMessageAntwoordAllOfFoutmeldingen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | PUTREQUEST_SENDER_ACCOUNT_NOT_AVAILABLE | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-PUT-F004 | 
**detail** | **str** | Het bericht kon niet verzonden worden, uw account is niet beschikbaar | 
**date_time** | **datetime** |  | [optional] 
**invalid_parameters** | [**List[InvalidParametersInner]**](InvalidParametersInner.md) |  | 

## Example

```python
from berichten_api.models.put_message_antwoord_all_of_foutmeldingen import PutMessageAntwoordAllOfFoutmeldingen

# TODO update the JSON string below
json = "{}"
# create an instance of PutMessageAntwoordAllOfFoutmeldingen from a JSON string
put_message_antwoord_all_of_foutmeldingen_instance = PutMessageAntwoordAllOfFoutmeldingen.from_json(json)
# print the JSON string representation of the object
print(PutMessageAntwoordAllOfFoutmeldingen.to_json())

# convert the object into a dict
put_message_antwoord_all_of_foutmeldingen_dict = put_message_antwoord_all_of_foutmeldingen_instance.to_dict()
# create an instance of PutMessageAntwoordAllOfFoutmeldingen from a dict
put_message_antwoord_all_of_foutmeldingen_from_dict = PutMessageAntwoordAllOfFoutmeldingen.from_dict(put_message_antwoord_all_of_foutmeldingen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


