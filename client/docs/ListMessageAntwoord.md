# ListMessageAntwoord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interactie_id** | **str** | Een uniek ID wat aan het HTTP request gekoppeld wordt. | 
**paginering** | [**PagineringResultaat**](PagineringResultaat.md) |  | 
**berichten** | [**List[ListMessageKenmerken]**](ListMessageKenmerken.md) |  | 

## Example

```python
from berichten_api.models.list_message_antwoord import ListMessageAntwoord

# TODO update the JSON string below
json = "{}"
# create an instance of ListMessageAntwoord from a JSON string
list_message_antwoord_instance = ListMessageAntwoord.from_json(json)
# print the JSON string representation of the object
print(ListMessageAntwoord.to_json())

# convert the object into a dict
list_message_antwoord_dict = list_message_antwoord_instance.to_dict()
# create an instance of ListMessageAntwoord from a dict
list_message_antwoord_from_dict = ListMessageAntwoord.from_dict(list_message_antwoord_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


