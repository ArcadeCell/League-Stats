from flask import Flask, render_template, request
from data import champion_dict, api_key, get_champion_mastery_data, organize_champion_data,\
get_summoner_icon, get_summoner_data, get_summoner_name, get_summoner_id, get_summoner_rank, get_region
from prettytable import PrettyTable

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    error_message = "Summoner not found. Please check spelling."
    if request.method == "POST":
        region = request.form["region-select"]
        region = get_region(region)
        summoner_name = request.form["summoner_name"]

        summoner_data = get_summoner_data(api_key, summoner_name, region)
        if summoner_data == -1:
            return render_template("index.html", error_message = error_message)
        
        summoner_id = get_summoner_id(summoner_data)
        summoner_rank = get_summoner_rank(summoner_id, region)
        summoner_name = get_summoner_name(summoner_data)
        summoner_icon_url = get_summoner_icon(summoner_data)
        mastery_data = get_champion_mastery_data(api_key, summoner_data, region)
        organized_mastery_data = organize_champion_data(mastery_data, champion_dict)

        # print table
        table = PrettyTable()
        table.add_column("Champion", organized_mastery_data["champion_names"])
        table.add_column("Mastery Level", organized_mastery_data["champion_levels"])
        table.add_column("Mastery Points", organized_mastery_data["champion_points"])
        table.add_column("Last Played(Days)", organized_mastery_data["last_played"])
        table.add_column("Mastery Points Until Next Level", organized_mastery_data["points_until_next_level"])
        table.add_column("Chest Granted", organized_mastery_data["chests_granted"])

        user_selected_sort = request.form["sort-by"].title()
        
        if user_selected_sort == "Last Played":
            user_selected_sort = "Last Played(Days)"

        if user_selected_sort == "Mastery Level" or user_selected_sort == "Last Played" or user_selected_sort == "Mastery Points":
            table.reversesort = True

        table.sortby = user_selected_sort
        table_html = table.get_html_string()
        
        return render_template("index.html", table=table_html, summoner_icon_url=summoner_icon_url, summoner_name=summoner_name, summoner_rank=summoner_rank)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
