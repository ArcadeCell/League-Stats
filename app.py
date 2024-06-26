from flask import Flask, render_template, request
from data import champion_dict, api_key, get_champion_mastery_data, organize_champion_data,\
get_summoner_icon, get_account_data, get_summoner_rank, get_summoner_data, region_to_continent
from prettytable import PrettyTable


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    error_message = "Summoner not found. Please check spelling."
    if request.method == "POST":
        region = request.form["region-select"]
        continent = region_to_continent(region)
        gameName = request.form["gameName_tagLine"].split("#")[0].strip()
        tagLine = request.form["gameName_tagLine"].split("#")[1].strip()

        account_data = get_account_data(api_key, gameName, tagLine, continent)
        if account_data == -1:
            return render_template("index.html", error_message = error_message)

        gameName = account_data["gameName"]
        puuid = account_data["puuid"]

        summoner_data = get_summoner_data(api_key, puuid)
        if summoner_data == -1:
            return render_template("index.html", error_message = error_message)
        
        summoner_id = summoner_data["id"]

        summoner_rank = get_summoner_rank(summoner_id, region)
        summoner_icon_url = get_summoner_icon(summoner_data)
        mastery_data = get_champion_mastery_data(api_key, puuid, region)
        organized_mastery_data = organize_champion_data(mastery_data, champion_dict)

        # print table
        table = PrettyTable()
        # table.add_column("Images", organized_mastery_data["champion_images"])
        table.add_column("Champion", organized_mastery_data["champion_names"])
        table.add_column("Mastery Level", organized_mastery_data["champion_levels"])
        table.add_column("Mastery Points", organized_mastery_data["champion_points"])
        table.add_column("Last Played(Days)", organized_mastery_data["last_played"])
        table.add_column("Mastery Points Until Next Level", organized_mastery_data["points_until_next_level"])
        table.add_column("Tokens Earned", organized_mastery_data["tokens_earned"])

        user_selected_sort = request.form["sort-by"].title()
        
        if user_selected_sort == "Last Played":
            user_selected_sort = "Last Played(Days)"

        if user_selected_sort == "Mastery Level" or user_selected_sort == \
        "Last Played" or user_selected_sort == "Mastery Points" or user_selected_sort == "Tokens Earned":
            table.reversesort = True

        table.sortby = user_selected_sort
        table_html = table.get_html_string()
        
        return render_template("index.html", 
                               table=table_html, 
                               summoner_icon_url=summoner_icon_url, 
                               gameName=gameName, 
                               summoner_rank=summoner_rank,
                              )
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
