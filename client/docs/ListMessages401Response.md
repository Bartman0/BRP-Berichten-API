# ListMessages401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | TECHNICAL_ERROR | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-F999 | 
**detail** | **str** | Onbekende (/technische) fout. | 
**status** | **int** | 401 | 
**date_time** | **datetime** |  | [optional] 
**instance** | **str** | Dit (RFC7807) veld beschrijft het request waarbij dit probleem is opgetreden (indien van toepassing). | [optional] 

## Example

```python
from berichten_api.models.list_messages401_response import ListMessages401Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMessages401Response from a JSON string
list_messages401_response_instance = ListMessages401Response.from_json(json)
# print the JSON string representation of the object
print(ListMessages401Response.to_json())

# convert the object into a dict
list_messages401_response_dict = list_messages401_response_instance.to_dict()
# create an instance of ListMessages401Response from a dict
list_messages401_response_from_dict = ListMessages401Response.from_dict(list_messages401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


