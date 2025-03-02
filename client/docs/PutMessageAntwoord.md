# PutMessageAntwoord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interactie_id** | **str** | Een uniek ID wat aan het HTTP request gekoppeld wordt. | 
**verwerkte_berichten** | [**List[PutMessageAntwoordAllOfVerwerkteBerichten]**](PutMessageAntwoordAllOfVerwerkteBerichten.md) |  | 
**niet_verwerkte_berichten** | [**List[PutMessageAntwoordAllOfNietVerwerkteBerichten]**](PutMessageAntwoordAllOfNietVerwerkteBerichten.md) |  | 

## Example

```python
from berichten_api.models.put_message_antwoord import PutMessageAntwoord

# TODO update the JSON string below
json = "{}"
# create an instance of PutMessageAntwoord from a JSON string
put_message_antwoord_instance = PutMessageAntwoord.from_json(json)
# print the JSON string representation of the object
print(PutMessageAntwoord.to_json())

# convert the object into a dict
put_message_antwoord_dict = put_message_antwoord_instance.to_dict()
# create an instance of PutMessageAntwoord from a dict
put_message_antwoord_from_dict = PutMessageAntwoord.from_dict(put_message_antwoord_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


