# Autorisatietabelregel

Een tabelregel voor Tabel 35 - autorisatietabel die de opsomming van de door de verantwoordelijk Minister geautoriseerde en aangesloten instanties binnen het BRP-stelsel bevat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e9510** | **str** |  | 
**e9511** | **List[str]** | Dit veld komt alleen in oude tabelregels voor (N-maal) | 
**e9512** | **str** | Numeriek: 0 &#x3D; geheimhouding niet van toepassing, 1 &#x3D; geheimhouding van toepassing | 
**e9513** | **str** | Numeriek: 0 &#x3D; geen beperking, 1 &#x3D; gevoelig, 2 &#x3D; geheim | 
**e9514** | **str** | Numeriek: 0 &#x3D; niet verstrekken, 1 &#x3D; verstrekken | 
**e9520** | **str** |  | 
**e9540** | **List[str]** | Numeriek (N maal) | 
**e9541** | **str** |  | 
**e9542** | **List[str]** | Numeriek (N maal) | 
**e9543** | **str** | 0 &#x3D; plaatsen afnemersindicatie, 1 &#x3D; conditionele gegevensverstrekking | 
**e9544** | **str** | N &#x3D; Berichtendienst, A &#x3D; alternatief medium | 
**e9550** | **List[str]** | Numeriek (N maal) | 
**e9551** | **str** |  | 
**e9552** | **str** | Numeriek: 0 &#x3D; niet plaatsen, 1 &#x3D; plaatsen, 2 &#x3D; logisch verwijderen, 3 &#x3D; voorwaardelijk fysiek verwijderen, 4 &#x3D; onvoorwaardelijk fysiek verwijderen | 
**e9553** | **str** | Numeriek: 0 &#x3D; niet verstrekken, 1 &#x3D; verstrekken | 
**e9554** | **str** | Numeriek: jjjjmmdd | 
**e9555** | **str** |  | 
**e9556** | **str** | Alfanumeriek: N &#x3D; Berichtendienst, webservice of API; A &#x3D; alternatief medium | 
**e9560** | **List[str]** | Numeriek (N maal) | 
**e9561** | **str** |  | 
**e9562** | **str** | Numeriek: 0 &#x3D; niet bevoegd, 1 &#x3D; bevoegd | 
**e9563** | **List[str]** | Numeriek (N maal) | 
**e9566** | **str** | Numeriek: 0 &#x3D; niet bevoegd, 1 &#x3D; bevoegd | 
**e9567** | **str** | Alfanumeriek: N &#x3D; Berichtendienst, webservice of API; A &#x3D; alternatief medium | 
**e9570** | **List[str]** | Numeriek: dit veld komt alleen in oude tabelregels voor; N maal | 
**e9571** | **str** | Alfamumeriek: dit veld komt alleen in oude tabelregels voor | 
**e9573** | **str** | Alfamumeriek: N &#x3D; Berichtendienst, A &#x3D; alternatief medium; dit veld komt alleen in oude tabelregels voor | 
**e9998** | **str** | Numeriek: jjjjmmdd | 
**e9999** | **str** | Numeriek: jjjjmmdd | 

## Example

```python
from berichten_api.models.autorisatietabelregel import Autorisatietabelregel

# TODO update the JSON string below
json = "{}"
# create an instance of Autorisatietabelregel from a JSON string
autorisatietabelregel_instance = Autorisatietabelregel.from_json(json)
# print the JSON string representation of the object
print(Autorisatietabelregel.to_json())

# convert the object into a dict
autorisatietabelregel_dict = autorisatietabelregel_instance.to_dict()
# create an instance of Autorisatietabelregel from a dict
autorisatietabelregel_from_dict = Autorisatietabelregel.from_dict(autorisatietabelregel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


