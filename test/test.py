import os

from berichten_api import LoBericht
from berichten_api import Configuration, ApiClient
from berichten_api import BerichtenverkeerApi
from berichten_api import PutMessageKenmerken

ap01_template = {
    "$schema": "berichten.schema.json#/berichtsoorten/Ap01Bericht",
    "berichtType": "Ap01",
    "herhaling": "0",
    "plData": {"c01": [{"e0120": "000000000"}]},
}

av01_template = {
    "$schema": "berichten.schema.json#/berichtsoorten/Av01Bericht",
    "berichtType": "Av01",
    "herhaling": "0",
    "plData": {"c01": [{"e0120": "000000000"}]},
}


put_message_kenmerken_template = {
    "berichtId": "000",
    "verwijzingBerichtId": "",
    "berichtType": "",
    "ontvanger": 0,
}


if __name__ == "__main__":
    conf = Configuration(
        server_index=3,
        username="11",
        password=os.environ["BERICHTEN_API_PASSWORD"],
    )
    api_client = ApiClient(conf)
    berichten_client = BerichtenverkeerApi(api_client)

    ap01_bericht_inhoud = ap01_template.copy()
    ap01_bericht_inhoud["plData"]["c01"][0]["e0120"] = "177022045"

    # av01_bericht_inhoud = av01_template.copy()
    # av01_bericht_inhoud["plData"]["c01"][0]["e0120"] = "177022045"

    ap01_put_message_kenmerken = put_message_kenmerken_template.copy()
    ap01_put_message_kenmerken["berichtId"] = "1"
    ap01_put_message_kenmerken["berichtType"] = "Ap01"
    ap01_put_message_kenmerken["ontvanger"] = 2


    bericht_kenmerken = PutMessageKenmerken.from_dict(ap01_put_message_kenmerken)
    bericht_inhoud = LoBericht.from_dict(ap01_bericht_inhoud)
    pass

    ap01_bericht = {
        "berichtKenmerken": bericht_kenmerken,
        "berichtInhoud": bericht_inhoud,
    }
    result = berichten_client.put_messages({"berichten": [ap01_bericht]})

    pass
