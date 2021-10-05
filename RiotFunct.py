from RiotAPI import RiotAPI
import csv
import os
import re


def info_type_selection():
    print('What Info Would You Like To Pull, Game Stats Or SummonerInfo?')
    InfoType = input("Please enter Stats or Info, Type 'exit' to quit: ")
    if InfoType.casefold() == 'exit':
        print('Have a lovely day')
        exit()
    elif InfoType.casefold() == 'stats' or InfoType.casefold() == 'info':
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


def get_league_stats(api, user_name):

    info = api.get_summoner_by_name(user_name)
    Id = info['id']

    s = api.get_entries_by_summonerid(Id)
    flex = s[0]
    solo = s[1]

    f_name = flex['summonerName']
    f_wins = flex['wins']
    f_tier = flex['tier']
    f_rank = flex['rank']
    f_Points = flex['leaguePoints']
    f_losses = flex['losses']
    f_hotStreak = flex['hotStreak']

    if f_hotStreak == True:
        f_winStreak = 'Your on winning streak'

    elif f_hotStreak == False:
        f_winStreak = 'Your not on a winning streak'
    
    flex_list = [["Username: ", f_name],
                ["Tier: ", f_tier],
                ["Rank: ", f_rank],
                ["Rank points: ", f_Points],
                ["Wins: ", f_wins],
                ["Losses: ", f_losses],
                ["Winning streak: ", f_hotStreak]]

    with open('FlexRanked.csv', 'w', newline='') as flex_file:
        writer = csv.writer(flex_file)
        writer.writerows(flex_list)

    s_name = solo['summonerName']
    s_wins = solo['wins']
    s_tier = solo['tier']
    s_rank = solo['rank']
    s_Points = solo['leaguePoints']
    s_losses = solo['losses']
    s_hotStreak = solo['hotStreak']

    if s_hotStreak == True:
        s_winStreak = "You're on winning streak"

    elif s_hotStreak == False:
        s_winStreak = "You're not on a winning streak"
    
    solo_list = [["Username: ", s_name],
                ["Tier: ", s_tier],
                ["Rank: ", s_rank],
                ["Rank points: ", s_Points],
                ["Wins: ", s_wins],
                ["Losses: ", s_losses],
                ["Winning streak: ", s_hotStreak]]

    with open('RankedSoloDou.csv', 'w', newline='') as solo_file:
        writer = csv.writer(solo_file)
        writer.writerows(solo_list)

    solo_stats = f"Username: {s_name} \nRank: {s_tier} {s_rank} {s_Points} \nWins/Losses: W:{s_wins} L:{s_losses} \n{s_winStreak}"

    flex_stats = f"Username: {f_name} \nRank: {f_tier} {f_rank} {f_Points} \nWins/Losses: W:{f_wins} L:{f_losses} \n{f_winStreak}"

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
        return get_league_stats()


def get_summoner_Id(api, user_name):

        info = api.get_summoner_by_name(user_name)
        name = info['name']
        level = info['summonerLevel']
        print(f"Username: {name} \nLevel: {level}")

        account_list = [["Username: ", name],
                    ["Level: ", level]]

        with open('AccountInfo.csv', 'w', newline='') as account_file:
            writer = csv.writer(account_file)
            writer.writerows(account_list)


def clear_files():
    if os.path.exists("/Riot-Extractor/AccountInfo.csv"):
        os.remove("AccountInfo.csv")
    if os.path.exists("/Riot-Extractor/RankedSoloDoe.csv"):
        os.remove("RankedSoloDuo.csv")
    if os.path.exists("/Riot-Extractor/RankedFlex.csv"):
        os.remove("RankedFlex.csv")
