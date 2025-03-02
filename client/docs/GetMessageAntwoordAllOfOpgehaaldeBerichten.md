# GetMessageAntwoordAllOfOpgehaaldeBerichten


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bericht_kenmerken** | [**GetMessageKenmerken**](GetMessageKenmerken.md) |  | 
**bericht_inhoud** | [**LoBericht**](LoBericht.md) |  | 

## Example

```python
from berichten_api.models.get_message_antwoord_all_of_opgehaalde_berichten import GetMessageAntwoordAllOfOpgehaaldeBerichten

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageAntwoordAllOfOpgehaaldeBerichten from a JSON string
get_message_antwoord_all_of_opgehaalde_berichten_instance = GetMessageAntwoordAllOfOpgehaaldeBerichten.from_json(json)
# print the JSON string representation of the object
print(GetMessageAntwoordAllOfOpgehaaldeBerichten.to_json())

# convert the object into a dict
get_message_antwoord_all_of_opgehaalde_berichten_dict = get_message_antwoord_all_of_opgehaalde_berichten_instance.to_dict()
# create an instance of GetMessageAntwoordAllOfOpgehaaldeBerichten from a dict
get_message_antwoord_all_of_opgehaalde_berichten_from_dict = GetMessageAntwoordAllOfOpgehaaldeBerichten.from_dict(get_message_antwoord_all_of_opgehaalde_berichten_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


