import requests
import RiotConsts as Consts
import json

class RiotAPI(object):

    def __init__(self, api_key):
        self.api_key = api_key


    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
                Consts.URL['base'].format(
                    url = api_url
                    ),
                params = args
                )
        return response.json()

    def get_entries_by_summonerid(self, encryptedSummonerId):
        api_url = Consts.URL['entries_by_summoner'].format(
                version = Consts.API_VERSIONS['V4'],
                summonerid = encryptedSummonerId
                )
        return self._request(api_url)
    
    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
                version = Consts.API_VERSIONS['V4'],
                names = name
                )
        return self._request(api_url)

