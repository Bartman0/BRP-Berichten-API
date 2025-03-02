# Af01PlDataC12InnerAllOfHistorieInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e3510** | **str** | Een codering, opgenomen in Tabel 48, Tabel Nederlands reisdocument, die aangeeft welk Nederlands reisdocument is verstrekt of in welk reisdocument de ingeschrevene is bijgeschreven. ⦿ Groep: Nederlands reisdocument (35) ⦿ Element: Soort Nederlands reisdocument (35.10) | [optional] 
**e3520** | **str** | Het nummer van het verstrekte Nederlandse reisdocument of het nummer van het Nederlandse reisdocument waarin de ingeschrevene is bijgeschreven. ⦿ Groep: Nederlands reisdocument (35) ⦿ Element: Nummer Nederlands reisdocument (35.20) | [optional] 
**e3530** | **str** | De datum waarop het Nederlands reisdocument is uitgegeven of de datum van bijschrijving van de ingeschrevene in een Nederlands reisdocument. ⦿ Groep: Nederlands reisdocument (35) ⦿ Element: Datum uitgifte Nederlands reisdocument (35.30) | [optional] 
**e3540** | **str** | Een codering, opgenomen in Tabel 49, Tabel Autoriteit van afgifte Nederlands reisdocument, die aangeeft welke autoriteit het Nederlands reisdocument heeft verstrekt of de bijschrijving heeft verricht. ⦿ Groep: Nederlands reisdocument (35) ⦿ Element: Autoriteit van afgifte Nederlands reisdocument (35.40) | [optional] 
**e3550** | **str** | De datum waarop een Nederlands reisdocument, dat aan de ingeschrevene is verstrekt of waarin de ingeschrevene is bijgeschreven, zijn geldigheid verliest. ⦿ Groep: Nederlands reisdocument (35) ⦿ Element: Datum einde geldigheid Nederlands reisdocument (35.50) | [optional] 
**e3560** | **str** | De datum waarop een Nederlands reisdocument is vermist, ingehouden, ingeleverd, dan wel van rechtswege is vervallen. ⦿ Groep: Nederlands reisdocument (35) ⦿ Element: Datum inhouding dan wel vermissing Nederlands reisdocument (35.60) | [optional] 
**e3570** | **str** | Een aanduiding dat een Nederlands reisdocument is vermist, ingehouden, ingeleverd, dan wel van rechtswege is vervallen. ⦿ Groep: Nederlands reisdocument (35) ⦿ Element: Aanduiding inhouding dan wel vermissing Nederlands reisdocument (35.70) | [optional] 
**e3610** | **str** | Een aanduiding dat aan de ingeschrevene geen reisdocument mag worden verstrekt. ⦿ Groep: Signalering (36) ⦿ Element: Signalering met betrekking tot verstrekken Nederlands reisdocument (36.10) | [optional] 
**e8210** | **str** | Een code, opgenomen in Tabel 33, Gemeententabel, die aangeeft in welke gemeente de ontlening aan of de afleiding uit het document heeft plaatsgevonden. ⦿ Groep: Document (82) ⦿ Element: Gemeente document (82.10) | [optional] 
**e8220** | **str** | De datum waarop de ontlening aan of de afleiding uit het document heeft plaatsgevonden. ⦿ Groep: Document (82) ⦿ Element: Datum document (82.20) | [optional] 
**e8230** | **str** | Beschrijving van het document waaraan de gegevens zijn ontleend of waaruit de gegevens zijn afgeleid. ⦿ Groep: Document (82) ⦿ Element: Beschrijving document (82.30) | [optional] 
**e8310** | **str** | Een aanduiding dat in een categorie één of meer gegevens met betrekking tot de onjuistheid of de strijdigheid met de openbare orde zijn of worden onderzocht. In categorie 08 Verblijfplaats kan de aanduiding tevens aangeven dat er is vastgesteld dat betrokkene niet op het geregistreerde adres woont. ⦿ Groep: Procedure (83) ⦿ Element: Aanduiding gegevens in onderzoek (83.10) | [optional] 
**e8320** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is gestart. ⦿ Groep: Procedure (83) ⦿ Element: Datum ingang onderzoek (83.20) | [optional] 
**e8330** | **str** | De datum waarop een onderzoek inzake de onjuistheid of de strijdigheid met de openbare orde is beéindigd. ⦿ Groep: Procedure (83) ⦿ Element: Datum einde onderzoek (83.30) | [optional] 
**e8510** | **str** | De datum waarop het geheel van gegevens geldig is geworden. ⦿ Groep: Geldigheid (85) ⦿ Element: Ingangsdatum geldigheid (85.10) | [optional] 
**e8610** | **str** | De datum waarop het geheel van gegevens daadwerkelijk in de BRP is opgenomen. ⦿ Groep: Opneming (86) ⦿ Element: Datum van opneming (86.10) | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c12_inner_all_of_historie_inner import Af01PlDataC12InnerAllOfHistorieInner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC12InnerAllOfHistorieInner from a JSON string
af01_pl_data_c12_inner_all_of_historie_inner_instance = Af01PlDataC12InnerAllOfHistorieInner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC12InnerAllOfHistorieInner.to_json())

# convert the object into a dict
af01_pl_data_c12_inner_all_of_historie_inner_dict = af01_pl_data_c12_inner_all_of_historie_inner_instance.to_dict()
# create an instance of Af01PlDataC12InnerAllOfHistorieInner from a dict
af01_pl_data_c12_inner_all_of_historie_inner_from_dict = Af01PlDataC12InnerAllOfHistorieInner.from_dict(af01_pl_data_c12_inner_all_of_historie_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


