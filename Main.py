from RiotAPI import RiotAPI
import RiotFunct as Rf
import GcpFunctions as Gp


class Error(Exception):
    """Base class for other exceptions"""
    pass

class SummonerNameInvalid(Error):
    """Raised when the Username input is not a real Username"""
    pass

class ApiNotValid(Error):
    """Raised when the Api input is not valid"""
    pass


user_name = None
api = None
Id = None
api_error = None

while True:

    #buckets = Gp.list_buckets()
    #if not 'Yoedle42' in buckets:
        #Gp.create_bucket('Yoedle42', 'Riot-Extractor')
    #if not 'ty6009' in buckets:
        #Gp.create_bucket('ty6009', 'Riot-Extractor')
    #if not 'TayMojo' in buckets:
        #Gp.create_bucket('TayMojo', 'Riot-Extractor')
    #if not 'Any' in buckets:
        #Gp.create_bucket('Any', 'Riot-Extractor')

    back = None
    
    Rf.clear_files()

    try:

        if api is None:
            api = Rf.get_league_api()
    
        if user_name is None:
            user_name = input('Please Enter Your summoner name: ')
            info = api.get_summoner_by_name(user_name)
        
        elif user_name == False:
            user_name = input('Please Enter Your summoner name: ')
            info = api.get_summoner_by_name(user_name)
        
        elif api_error == False:
            info = api.get_summoner_by_name(user_name)

        else:
            select = input('Would you like to select a different summoner? Yes/No: ')

            if select.casefold() == 'yes':
                user_name = input('Please enter the new summoner name: ')
                info = api.get_summoner_by_name(user_name)

            elif select.casefold() != 'no':
                print('Please enter a yes or no response')
                continue

        if info == 'bad username':
            raise SummonerNameInvalid
        
        if info == 'bad api':
            raise ApiNotValid

        else:
            Id = info['id']
            level = info ['summonerLevel']
            api_error = None

    except SummonerNameInvalid:
        user_name = False
        continue

    except ApiNotValid:
        api_error = False
        api = Rf.get_league_api()
        continue

    Infotype = Rf.info_type_selection()
    
    if Infotype.casefold() == 'stats':
        Rf.get_league_stats(api, Id, user_name, level)

    elif Infotype.casefold() == 'masteries':
        Rf.get_champion_masteries(api, Id)
    


