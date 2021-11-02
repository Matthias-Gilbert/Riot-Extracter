from RiotAPI import RiotAPI
import csv
import json
import os


def info_type_selection():
    print('What Info Would You Like To Pull, Game Stats Or Masteries?')
    InfoType = input("Please enter Stats or Masteries, Type 'exit' to quit: ")
    if InfoType.casefold() == 'exit':
        print('Have a lovely day')
        exit()
    elif InfoType.casefold() == 'stats' or InfoType.casefold() == 'masteries':
        return InfoType
    else:
        print('Please enter one of the options')
        return info_type_selection()

def get_league_api():
    
    info = input("Please enter your Api, Type 'exit' if you want to quit: ")
    if info.casefold() == 'exit' or info.casefold() == 'quit':
        print('Have a lovely day')
        exit()
    
    if info[:5] == 'RGAPI' and len(info) == 42:
        api = RiotAPI(info)
        return api

    else:
        print('Please enter a valid Api')
        return get_league_api()


def get_league_stats(api, Id, level, user_name):
    while True:
        try:
            stats = api.get_entries_by_summonerid(Id)
            flex = stats[0]
            solo = stats[1]

            flex_name = flex['summonerName']
            flex_wins = flex['wins']
            flex_tier = flex['tier']
            flex_rank = flex['rank']
            flex_Points = flex['leaguePoints']
            flex_losses = flex['losses']
            flex_hotStreak = flex['hotStreak']
            flex_total = int(flex_wins) + int(flex_losses)
            flex_winperc = int(flex_wins) / int(flex_total)
            flex_winperc = flex_winperc * 100
            flex_winRate = int(flex_winperc)
            if flex_hotStreak == True:
                flex_winStreak = 'Your on winning streak'

            elif flex_hotStreak == False:
                flex_winStreak = 'Your not on a winning streak'
    
            flex_list = [f"Username:{flex_name}",f"Level:,{level}",f"Tier:{flex_tier}",f"Rank:{flex_rank}",f"Rank points:{flex_Points}",f"Wins:{flex_wins}",f"Losses:{flex_losses}",f"Winningstreak:{flex_hotStreak}",f"WinRate:{flex_winRate}%"]

            with open('FlexRanked.csv', 'w', encoding='UTF8', newline='') as flex_file:
                writer = csv.writer(flex_file)
                writer.writerow(flex_list)
    
            flex_data = {
                    'Flex_stats': {
                        'Summoner' : flex_name,
                        'Level' : level,
                        'Tier' : flex_tier,
                        'Rank' : flex_rank,
                        'LeaguePoints' : flex_Points,
                        'Wins' : flex_wins,
                        'Losses' : flex_losses,
                        'WinningStreak' : flex_hotStreak,
                        'WinRate' : flex_winRate
                        }
                }

    

            flex_json = json.dumps(flex_data)
            with open('FlexRanked.json', 'w') as f:
                f.write(flex_json)


            solo_name = solo['summonerName']
            solo_wins = solo['wins']
            solo_tier = solo['tier']
            solo_rank = solo['rank']
            solo_Points = solo['leaguePoints']
            solo_losses = solo['losses']
            solo_hotStreak = solo['hotStreak']
            solo_total = int(solo_wins) + int(solo_losses)
            solo_winperc = int(solo_wins) / int(solo_total)
            solo_winperc = solo_winperc * 100
            solo_winRate = int(solo_winperc)

            if solo_hotStreak == True:
                solo_winStreak = "You're on winning streak"

            elif solo_hotStreak == False:
                solo_winStreak = "You're not on a winning streak"
    
            solo_list = [f"Username:{solo_name}",f"Level:,{level}",f"Tier:{solo_tier}",f"Rank:{solo_rank}",f"Rank points:{solo_Points}",f"Wins:{solo_wins}",f"Losses:{solo_losses}",f"Winningstreak:{solo_hotStreak}",f"WinRate:{solo_winRate}%"]

            with open('RankedSoloDuo.csv', 'w', encoding='UTF8' ,newline='') as solo_file: 
                writer = csv.writer(solo_file)
                writer.writerow(solo_list)
    
            solo_data = {
                    'Solo_stats': {
                        'Summoner' : solo_name,
                        'Level' : level,
                        'Tier' : solo_tier,
                        'Rank' : solo_rank,
                        'LeaguePoints' : solo_Points,
                        'Wins' : solo_wins,
                        'Losses' : solo_losses,
                        'WinningStreak' : solo_hotStreak,
                        'Winrate' : solo_winRate
                        }
                    }



            solo_json = json.dumps(solo_data)
            with open('RankedSoloDuo.json', 'w') as s:
                s.write(solo_json)

            solo_stats = f"Username: {solo_name} \nLevel: {level} \nRank: {solo_tier} {solo_rank} {solo_Points} \nWins/Losses: W:{solo_wins} L:{solo_losses} \nWinrate: {solo_winRate}% \n{solo_winStreak}"

            flex_stats = f"Username: {flex_name} \nLevel: {level} \nRank: {flex_tier} {flex_rank} {flex_Points} \nWins/Losses: W:{flex_wins} L:{flex_losses} \nWinrate: {flex_winRate}% \n{flex_winStreak}"

            Game_mode = input("What game type do you want your stats for Flex, Solo or Both: Type 'back' if you want a different opttion: ")

            if Game_mode.casefold() == 'back':
                break
            elif Game_mode.casefold() == 'flex':
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
                return get_league_stats(api, Id)
        except ValueError:
            print('Please enter a valid resopnse')
            return get_league_stats(api, Id)


