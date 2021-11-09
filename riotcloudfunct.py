from RiotAPI import RiotAPI
import RiotFunct as Rf
import GcpFunctions as Gp
import pubsub as Ps


project_id = Ps.project_id
subscription_id = Ps.subscription_id

class Error(Exception):
    """Base class for other exceptions"""
    pass

class SummonerNameInvalid(Error):
    """Raised when the Username input is not a real Username"""
    pass

class ApiNotValid(Error):
    """Raised when the Api input is not valid"""
    pass

def extractor_cloud_function(event, context):

    #Ps.pubsub_pull(project_id)
    #data = Ps.receiving_message(project_id, subscription_id)

    user_name = 'ty6009'
    info = 'RGAPI-d0c54f51-3bd2-4e01-ba27-a5dd166759ca'

        #buckets = Gp.list_buckets()
        #if not 'Yoedle42' in buckets:
            #Gp.create_bucket('Yoedle42', 'Riot-Extractor')
        #if not 'ty6009' in buckets:
            #Gp.create_bucket('ty6009', 'Riot-Extractor')
        #if not 'TayMojo' in buckets:
            #Gp.create_bucket('TayMojo', 'Riot-Extractor')
        #if not 'Any' in buckets:
            #Gp.create_bucket('Any', 'Riot-Extractor')

    Rf.clear_files()

    api = Rf.cloud_get_api(info)

    #summoner = api.get_summoner_by_name(user_name)
    #Id = summoner['id']
    #Level = summoner['summonerLevel']

    Rf.get_league_stats(api, user_name)

    #Rf.get_champion_masteries(api, Id)




extractor_cloud_function()
