# PutMessageAntwoordAllOfVerwerkteBerichten


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ontvanger** | **int** |  | [optional] 
**bericht_id** | **str** | Het unieke volgnummer dat aan het uitgaande bericht wordt toegekend door de afzender. De \&quot;BRP berichten API\&quot; voert geen inhoudelijke controles uit op dit BerichtId. Maximaal 12 posities.  | 
**bericht_transport_id** | **str** | De is de referentie naar het bericht zoals deze bekend is bij de &#x60;BRP berichten API&#x60; (UUID). Bij elke interactie met deze dienst omtrent een bericht, wordt deze waarde gebruikt. Het mag, net zoals &#x60;berichtVolgnummer&#x60; gebruikt worden om het bericht uniek te identificeren. | 

## Example

```python
from berichten_api.models.put_message_antwoord_all_of_verwerkte_berichten import PutMessageAntwoordAllOfVerwerkteBerichten

# TODO update the JSON string below
json = "{}"
# create an instance of PutMessageAntwoordAllOfVerwerkteBerichten from a JSON string
put_message_antwoord_all_of_verwerkte_berichten_instance = PutMessageAntwoordAllOfVerwerkteBerichten.from_json(json)
# print the JSON string representation of the object
print(PutMessageAntwoordAllOfVerwerkteBerichten.to_json())

# convert the object into a dict
put_message_antwoord_all_of_verwerkte_berichten_dict = put_message_antwoord_all_of_verwerkte_berichten_instance.to_dict()
# create an instance of PutMessageAntwoordAllOfVerwerkteBerichten from a dict
put_message_antwoord_all_of_verwerkte_berichten_from_dict = PutMessageAntwoordAllOfVerwerkteBerichten.from_dict(put_message_antwoord_all_of_verwerkte_berichten_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