def clear_files():
    if os.path.exists("/Riot-Extractor/RankedSoloDou.json"):
        os.remove("RankedSoloDuo.json")

    if os.path.exists("/Riot-Extractor/RankedSoloDou.csv"):
        os.remove("RankedSoloDuo.csv")

    if os.path.exists("/Riot-Extractor/FlexRanked.json"):
        os.remove("FlexRanked.json")

    if os.path.exists("/Riot-Extractor/FlexRanked.csv"):
        os.remove("FlexRanked.csv")


def get_champion_masteries(api, Id):
    
    # When given an api and a Id it will pull you champion masteries and stats
    
    with open('champions.json') as champdata:
        champs = json.load(champdata)
    
    # While loop takes the given variables and goes through the process of pulling champion information and masteries for specific champions

    while True:

        champ = input("Please enter a champion name, Type 'back' if you want to select another option: ")
        champ = champ.capitalize()
    
        if champ.casefold() == 'back':
            break

        elif not champ in champs['data']:
            print('Please enter a valid champion')
            return get_champion_masteries(api, user_name, Id)

        champId = champs["data"][champ]["key"]
    
        masteries = api.get_masteries_by_summonerid(Id, champId)
    
        champion_level = masteries["championLevel"]
        champion_points = masteries["championPoints"]
        champion_sincelevel = masteries['championPointsSinceLastLevel']
        champion_tilllevel = masteries['championPointsUntilNextLevel']
        champion_chestGranted = masteries["chestGranted"]
        champion_tokens = masteries['tokensEarned']

        champion_mastery = f"{champ} stats: \nMastery: level {champion_level}, points {champion_points} \nProgress: Points till next level {champion_tilllevel} \nTokens Earned: {champion_tokens} \nEarned Chest: {champion_chestGranted}"

        print(champion_mastery)
        
        while True:
            try:
                again = input('Would you like to look at a another champion? yes/no: ')
                if again.casefold() == 'yes':
                    return get_champion_masteries(api, user_name, Id)
                elif again.casefold() == 'no':
                    break
                else:
                    print('Please enter a yes or no response')
                    continue
            except ValueError:
                print('please enter a vailid response')
                continue
        break


#def get_all_champion_masteries(api, user_name, Id):


