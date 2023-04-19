from data import champion_dict, api_key, get_champion_mastery_data, organize_champion_data
from prettytable import PrettyTable
import os

ongoing = True
while ongoing:
    summoner_name = str(input("Enter the summoner's IGN: "))
    data = get_champion_mastery_data(api_key, summoner_name)
    while data == -1: 
        summoner_name = str(input("Summoner does not exist. Please try again: "))
        data = get_champion_mastery_data(api_key, summoner_name)
        
    data = organize_champion_data(data, champion_dict)
    
    # print table
    table = PrettyTable()
    table.junction_char = "o"
    table.add_column("Champion", data["champion_names"])
    table.add_column("Mastery Level", data["champion_levels"])
    table.add_column("Mastery Points", data["champion_points"])
    table.add_column("Last Played(Days)", data["last_played"])
    table.add_column("Mastery Points Until Next Level", data["points_until_next_level"])
    table.add_column("Chest Granted", data["chests_granted"])

    print("What would you like to sort by?")
    user_sort = str(input('Sort By "Champion"\n"Mastery Level"\n"Mastery Points"\n"Last Played"\n"Mastery Points Until Next Level"\n"Chest Granted": ')).title()
    while user_sort not in ["Champion", "Mastery Level", "Mastery Points", "Last Played", "Mastery Points Until Next Level", "Chest Granted"]:
        user_sort = str(input("Invalid input. Enter one of the above options: ")).title()

    if user_sort == "Last Played":
        user_sort = "Last Played(Days)"

    if user_sort == "Mastery Level" or user_sort == "Last Played" or user_sort == "Mastery Points":
        table.reversesort = True
    else:
        table.reversesort = False   

    table.sortby = user_sort
    print(table)

    end = input("End program? (y/n): ")
    if end == "y":
        ongoing = False
    os.system("cls")


