# BBAPUTF003

Het bericht kon niet verzonden worden aan de geadresseerde

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | PUTREQUEST_MESSAGE_COULD_NOT_BE_SEND | 
**type** | **str** | https://www.rvig.nl/brp/berichten-api/probleem/BBA-PUT-F003 | 
**detail** | **str** | Het bericht kon niet verzonden worden aan de geadresseerde | 
**date_time** | **datetime** |  | [optional] 

## Example

```python
from berichten_api.models.bbaputf003 import BBAPUTF003

# TODO update the JSON string below
json = "{}"
# create an instance of BBAPUTF003 from a JSON string
bbaputf003_instance = BBAPUTF003.from_json(json)
# print the JSON string representation of the object
print(BBAPUTF003.to_json())

# convert the object into a dict
bbaputf003_dict = bbaputf003_instance.to_dict()
# create an instance of BBAPUTF003 from a dict
bbaputf003_from_dict = BBAPUTF003.from_dict(bbaputf003_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


