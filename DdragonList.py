import urllib.request
import json
import requests
from requests.structures import CaseInsensitiveDict


with urllib.request.urlopen("https://ddragon.leagueoflegends.com/api/versions.json") as champurl:
    data = json.loads(champurl.read().decode())
    version = data[0]
    print(version)

url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"


resp = requests.get(url, headers=headers)

print(type(resp))



champ = resp.json()
print(type(champ))

with open('champions.json', 'w') as champs:
    json.dump(champ, champs)

