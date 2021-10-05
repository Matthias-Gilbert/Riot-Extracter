from RiotAPI import RiotAPI
import RiotFunct as Rf


api = None
while True:
    back = None
    Rf.clear_files()

    if api is None:
        api = Rf.get_league_api()
    
    Infotype = Rf.info_type_selection()
    
    if Infotype.casefold() == 'stats':
        user_name = input("Please Enter Your summoner name, Type 'back' to select another option: ")
        if user_name.lower() == 'back':
            back = 'back'
        if back is None:
            Rf.get_league_stats(api, user_name)
        else:
            continue

    elif Infotype.casefold() == 'info':
        user_name = input("Please Enter Your summoner name, Type 'back' to select another option: ")
        if user_name.lower() == 'back':
            back = 'back'
        if back is None:
            Rf.get_summoner_Id(api, user_name)
        else:
            continue
    
    

