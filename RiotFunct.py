from RiotAPI import RiotAPI


def get_league_api():
        info = input("Please enter your Api, Type 'exit' if you want to quit: ")
        if info.casefold() == 'exit' or info.casefold() == 'quit':
            print('Have a lovely day')
            exit()
        else:
            api = RiotAPI(info)
            return api


def get_league_stats(api):

    user_name = input("Please Enter Your summoner name, Type 'back' to select another option: ")
    if user_name.lower() == 'back':
        return get_league_api

    info = api.get_summoner_by_name(user_name)
    Id = info['id']

    s = api.get_entries_by_summonerid(Id)
    flex = s[0]
    solo = s[1]

    f_name = flex['summonerName']
    f_wins = flex['wins']
    f_tier = flex['tier']
    f_rank = flex['rank']
    f_leaguePoints = flex['leaguePoints']
    f_losses = flex['losses']
    f_hotStreak = flex['hotStreak']

    if f_hotStreak == True:
        f_winStreak = 'Your on winning streak'

    elif f_hotStreak == False:
        f_winStreak = 'Your not on a winning streak'

    s_name = solo['summonerName']
    s_wins = solo['wins']
    s_tier = solo['tier']
    s_rank = solo['rank']
    s_leaguePoints = solo['leaguePoints']
    s_losses = solo['losses']
    s_hotStreak = solo['hotStreak']

    if s_hotStreak == True:
        s_winStreak = 'Your on winning streak'

    elif s_hotStreak == False:
        s_winStreak = 'Your not on a winning streak'

    solo_stats = f"Username: {s_name} \nRank: {s_tier} {s_rank} {s_leaguePoints} \nWins/Losses: W:{s_wins} L:{s_losses} \n{s_winStreak}"

    flex_stats = f"Username: {f_name} \nRank: {f_tier} {f_rank} {f_leaguePoints} \nWins/Losses: W:{f_wins} L:{f_losses} \n{f_winStreak}"

    Game_mode = input("What game type do you want your stats for Flex, Solo or Both: ")

    if Game_mode.casefold() == 'flex':
        print('Your Ranked Flex stats are: ')
        print(flex_stats)

    elif Game_mode.casefold() == 'solo':
        print('Your Solo/Duo stats are: ')
        print(solo_stats)

    elif Game_mode == 'both' or Game_mode == 'Both':
        print('Your stats for Flex are: ')
        print(flex_stats)
        print()        
        print('Your stats for Solo/Duo are')
        print(solo_stats)

    else:
        print('Please Enter a valid game mode')
        return get_league_stats


def get_summoner_Id(api):

        user_name = input("Please Enter Your summoner name, Type 'back' to select another option: ")
        if user_name.lower() == 'back':
            return get_league_api

        else:
            info = api.get_summoner_by_name(user_name)
            name = info['name']
            summonerLevel = info['summonerLevel']
            print(f"Username: {name} \nLevel: {summonerLevel}")
