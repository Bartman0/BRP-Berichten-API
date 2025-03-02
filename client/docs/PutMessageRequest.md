# PutMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**berichten** | [**List[PutMessage]**](PutMessage.md) |  | 

## Example

```python
from berichten_api.models.put_message_request import PutMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutMessageRequest from a JSON string
put_message_request_instance = PutMessageRequest.from_json(json)
# print the JSON string representation of the object
print(PutMessageRequest.to_json())

# convert the object into a dict
put_message_request_dict = put_message_request_instance.to_dict()
# create an instance of PutMessageRequest from a dict
put_message_request_from_dict = PutMessageRequest.from_dict(put_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


