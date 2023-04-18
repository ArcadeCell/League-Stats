from flask import Flask, render_template, request
from data import champion_dict, api_key, get_champion_mastery_data, organize_champion_data
from prettytable import PrettyTable

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        summoner_name = request.form["summoner_name"]
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

        user_selected_sort = request.form["sort_by"].title()
        
        if user_selected_sort == "Last Played":
            user_selected_sort = "Last Played(Days)"

        if user_selected_sort == "Mastery Level" or user_selected_sort == "Last Played":
            table.reversesort = True

        table.sortby = user_selected_sort
        table_html = table.get_html_string()
        
        return render_template("index.html", table=table_html)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
