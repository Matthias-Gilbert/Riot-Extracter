from RiotAPI import RiotAPI
import RiotFunct as Rf

def main():
    api = Rf.get_league_api()

    print('What Info Would You Like To Pull, Game Stats Or SummonerInfo?')
    InfoType = input("Please enter Stats or Info: ")

    if InfoType.casefold() == 'stats':
        Rf.get_league_stats(api)

    elif InfoType.casefold() == 'info':
        Rf.get_summoner_Id(api)
    
    else:
        print('Please enter a valid input')
        main()


while True:
    main()
        
