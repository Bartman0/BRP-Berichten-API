# DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten

De foutmelding welke aangeeft waarom een bericht niet verwijderd kon worden.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bericht_transport_id** | **str** | De is de referentie naar het bericht zoals deze bekend is bij de &#x60;BRP berichten API&#x60; (UUID). Bij elke interactie met deze dienst omtrent een bericht, wordt deze waarde gebruikt. Het mag, net zoals &#x60;berichtVolgnummer&#x60; gebruikt worden om het bericht uniek te identificeren. | 
**foutmeldingen** | [**List[DeleteMessageAntwoordAllOfFoutmeldingen]**](DeleteMessageAntwoordAllOfFoutmeldingen.md) |  | 

## Example

```python
from berichten_api.models.delete_message_antwoord_all_of_niet_succesvol_verwijderde_berichten import DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten from a JSON string
delete_message_antwoord_all_of_niet_succesvol_verwijderde_berichten_instance = DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten.from_json(json)
# print the JSON string representation of the object
print(DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten.to_json())

# convert the object into a dict
delete_message_antwoord_all_of_niet_succesvol_verwijderde_berichten_dict = delete_message_antwoord_all_of_niet_succesvol_verwijderde_berichten_instance.to_dict()
# create an instance of DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten from a dict
delete_message_antwoord_all_of_niet_succesvol_verwijderde_berichten_from_dict = DeleteMessageAntwoordAllOfNietSuccesvolVerwijderdeBerichten.from_dict(delete_message_antwoord_all_of_niet_succesvol_verwijderde_berichten_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


