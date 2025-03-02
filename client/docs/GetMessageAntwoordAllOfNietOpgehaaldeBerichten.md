# GetMessageAntwoordAllOfNietOpgehaaldeBerichten


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bericht_transport_id** | **str** | De is de referentie naar het bericht zoals deze bekend is bij de &#x60;BRP berichten API&#x60; (UUID). Bij elke interactie met deze dienst omtrent een bericht, wordt deze waarde gebruikt. Het mag, net zoals &#x60;berichtVolgnummer&#x60; gebruikt worden om het bericht uniek te identificeren. | 
**foutmeldingen** | [**List[GetMessageAntwoordAllOfFoutmeldingen]**](GetMessageAntwoordAllOfFoutmeldingen.md) |  | 

## Example

```python
from berichten_api.models.get_message_antwoord_all_of_niet_opgehaalde_berichten import GetMessageAntwoordAllOfNietOpgehaaldeBerichten

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageAntwoordAllOfNietOpgehaaldeBerichten from a JSON string
get_message_antwoord_all_of_niet_opgehaalde_berichten_instance = GetMessageAntwoordAllOfNietOpgehaaldeBerichten.from_json(json)
# print the JSON string representation of the object
print(GetMessageAntwoordAllOfNietOpgehaaldeBerichten.to_json())

# convert the object into a dict
get_message_antwoord_all_of_niet_opgehaalde_berichten_dict = get_message_antwoord_all_of_niet_opgehaalde_berichten_instance.to_dict()
# create an instance of GetMessageAntwoordAllOfNietOpgehaaldeBerichten from a dict
get_message_antwoord_all_of_niet_opgehaalde_berichten_from_dict = GetMessageAntwoordAllOfNietOpgehaaldeBerichten.from_dict(get_message_antwoord_all_of_niet_opgehaalde_berichten_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


