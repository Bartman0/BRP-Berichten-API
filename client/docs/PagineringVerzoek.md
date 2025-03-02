# PagineringVerzoek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagina** | **int** |  | 

## Example

```python
from berichten_api.models.paginering_verzoek import PagineringVerzoek

# TODO update the JSON string below
json = "{}"
# create an instance of PagineringVerzoek from a JSON string
paginering_verzoek_instance = PagineringVerzoek.from_json(json)
# print the JSON string representation of the object
print(PagineringVerzoek.to_json())

# convert the object into a dict
paginering_verzoek_dict = paginering_verzoek_instance.to_dict()
# create an instance of PagineringVerzoek from a dict
paginering_verzoek_from_dict = PagineringVerzoek.from_dict(paginering_verzoek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


