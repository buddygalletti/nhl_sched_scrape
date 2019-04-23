# Owner: Buddy Galletti
# Created: September 2018
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import requests

url = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate=2018-10-03&endDate=2019-04-20' #change startDate and endDate to whatever you prefer
data = requests.get(url).json()

download_dir = 'nhl_sched_2019.csv' #change file name to whatever you prefer
csv = open(download_dir, "w")

keys = data.keys()

dates = data.get('dates')

columnTitleRow = 'Date, Away, Home, My Pick, Winner, Score \n' #change column titles to fit the data you want to collect
csv.write(columnTitleRow)

for date in dates:
    games = date.get('games')
    
    for game in games:
        teams = game.get('teams')
        
        home_team_name = teams['home']['team']['name']
        away_team_name = teams['away']['team']['name']
        
        home_score = game['teams']['home']['score']
        away_score = game['teams']['away']['score']
        score = str(away_score) + '-' + str(home_score)

        if (home_score > away_score):
            winner = home_team_name
        elif (home_score < away_score):
            winner = away_team_name
        else: winner = ''

        row = date['date'] + ',' + away_team_name + ',' + home_team_name + ',,' + winner + ',' + score + '\n'
        csv.write(row)
