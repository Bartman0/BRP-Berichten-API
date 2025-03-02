# DeleteMessageAntwoord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interactie_id** | **str** | Een uniek ID wat aan het HTTP request gekoppeld wordt. | 
**succesvol_verwijderde_berichten** | **List[str]** | In deze collectie staan de berichten die daadwerkelijk verwijderd zijn. | [optional] 
**niet_succesvol_verwijderde_berichten** | [**List[DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten]**](DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten.md) | In deze collectie staan de berichten die niet verwijderd konden worden. | [optional] 

## Example

```python
from berichten_api.models.delete_message_antwoord import DeleteMessageAntwoord

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMessageAntwoord from a JSON string
delete_message_antwoord_instance = DeleteMessageAntwoord.from_json(json)
# print the JSON string representation of the object
print(DeleteMessageAntwoord.to_json())

# convert the object into a dict
delete_message_antwoord_dict = delete_message_antwoord_instance.to_dict()
# create an instance of DeleteMessageAntwoord from a dict
delete_message_antwoord_from_dict = DeleteMessageAntwoord.from_dict(delete_message_antwoord_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


