# DeleteMessageAntwoordAllOfFoutmeldingen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | DELETEREQUEST_MESSAGE_NOT_FOUND | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-DELETE-F003 | 
**detail** | **str** | Onbekend berichtTransportId | 
**date_time** | **datetime** |  | [optional] 

## Example

```python
from berichten_api.models.delete_message_antwoord_all_of_foutmeldingen import DeleteMessageAntwoordAllOfFoutmeldingen

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMessageAntwoordAllOfFoutmeldingen from a JSON string
delete_message_antwoord_all_of_foutmeldingen_instance = DeleteMessageAntwoordAllOfFoutmeldingen.from_json(json)
# print the JSON string representation of the object
print(DeleteMessageAntwoordAllOfFoutmeldingen.to_json())

# convert the object into a dict
delete_message_antwoord_all_of_foutmeldingen_dict = delete_message_antwoord_all_of_foutmeldingen_instance.to_dict()
# create an instance of DeleteMessageAntwoordAllOfFoutmeldingen from a dict
delete_message_antwoord_all_of_foutmeldingen_from_dict = DeleteMessageAntwoordAllOfFoutmeldingen.from_dict(delete_message_antwoord_all_of_foutmeldingen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


