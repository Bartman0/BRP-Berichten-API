# Converteer200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bericht_inhoud** | [**LoBericht**](LoBericht.md) |  | [optional] 
**validatie_fouten** | [**List[Converteer200ResponseValidatieFoutenInner]**](Converteer200ResponseValidatieFoutenInner.md) |  | [optional] 

## Example

```python
from berichten_api.models.converteer200_response import Converteer200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Converteer200Response from a JSON string
converteer200_response_instance = Converteer200Response.from_json(json)
# print the JSON string representation of the object
print(Converteer200Response.to_json())

# convert the object into a dict
converteer200_response_dict = converteer200_response_instance.to_dict()
# create an instance of Converteer200Response from a dict
converteer200_response_from_dict = Converteer200Response.from_dict(converteer200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


