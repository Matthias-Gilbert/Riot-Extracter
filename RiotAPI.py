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


        if response.status_code == 200:
            return response.json()

        elif response.status_code == 500:
            print('The server seems to be having issues please try again later')
            exit()

        else:
            print('Please confirm your Api is up to date and was entered correctly')


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

