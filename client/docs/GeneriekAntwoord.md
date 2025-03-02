# GeneriekAntwoord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interactie_id** | **str** | Een uniek ID wat aan het HTTP request gekoppeld wordt. | 

## Example

```python
from berichten_api.models.generiek_antwoord import GeneriekAntwoord

# TODO update the JSON string below
json = "{}"
# create an instance of GeneriekAntwoord from a JSON string
generiek_antwoord_instance = GeneriekAntwoord.from_json(json)
# print the JSON string representation of the object
print(GeneriekAntwoord.to_json())

# convert the object into a dict
generiek_antwoord_dict = generiek_antwoord_instance.to_dict()
# create an instance of GeneriekAntwoord from a dict
generiek_antwoord_from_dict = GeneriekAntwoord.from_dict(generiek_antwoord_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


