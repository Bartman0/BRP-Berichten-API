# Summarize200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interactie_id** | **str** | Een uniek ID wat aan het HTTP request gekoppeld wordt. | 
**aantal_berichten** | **int** | Het aantal berichten dat voldeed aan de criteria. | 

## Example

```python
from berichten_api.models.summarize200_response import Summarize200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Summarize200Response from a JSON string
summarize200_response_instance = Summarize200Response.from_json(json)
# print the JSON string representation of the object
print(Summarize200Response.to_json())

# convert the object into a dict
summarize200_response_dict = summarize200_response_instance.to_dict()
# create an instance of Summarize200Response from a dict
summarize200_response_from_dict = Summarize200Response.from_dict(summarize200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


