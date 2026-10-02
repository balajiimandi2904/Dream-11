# Dream 11 Fantasy Team Predictor

A Python-based machine learning project that predicts fantasy cricket points for players using their historical batting, bowling, and fielding performances.

The project uses XGBoost to predict player performance and converts those predictions into fantasy points. Based on the predicted points, it generates a 15-player fantasy team.

## Features

- Fetches historical player statistics from ESPNcricinfo
- Supports batsmen, bowlers, wicketkeepers, and all-rounders
- Uses XGBoost regression for player performance prediction
- Uses previous performances as lag features
- Gives higher importance to recent performances
- Calculates batting, bowling, and fielding fantasy points
- Ranks players based on predicted fantasy points
- Generates a 15-player fantasy team
- Attempts to maintain different player roles in the final team
- Assigns Captain and Vice-Captain
- Exports the final team to a CSV file

## How It Works

The project follows this workflow:

    Excel Player Data
           |
           v
    Player Selection
           |
           v
    Fetch Historical Statistics
           |
           v
    Data Cleaning
           |
           v
    Create Lag Features
           |
           v
    XGBoost Prediction
           |
           v
    Fantasy Point Calculation
           |
           v
    Player Ranking
           |
           v
    15-Player Team Selection
           |
           v
    CSV Output

## Machine Learning Approach

The project uses XGBoost Regression to predict future player performance.

Historical player statistics are converted into lag features. The model uses previous performances to predict the next performance.

For example, with 5 lag values:

    Previous Performance 1
    Previous Performance 2
    Previous Performance 3
    Previous Performance 4
    Previous Performance 5
              |
              v
        XGBoost Model
              |
              v
     Predicted Performance

Recent performances are given higher weights so that newer performances have more influence on the prediction.

### Model Parameters

    Objective       : reg:squarederror
    Max Depth       : 5
    Learning Rate   : 0.1
    Boosting Rounds : 100

## Fantasy Point Calculation

The project calculates fantasy points from three main areas.

### Batting Points

Batting points consider:

- Runs
- Fours
- Sixes
- Run milestones
- Strike rate

### Bowling Points

Bowling points consider:

- Runs conceded
- Wickets
- Economy rate
- Wicket milestones

### Fielding Points

Fielding points are calculated using the predicted number of dismissals.

## Player Roles

The project supports four player types:

| Player Type | Description |
|-------------|-------------|
| BAT         | Batsman     |
| BOWL        | Bowler      |
| WK          | Wicketkeeper|
| ALL         | All-rounder |

The team selection logic also attempts to ensure that different player roles are represented in the final squad.

## Project Structure

    fantasy-cricket-predictor/
    |
    ├── src/
    │   └── predictor.py
    |
    ├── data/
    │   └── .gitkeep
    |
    ├── .gitignore
    ├── requirements.txt
    └── README.md

## Requirements

- Python 3.9+
- pandas
- NumPy
- Requests
- BeautifulSoup4
- XGBoost
- openpyxl

## Installation

### 1. Clone the Repository

    git clone https://github.com/YOUR_USERNAME/fantasy-cricket-predictor.git
    cd fantasy-cricket-predictor

### 2. Create a Virtual Environment

#### Windows

    python -m venv venv
    venv\Scripts\activate

#### Linux / macOS

    python3 -m venv venv
    source venv/bin/activate

### 3. Install Dependencies

    pip install -r requirements.txt

## Input Data

The project expects an Excel file named:

    SquadPlayerNames_IndianT20League.xlsx

The workbook should contain sheets based on match numbers:

    Match_1
    Match_2
    Match_3
    ...

Each sheet should contain player information such as:

| Column      | Description                  |
|-------------|------------------------------|
| Player Name | Name of the player           |
| Player Type | BAT, BOWL, WK, or ALL        |
| Team        | Player's team                |
| IsPlaying   | Player's playing status      |

### Example

| Player Name | Player Type | Team   | IsPlaying |
|-------------|-------------|--------|-----------|
| Player 1    | BAT         | Team A | PLAYING   |
| Player 2    | BOWL        | Team B | PLAYING   |
| Player 3    | ALL         | Team A | PLAYING   |

## Running the Project

The match number is passed as a command-line argument.

For example, to process Match_1:

    python src/predictor.py 1

For Match_2:

    python src/predictor.py 2

The program reads the corresponding match sheet from the Excel workbook.

For example:

    python src/predictor.py 1

will read:

    Match_1

## Output

The program generates:

    AI_Explorers_output.csv

The output contains:

| Player Name | Team   | C/VC |
|-------------|--------|------|
| Player 1    | Team A | C    |
| Player 2    | Team B | VC   |
| Player 3    | Team A | NA   |

Where:

- C = Captain
- VC = Vice-Captain
- NA = No Captain/Vice-Captain assignment

## Data Source

Historical player statistics are collected from ESPNcricinfo.

The project uses player IDs to retrieve individual batting, bowling, and fielding statistics.

The project depends on the current structure of ESPNcricinfo statistics pages. If the website structure changes, the scraping code may need to be updated.

## Important Notes

### Excel Input File

The Excel input file is excluded from the Git repository using `.gitignore`.

This keeps the repository lightweight and prevents local input data from being accidentally uploaded.

### Generated CSV

Generated CSV files are also excluded from Git using:

    *.csv

### Internet Connection

An active internet connection is required because the project fetches player statistics from ESPNcricinfo.

## Current Limitations

- The project is currently implemented mainly in a single Python file.
- The model is trained separately for each prediction.
- Predictions are primarily based on historical player statistics.
- Venue-specific performance is not currently considered.
- Opposition-specific performance is not currently considered.
- Error handling for failed web requests can be improved.
- The scraper depends on the structure of ESPNcricinfo pages.
- Model evaluation metrics have not yet been implemented.

## Future Improvements

- Split the project into multiple modules
- Add proper exception handling
- Add logging
- Add unit tests
- Add model evaluation metrics
- Include venue statistics
- Include opposition-specific statistics
- Include recent player form
- Include pitch and match conditions
- Experiment with different machine learning models
- Improve team selection constraints
- Automate data collection
- Build a web interface for predictions
- Move configuration values out of the source code

## Author

BALAJI IMANDI
https://github.com/balajiimandi2904
