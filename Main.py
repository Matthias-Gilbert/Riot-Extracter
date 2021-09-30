from RiotAPI import RiotAPI

def main():
    info = input('Please Enter Your Api In Quotation Marks: ')
    api = RiotAPI(info)
    
    print('What Info Would You Like To Pull, Game Stats Or SummonerInfo?')
    InfoType = input("Please Enter Stats, Info or 'exit' if you are finished: ")
    if InfoType.casefold() == 'exit':
        print('Have a lovely day')
        exit()
                
    elif InfoType.casefold() == 'stats':
        SummonerId = input('Please Enter Your SummonerId: ')
        s = api.get_entries_by_summonerid(SummonerId)
        flex = s[0]
        solo = s[1]

        Game_mode = input('What game type do you want your stats for Flex, Solo or Both: ')
        if Game_mode == 'flex' or Game_mode == 'Flex':
            print('Your Ranked Flex stats are: ')
            print(flex)
        elif Game_mode == 'solo' or Game_mode == 'Solo':
            print('Your Solo/Duo stats are: ')
            print(solo)
        elif Game_mode == 'both' or Game_mode == 'Both':
            print('Your stats for Both are: ')
            print(flex)
            print(solo)
        else:
            print('Please Enter a valid game mode')
            return main()
    elif InfoType.casefold() == 'info':
        user_name = input('Please Enter Your summoner name: ')
        i = api.get_summoner_by_name(user_name)
        print(i)
    else:
        print('Please enter a valid response')
        main()


while True:
    main()
        
