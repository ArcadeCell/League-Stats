import datetime
import requests
import os

api_key = os.getenv("API_KEY")


# function to get summoner_data
def get_summoner_data(api_key, summoner_name):
    # get Encrypted summoner ID from summoner username
    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 404:
        return -1
    summoner_data = response.json()
    return summoner_data


def get_summoner_id(data):
    summoner_id = data["id"]
    return summoner_id


def get_summoner_name(data):
    summoner_name = data["name"]
    return summoner_name


def get_summoner_rank(summoner_id):
    url = f"https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    summoner_rank = {
        "RANKED_SOLO_5x5": {},
        "RANKED_FLEX_SR": {}
    }

    if len(data) == 0:
        summoner_rank["RANKED_SOLO_5x5"]["rank"] = "UNRANKED"
        summoner_rank["RANKED_FLEX_SR"]["rank"] = "UNRANKED"
        return summoner_rank
    
    for object in data:
        if object["queueType"] == "RANKED_SOLO_5x5":
            # get league of summoner in lowercase for image url
            summoner_rank["RANKED_SOLO_5x5"]["league"] = object["tier"].lower()
            # if summoner is master, grandmaster, or challenger, don't add division
            if object["tier"] == "MASTER" or object["tier"] == "GRANDMASTER" or object["tier"] == "CHALLENGER":
                summoner_rank["RANKED_SOLO_5x5"]["rank"] = object["tier"]
            else:
                summoner_rank["RANKED_SOLO_5x5"]["rank"] = object["tier"] + " " + object["rank"]
            summoner_rank["RANKED_SOLO_5x5"]["lp"] = object["leaguePoints"]    
            summoner_rank["RANKED_SOLO_5x5"]["wins"] = object["wins"]
            summoner_rank["RANKED_SOLO_5x5"]["losses"] = object["losses"]
            summoner_rank["RANKED_SOLO_5x5"]["winrate"] = str(round(object["wins"] / (object["wins"] + object["losses"]) * 100, 1)) + "%"

        if object["queueType"] == "RANKED_FLEX_SR":
            # get league of summoner in lowercase for image url
            summoner_rank["RANKED_FLEX_SR"]["league"] = object["tier"].lower()
            # if summoner is master, grandmaster, or challenger, don't add division
            if object["tier"] == "MASTER" or object["tier"] == "GRANDMASTER" or object["tier"] == "CHALLENGER":
                summoner_rank["RANKED_FLEX_SR"]["rank"] = object["tier"]
            else:
                summoner_rank["RANKED_FLEX_SR"]["rank"] = object["tier"] + " " + object["rank"]
            summoner_rank["RANKED_FLEX_SR"]["lp"] = object["leaguePoints"]    
            summoner_rank["RANKED_FLEX_SR"]["wins"] = object["wins"]
            summoner_rank["RANKED_FLEX_SR"]["losses"] = object["losses"]
            summoner_rank["RANKED_FLEX_SR"]["winrate"] = str(round(object["wins"] / (object["wins"] + object["losses"]) * 100, 1)) + "%"
        
        if len(summoner_rank["RANKED_SOLO_5x5"]) == 0:
            summoner_rank["RANKED_SOLO_5x5"]["rank"] = "UNRANKED"
        if len(summoner_rank["RANKED_FLEX_SR"]) == 0:
            summoner_rank["RANKED_FLEX_SR"]["rank"] = "UNRANKED"
            
    return summoner_rank


# function to get summoner mastery data
def get_champion_mastery_data(api_key, data):
    summoner_id = data["id"]
    # use Encrypted summoner ID to request, store, and return summoner data
    url = f"https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data


# function to get summoner icon
def get_summoner_icon(data):
    iconId = data["profileIconId"]
    url = f"http://ddragon.leagueoflegends.com/cdn/{current_patch}/img/profileicon/{iconId}.png"
    return url


# function to organize summoner mastery data
def organize_champion_data(data, champion_dict):
    champion_ids = []
    champion_levels = []
    champion_points = []
    last_play_times = []
    points_until_next_level = []
    chests_granted = []

    # append values from data to their appropriate arrays
    for obj in data:
        champion_ids.append(obj["championId"])
        champion_levels.append(obj["championLevel"])
        champion_points.append(obj["championPoints"])
        last_play_times.append(obj["lastPlayTime"])
        points_until_next_level.append(obj["championPointsUntilNextLevel"])
        chests_granted.append(obj["chestGranted"])

    # convert champion IDs to their corresponding champion names
    champion_names = []
    for champion_id in champion_ids:
        champion_name = champion_dict[str(champion_id)]
        champion_names.append(champion_name)

    # convert last played time from unix time to days
    last_played = []
    for last_play_time in last_play_times:
        last_play_datetime = datetime.datetime.fromtimestamp(last_play_time / 1000)
        duration = datetime.datetime.now() - last_play_datetime
        duration_days = duration.days
        last_played.append(duration_days)

    champion_data = {
        "champion_names": champion_names,
        "champion_levels": champion_levels,
        "champion_points": champion_points,
        "last_played": last_played,
        "points_until_next_level": points_until_next_level,
        "chests_granted": chests_granted,
    }
    return champion_data


# set up the API request URL for getting champion names. first get current patch number
url = "https://ddragon.leagueoflegends.com/api/versions.json"
response = requests.get(url)
patch_data = response.json()
current_patch = patch_data[0]

# use current patch number to request most recent patch data
url = f"https://ddragon.leagueoflegends.com/cdn/{current_patch}/data/en_US/champion.json"
response = requests.get(url)
patch_data = response.json()

# retrieve champion IDs, convert to champion names, and store them in dictionary
champion_dict = {}
for champion_data in patch_data["data"].values():
    champion_id = champion_data["key"]
    champion_name = champion_data["name"]
    champion_dict[champion_id] = champion_name





