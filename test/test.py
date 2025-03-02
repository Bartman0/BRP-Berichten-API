plaats_bericht = """
{{
  "$schema" : "berichten.schema.json#/berichtsoorten/Ap01Bericht",
  "berichtType" : "Ap01",
  "herhaling" : "0",
  "plData" : {{
    "c01" : [ {{
      "e0120" : "{}"
    }} ]
  }}
}}
"""

verwijder_bericht = """
{{
  "$schema" : "berichten.schema.json#/berichtsoorten/Av01Bericht",
  "berichtType" : "Av01",
  "herhaling" : "0",
  "plData" : {{
    "c01" : [ {{
      "e0120" : "{}"
    }} ]
  }}
}}
"""


if __name__ == "__main__":
    print(plaats_bericht.format("123456789"))
    print(verwijder_bericht.format("123456789"))
