# PutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bericht_kenmerken** | [**PutMessageKenmerken**](PutMessageKenmerken.md) |  | 
**bericht_inhoud** | [**LoBericht**](LoBericht.md) |  | 

## Example

```python
from berichten_api.models.put_message import PutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PutMessage from a JSON string
put_message_instance = PutMessage.from_json(json)
# print the JSON string representation of the object
print(PutMessage.to_json())

# convert the object into a dict
put_message_dict = put_message_instance.to_dict()
# create an instance of PutMessage from a dict
put_message_from_dict = PutMessage.from_dict(put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


