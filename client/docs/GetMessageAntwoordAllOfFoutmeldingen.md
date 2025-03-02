# GetMessageAntwoordAllOfFoutmeldingen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | GETREQUEST_MESSAGE_NOT_FOUND | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-GET-F003 | 
**detail** | **str** | Onbekend berichtTransportId | 
**date_time** | **datetime** |  | [optional] 

## Example

```python
from berichten_api.models.get_message_antwoord_all_of_foutmeldingen import GetMessageAntwoordAllOfFoutmeldingen

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageAntwoordAllOfFoutmeldingen from a JSON string
get_message_antwoord_all_of_foutmeldingen_instance = GetMessageAntwoordAllOfFoutmeldingen.from_json(json)
# print the JSON string representation of the object
print(GetMessageAntwoordAllOfFoutmeldingen.to_json())

# convert the object into a dict
get_message_antwoord_all_of_foutmeldingen_dict = get_message_antwoord_all_of_foutmeldingen_instance.to_dict()
# create an instance of GetMessageAntwoordAllOfFoutmeldingen from a dict
get_message_antwoord_all_of_foutmeldingen_from_dict = GetMessageAntwoordAllOfFoutmeldingen.from_dict(get_message_antwoord_all_of_foutmeldingen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


