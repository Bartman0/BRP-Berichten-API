# Af01PlDataC10Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e3910** | **str** | Een code, opgenomen in Tabel 56, Verblijfstiteltabel, die aangeeft over welke verblijfsrechtelijke status de ingeschrevene beschikt. ⦿ Groep: Verblijfstitel (39) ⦿ Element: Aanduiding verblijfstitel (39.10) | [optional] 
**e3920** | **str** | De datum waarop de verblijfstitel zijn geldigheid verliest.  Dit element wordt uitsluitend opgenomen indien er sprake is van een verblijfstitel voor bepaalde tijd. Bij een verblijfstitel voor het leven komt het element niet voor. ⦿ Groep: Verblijfstitel (39) ⦿ Element: Datum einde verblijfstitel (39.20) | [optional] 
**e3930** | **str** | De datum waarop de verblijfstitel zijn geldigheid krijgt. ⦿ Groep: Verblijfstitel (39) ⦿ Element: Ingangsdatum verblijfstitel (39.30) | [optional] 
**e8310** | **str** | Een aanduiding dat in een categorie één of meer gegevens met betrekking tot de onjuistheid of de strijdigheid met de openbare orde zijn of worden onderzocht. In categorie 08 Verblijfplaats kan de aanduiding tevens aangeven dat er is vastgesteld dat betrokkene niet op het geregistreerde adres woont. ⦿ Groep: Procedure (83) ⦿ Element: Aanduiding gegevens in onderzoek (83.10) | [optional] 
**e8320** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is gestart. ⦿ Groep: Procedure (83) ⦿ Element: Datum ingang onderzoek (83.20) | [optional] 
**e8330** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is beéindigd. ⦿ Groep: Procedure (83) ⦿ Element: Datum einde onderzoek (83.30) | [optional] 
**e8410** | **str** | Een aanduiding dat één of meer gegevens onjuist of strijdig zijn met de openbare orde. ⦿ Groep: Onjuist (84) ⦿ Element: Indicatie onjuist, dan wel strijdigheid met de openbare orde (84.10) | [optional] 
**e8510** | **str** | De datum waarop het geheel van gegevens geldig is geworden. ⦿ Groep: Geldigheid (85) ⦿ Element: Ingangsdatum geldigheid (85.10) | [optional] 
**e8610** | **str** | De datum waarop het geheel van gegevens daadwerkelijk in de BRP is opgenomen. ⦿ Groep: Opneming (86) ⦿ Element: Datum van opneming (86.10) | [optional] 
**historie** | [**List[Af01PlDataC10InnerAllOfHistorieInner]**](Af01PlDataC10InnerAllOfHistorieInner.md) |  | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c10_inner import Af01PlDataC10Inner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC10Inner from a JSON string
af01_pl_data_c10_inner_instance = Af01PlDataC10Inner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC10Inner.to_json())

# convert the object into a dict
af01_pl_data_c10_inner_dict = af01_pl_data_c10_inner_instance.to_dict()
# create an instance of Af01PlDataC10Inner from a dict
af01_pl_data_c10_inner_from_dict = Af01PlDataC10Inner.from_dict(af01_pl_data_c10_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


