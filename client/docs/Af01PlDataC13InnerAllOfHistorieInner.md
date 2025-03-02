# Af01PlDataC13InnerAllOfHistorieInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e3110** | **str** | Een aanduiding die aangeeft of de persoon een oproep moet ontvangen voor verkiezingen voor het Europees parlement. ⦿ Groep: Europees kiesrecht (31) ⦿ Element: Aanduiding Europees kiesrecht (31.10) | [optional] 
**e3120** | **str** | De datum waarop de persoon een verzoek heeft gedaan met betrekking tot het uitoefenen van zijn kiesrecht voor het Europees parlement of de datum waarop de gemeente een melding heeft ontvangen dat de persoon is uitgesloten van deelname aan verkiezingen voor het Europees parlement. ⦿ Groep: Europees kiesrecht (31) ⦿ Element: Datum verzoek of mededeling Europees kiesrecht (31.20) | [optional] 
**e3130** | **str** | De datum waarop een uitsluiting voor deelname aan verkiezingen voor het Europees parlement niet meer van toepassing is.  Dit element wordt uitsluitend opgenomen indien er sprake is van een uitsluiting voor bepaalde tijd. ⦿ Groep: Europees kiesrecht (31) ⦿ Element: Einddatum uitsluiting Europees kiesrecht (31.30) | [optional] 
**e3140** | **str** | Het adres (zonder de plaatsnaam) in de EU-lidstaat waarvan de ingeschrevene de nationaliteit bezit en waar de ingeschrevene het laatst als kiezer was geregistreerd. ⦿ Groep: Europees kiesrecht (31) ⦿ Element: Adres EU-lidstaat van herkomst (31.40) | [optional] 
**e3150** | **str** | Plaatsnaam in de EU-lidstaat waarvan de ingeschrevene de nationaliteit bezit en waar de ingeschrevene het laatst als kiezer was geregistreerd. ⦿ Groep: Europees kiesrecht (31) ⦿ Element: Plaats EU-lidstaat van herkomst (31.50) | [optional] 
**e3160** | **str** | Een code, opgenomen in Tabel 34, Landentabel, dat het land (de EU-lidstaat) aangeeft waarvan de ingeschrevene de nationaliteit bezit en waar de ingeschrevene het laatst als kiezer was geregistreerd. ⦿ Groep: Europees kiesrecht (31) ⦿ Element: Land EU-lidstaat van herkomst (31.60) | [optional] 
**e3810** | **str** | Een aanduiding ter uitvoering van de Kieswet. ⦿ Groep: Uitsluiting kiesrecht (38) ⦿ Element: Aanduiding uitgesloten kiesrecht (38.10) | [optional] 
**e3820** | **str** | De datum waarop een uitsluiting kiesrecht niet meer van toepassing is. Dit element wordt uitsluitend opgenomen indien er sprake is van een uitsluiting voor bepaalde tijd. Bij een uitsluiting voor het leven komt het element niet voor. ⦿ Groep: Uitsluiting kiesrecht (38) ⦿ Element: Einddatum uitsluiting kiesrecht (38.20) | [optional] 
**e8210** | **str** | Een code, opgenomen in Tabel 33, Gemeententabel, die aangeeft in welke gemeente de ontlening aan of de afleiding uit het document heeft plaatsgevonden. ⦿ Groep: Document (82) ⦿ Element: Gemeente document (82.10) | [optional] 
**e8220** | **str** | De datum waarop de ontlening aan of de afleiding uit het document heeft plaatsgevonden. ⦿ Groep: Document (82) ⦿ Element: Datum document (82.20) | [optional] 
**e8230** | **str** | Beschrijving van het document waaraan de gegevens zijn ontleend of waaruit de gegevens zijn afgeleid. ⦿ Groep: Document (82) ⦿ Element: Beschrijving document (82.30) | [optional] 

## Example

```python
from berichten_api.models.af01_pl_data_c13_inner_all_of_historie_inner import Af01PlDataC13InnerAllOfHistorieInner

# TODO update the JSON string below
json = "{}"
# create an instance of Af01PlDataC13InnerAllOfHistorieInner from a JSON string
af01_pl_data_c13_inner_all_of_historie_inner_instance = Af01PlDataC13InnerAllOfHistorieInner.from_json(json)
# print the JSON string representation of the object
print(Af01PlDataC13InnerAllOfHistorieInner.to_json())

# convert the object into a dict
af01_pl_data_c13_inner_all_of_historie_inner_dict = af01_pl_data_c13_inner_all_of_historie_inner_instance.to_dict()
# create an instance of Af01PlDataC13InnerAllOfHistorieInner from a dict
af01_pl_data_c13_inner_all_of_historie_inner_from_dict = Af01PlDataC13InnerAllOfHistorieInner.from_dict(af01_pl_data_c13_inner_all_of_historie_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


