from RiotAPI import RiotAPI
import RiotFunct as Rf


def extractor_cloud_function(event, context):

    user_name = 'ty6009'
    info = 'RGAPI-ed543b26-73a7-4c12-9c64-b4402a871bc0'

    api = Rf.cloud_get_api(info)

    Rf.get_league_stats(api, user_name)

