Dream 11 Fantasy Team Predictor

A Python-based fantasy cricket player prediction project that uses historical player performance data and machine learning to estimate fantasy points.

The project collects batting, bowling, and fielding statistics from ESPNcricinfo, predicts recent performance using an XGBoost model, calculates fantasy points, and generates a 15-player squad.

Features

Uses historical player statistics.

Supports batting, bowling, wicket-keeping, and all-rounder players.

Predicts player performance using XGBoost.

Calculates fantasy points from predicted performance.

Gives extra importance to recent matches.

Considers batting, bowling, and fielding points.

Automatically selects a 15-player squad.

Tries to include different player roles in the final squad.

Saves the final team as a CSV file.

How It Works

The project follows these main steps:

Reads the list of players and their roles from an Excel file.

Gets player statistics from ESPNcricinfo.

Cleans and converts the statistics into numerical data.

Creates lag features from previous performances.

Trains an XGBoost regression model for each statistical category.

Predicts the player's next performance.

Converts the prediction into fantasy points.

Adds fielding, batting, and bowling points where applicable.

Sorts players based on predicted fantasy points.

Selects a final 15-player team.

Saves the result to a CSV file.

Machine Learning

The project uses XGBoost Regression.

Historical performances are converted into lag features. For example, with 5 lags, the model uses the previous five observations to predict the next value.

Recent matches are also given higher weights so that newer performances have more influence on the prediction.

Fantasy Point Calculation

The project calculates points for three main areas:

Batting

Batting points consider:

Runs

Boundaries

Sixes

Milestones

Strike rate

Bowling

Bowling points consider:

Runs conceded

Wickets

Economy rate

Wicket milestones

Fielding

Fielding points are calculated using dismissals.

Project Structure
fantasy-cricket-predictor/
│
├── src/
│   └── predictor.py
│
├── data/
│   └── .gitkeep
│
├── .gitignore
├── requirements.txt
└── README.md

Requirements

Python 3.9+

pandas

NumPy

Requests

BeautifulSoup4

XGBoost

openpyxl

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/fantasy-cricket-predictor.git
cd fantasy-cricket-predictor


Create a virtual environment:

Windows
python -m venv venv
venv\Scripts\activate

Linux / macOS
python3 -m venv venv
source venv/bin/activate


Install the required packages:

pip install -r requirements.txt

Input Data

The program expects an Excel file named:

SquadPlayerNames_IndianT20League.xlsx


The workbook should contain sheets in the following format:

Match_1
Match_2
Match_3
...


Each sheet should contain player information including fields such as:

Player Name

Player Type

Team

IsPlaying

The Excel file is intentionally excluded from Git using .gitignore.

Running the Project

Run the program by providing the match number:

python src/predictor.py 1


For another match:

python src/predictor.py 2


The program will generate:

AI_Explorers_output.csv


The output contains:

Player Name	Team	C/VC
Player 1	Team A	C
Player 2	Team B	VC
Player 3	Team A	NA
Important Notes

This project is intended as a machine learning and data analysis project.

The predictions are based on historical performance and should not be treated as guaranteed future results.

The project depends on data being available from ESPNcricinfo. Changes to the website's HTML structure may require changes to the scraping code.

Future Improvements

Some possible improvements are:

Move the code into separate modules.

Add proper logging and error handling.

Avoid training a new model for every prediction.

Add more player and match features.

Include venue and opposition statistics.

Include recent team/player form.

Add automated data collection.

Add model evaluation metrics.

Compare XGBoost with other machine learning models.

Create a web interface for predictions.

Add unit tests.

Use configuration files instead of hard-coded values.

Disclaimer

This project is created for educational and experimental purposes. Predictions are estimates based on historical data and machine learning and are not guaranteed to be accurate.
