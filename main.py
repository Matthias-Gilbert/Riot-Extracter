from RiotAPI import RiotAPI
import RiotFunct as Rf
import base64
import json

def extractor_cloud_function(event, context):
    
    print(event)
    data = base64.b64decode(event['data'])
    data_dict = json.loads(data)
    

    user_name = data_dict['username']
    info = data_dict['Api']

    api = Rf.cloud_get_api(info)

    Rf.get_league_stats(api, user_name)

