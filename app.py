from flask import Flask, render_template, request
from data import champion_dict, api_key, get_champion_mastery_data, organize_champion_data
from prettytable import PrettyTable

app = Flask(__name__, template_folder='templates')

def get_stats(summoner_name):
    data = get_champion_mastery_data(api_key, summoner_name)
    if data == -1:
        return {'error': 'Summoner does not exist. Please try again.'}
    else:
        data = organize_champion_data(data, champion_dict)
        table = PrettyTable()
        table.junction_char = "o"
        table.add_column("Champion", data["champion_names"])
        table.add_column("Mastery Level", data["champion_levels"])
        table.add_column("Mastery Points", data["champion_points"])
        table.add_column("Last Played(Days)", data["last_played"])
        table.add_column("Mastery Points Until Next Level", data["points_until_next_level"])
        table.add_column("Chest Granted", data["chests_granted"])
        table.sortby = "Chest Granted"
        return {'table': table.get_html_string()}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        summoner_name = request.form['summoner_name']
        stats = get_stats(summoner_name)
        if 'error' in stats:
            return render_template('index.html', error=stats['error'])
        else:
            return render_template('stats.html', table=stats['table'])
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

