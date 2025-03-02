# PagineringResultaat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paginering_verzoek** | [**PagineringVerzoek**](PagineringVerzoek.md) |  | 
**totaal_aantal_berichten** | **int** |  | [default to 0]
**aantal_berichten_op_deze_pagina** | **int** |  | [default to 2000]
**aantal_paginas** | **int** |  | [default to 3]
**huidige_pagina** | **int** |  | 
**eerste_pagina** | **bool** |  | 
**laatste_pagina** | **bool** |  | 

## Example

```python
from berichten_api.models.paginering_resultaat import PagineringResultaat

# TODO update the JSON string below
json = "{}"
# create an instance of PagineringResultaat from a JSON string
paginering_resultaat_instance = PagineringResultaat.from_json(json)
# print the JSON string representation of the object
print(PagineringResultaat.to_json())

# convert the object into a dict
paginering_resultaat_dict = paginering_resultaat_instance.to_dict()
# create an instance of PagineringResultaat from a dict
paginering_resultaat_from_dict = PagineringResultaat.from_dict(paginering_resultaat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


