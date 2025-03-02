# LoBericht


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**bericht_type** | **str** |  | 
**foutreden** | **str** |  | 
**gemeente** | **str** |  | 
**a_nummer** | **str** |  | 
**pl_data** | [**Af01PlData**](Af01PlData.md) |  | 
**status** | **str** |  | 
**datum** | **str** |  | 
**herhaling** | **str** |  | 
**afnemersindicatie** | **str** |  | 
**datum_ingang** | **str** |  | 
**datum_einde** | **str** |  | 
**autorisatietabelregel** | [**Autorisatietabelregel**](Autorisatietabelregel.md) |  | 
**te_wijzigen_tabel** | **str** |  | 
**tabel_data** | **object** | Beschrijving van de inhoud van de tabelberichten | 
**rubrieken** | **List[str]** |  | 
**datum_tijd** | **str** |  | 
**oud_a_nummer** | **str** |  | 
**gezochte_persoon** | **str** |  | 
**aktenummer** | **str** |  | 
**vrije_tekst** | **str** |  | 
**communicatiepartner_aan** | **str** |  | 
**communicatiepartner_van** | **str** |  | 
**datum_geldigheid** | **str** |  | 
**pl_data_set** | [**List[Af01PlData]**](Af01PlData.md) |  | 
**adresfunctie** | **str** |  | 
**identificatie** | **str** |  | 

## Example

```python
from berichten_api.models.lo_bericht import LoBericht

# TODO update the JSON string below
json = "{}"
# create an instance of LoBericht from a JSON string
lo_bericht_instance = LoBericht.from_json(json)
# print the JSON string representation of the object
print(LoBericht.to_json())

# convert the object into a dict
lo_bericht_dict = lo_bericht_instance.to_dict()
# create an instance of LoBericht from a dict
lo_bericht_from_dict = LoBericht.from_dict(lo_bericht_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


