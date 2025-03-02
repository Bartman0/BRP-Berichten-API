# GetMessageAntwoord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interactie_id** | **str** | Een uniek ID wat aan het HTTP request gekoppeld wordt. | 
**opgehaalde_berichten** | [**List[GetMessageAntwoordAllOfOpgehaaldeBerichten]**](GetMessageAntwoordAllOfOpgehaaldeBerichten.md) | Gevraagde berichten die ook succesvol opgehaald konden worden. | 
**niet_opgehaalde_berichten** | [**List[GetMessageAntwoordAllOfNietOpgehaaldeBerichten]**](GetMessageAntwoordAllOfNietOpgehaaldeBerichten.md) | Gevraagde berichten die niet succesvol opgehaald konden worden. | 

## Example

```python
from berichten_api.models.get_message_antwoord import GetMessageAntwoord

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageAntwoord from a JSON string
get_message_antwoord_instance = GetMessageAntwoord.from_json(json)
# print the JSON string representation of the object
print(GetMessageAntwoord.to_json())

# convert the object into a dict
get_message_antwoord_dict = get_message_antwoord_instance.to_dict()
# create an instance of GetMessageAntwoord from a dict
get_message_antwoord_from_dict = GetMessageAntwoord.from_dict(get_message_antwoord_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


