# League-Stats

## App Overview
<p>League-Stats is a web application that allows users to check and analyze any summoner's League of Legends statistics. 
The application fetches data using the Riot Games API and presents it in an easy-to-read format. 
This application provides a comprehensive and user-friendly interface for League of Legends players to track and analyze their performance. 
By entering a summoner's name, users can access detailed statistics, historical data, and compare their progress over time.</p>

## Features
- **Summoner Statistics**: View detailed stats for any summoner.
- **Historical Data**: Track performance over time.
- **Responsive Design**: Accessible on all devices.

## Directory Structure
<ul>
  <li><code>app.py</code>: Main application script</li>
  <li><code>data.py</code>: Data fetching and processing logic</li>
  <li><code>image.py</code>: Image handling or generation logic</li>
  <li><code>templates/</code>: HTML templates for rendering web pages</li>
  <li><code>static/</code>: Static files (CSS, JavaScript, images)</li>
  <li><code>requirements.txt</code>: Python dependencies</li>
</ul>


## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/kevintian4/League-Stats.git
cd League-Stats
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configuration
<ol>
  <li>Obtain an API key from the <a href="https://developer.riotgames.com"/>Riot Games Developer Portal</a>.</li>
  <li>Create a '.env' file in the root directory of the project and add your API key:</li>
</ol>

```bash
api_key=your_api_key_here
```

### Running the Application
```bash
python app.py
```
<p>Open your web browser and navigate to http://127.0.0.1:5000/ to access the application.</p>
