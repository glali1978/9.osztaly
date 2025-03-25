# seged.py

import requests

#  Segédfüggvény
def leker_idojaras(varos):
    url = f"https://wttr.in/{varos}?format=j1"
    try:
        valasz = requests.get(url)
        if valasz.status_code == 200:
            adat = valasz.json()
            aktualis = adat['current_condition'][0]
            homerseklet = aktualis['temp_C']
            leiras = aktualis['weatherDesc'][0]['value']
            paratartalom = aktualis['humidity']
            return [homerseklet, leiras, paratartalom]
        else:
            return ["nincs adat", "-", "-"]
    except:
        return ["hiba", "-", "-"]