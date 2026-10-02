spinnersList = [
    "Noor Ahmad","Mukesh Choudhary","Shreyas Gopal","Ravichandran Ashwin",
    "Ravindra Jadeja","Tripurana Vijay","Vipraj Nigam","Kuldeep Yadav",
    "Axar Patel","Nishant Sindhu","Manav Suthar","Ravisrinivasan Sai Kishore",
    "Washington Sundar","Glenn Phillips","Rashid-Khan" ,"Jayant Yadav","Rahul Tewatia",
    "Mayank Markande","Varun Chakravarthy","Anukul Sudhakar Roy","Moeen Ali","Sunil Narine",
    "Digvesh Singh","Yuvraj Chaudhary","Ravi Bishnoi","Shahbaz Ahmed","Manimaran Siddharth",
    "Aiden Markram","Naman Dhir","Vignesh Puthur","Mujeeb-ur-Rahman","Will Jacks","Mitchell Santner",
    "Karn Sharma","Musheer Khan","Musheer Khan","Pravin Dubey","Yuzvendra Chahal","Glenn Maxwell","Mohit Rathee",
    "Suyash Sharma","Krunal Pandya","Liam Livingstone","Swapnil Singh","Maheesh Theekshana","Wanindu Hasaranga","Nitish Rana",
    "Rahul Chahar","Abhishek Sharma","Kamindu Mendis","Zeeshan Ansari","Adam Zampa"
]

mapId = {
    "Vansh Bedi": 1413379, "Andre Siddharth": 1440190, "Ramakrishna Ghosh": 1339053, "Shaik Rasheed": 1292497, 
    "Gurjapneet Singh": 1269869, "Matheesha Pathirana": 1194795, "Noor Ahmad": 1182529, "Anshul Kamboj": 1175428, 
    "Nathan Ellis": 826915, "Mukesh Choudhary": 1125688, "Ruturaj Gaikwad": 1060380, "Kamlesh Nagarkoti": 1070188, 
    "Rachin Ravindra": 959767, "Khaleel Ahmed": 942645, "Shivam Dube": 714451, "Rahul Tripathi": 446763, 
    "Sam Curran": 662973, "Shreyas Gopal": 344580, "Deepak Hooda": 497121, "Devon Conway": 379140, 
    "Jamie Overton": 510530, "Vijay Shankar": 477021, "Ravichandran Ashwin": 26421, "Ravindra Jadeja": 234675, 
    "MS Dhoni": 28081, "Madhav Tiwari": 1460385, "Manvanth Kumar L": 1392186, "Tripurana Vijay": 1292527, 
    "Vipraj Nigam": 1449074, "Tristan Stubbs": 595978, "Abishek Porel": 1277545, "Ashutosh Sharma": 1131978, 
    "Donovan Ferreira": 698315, "Sameer Rizvi": 1175489, "Jake Fraser-McGurk": 1168049, "Ajay Mandal": 1059570, 
    "Darshan Nalkande": 1111917, "T Natarajan": 802575, "Mukesh Kumar": 926851, "Kuldeep Yadav": 559235, 
    "Mohit Sharma": 537119, "Lokesh Rahul": 422108, "Axar Patel": 554691, "Dushmantha Chameera": 552152, 
    "Karun Nair": 398439, "Faf du Plessis": 44828, "Mitchell Starc": 311592, "Gurnoor Brar Singh": 1287033, 
    "Nishant Sindhu": 1292506, "Arshad Khan": 1244751, "Sai Sudharsan": 1151288, "Kumar Kushagra": 1207295, 
    "Manav Suthar": 1175426, "Sherfane Rutherford": 914541, "Gerald Coetzee": 596010, "Anuj Rawat": 1123073, 
    "Kulwant Khejroliya": 1083033, "Shubman Gill": 1070173, "Ravisrinivasan Sai Kishore": 1048739, 
    "Mahipal Lomror": 853265, "Karim Janat": 793467, "Washington Sundar": 719715, "Shahrukh Khan": 719719, 
    "Mohammed Siraj": 940973, "Glenn Phillips": 823509, "Rashid-Khan": 793463, "Prasidh Krishna": 917159, 
    "Jayant Yadav": 447587, "Rahul Tewatia": 423838, "Kagiso Rabada": 550215, "Jos Buttler": 308967, 
    "Ishant Sharma": 236779, "Harshit Rana": 1312645, "Angkrish Raghuvanshi": 1292495, "Vaibhav Arora": 1209292, 
    "Luvnith Sisodia": 1155253, "Mayank Markande": 1081442, "Chetan Sakariya": 1131754, "Rahmanullah Gurbaz": 974087, 
    "Spencer Johnson": 1123718, "Varun Chakravarthy": 1108375, "Anrich Nortje": 481979, "Anukul Sudhakar Roy": 1079839, 
    "Ramandeep Singh": 1079470, "Rovman Powell": 820351, "Rinku Singh": 723105, "Venkatesh Iyer": 851403, 
    "Moeen Ali": 8917, "Quinton de Kock": 379143, "Andre Russell": 276298, "Sunil Narine": 230558, 
    "Manish Pandey": 290630, "Ajinkya Rahane": 277916, "Umran Malik": 1246528, "Digvesh Singh": 1460529, 
    "Prince Yadav": 1300836, "Shamar Joseph": 1356971, "Mayank Yadav": 1292563, "Arshin Kulkarni": 1403153, 
    "Akash Deep": 1176959, "Akash Singh": 1175458, "Yuvraj Chaudhary": 1175463, "Ravi Bishnoi": 1175441, 
    "Abdul Samad": 1175485, "Shahbaz Ahmed": 1159711, "Rajvardhan Hangargekar": 1175429, "Ayush Badoni": 1151270, 
    "Aryan Juyal": 1130300, "Mohsin Khan": 1132005, "Matthew Breetzke": 595267, "Manimaran Siddharth": 1151286, 
    "Rishabh Pant": 931581, "Himmat Singh": 805235, "Aiden Markram": 600498, "Avesh Khan": 694211, 
    "Nicholas Pooran": 604302, "David Miller": 321777, "Mitchell Marsh": 272450, "Bevon Jacobs": 1410577, 
    "Naman Dhir": 1287032, "Robin Minz": 1350762, "Raj Angad Bawa": 1292502, "Vignesh Puthur": 1460388, 
    "Satyanarayana Raju": 1392201, "Ashwani Kumar": 1209126, "Tilak Varma": 1170265, "KL Shrijith": 778241, 
    "Mujeeb-ur-Rahman": 974109, "Ryan Rickelton": 605661, "Arjun Tendulkar": 1148776, "Will Jacks": 897549, 
    "Hardik Pandya": 625371, "Mitchell Santner": 502714, "Reece Topley": 461632, "Corbin Bosch": 594322, 
    "Jasprit Bumrah": 625383, "Trent Boult": 277912, "Suryakumar Yadav": 446507, "Deepak Chahar": 447261, 
    "Karn Sharma": 30288, "Rohit Sharma": 34102, "Musheer Khan": 1316430, "Harnoor Singh Pannu": 1292496, 
    "Pyla Avinash": 1324449, "Suryansh Shedge": 1339698, "Harpreet Brar": 1168641, "Priyansh Arya": 1175456, 
    "Kuldeep Sen": 1163695, "Marco Jansen": 696401, "Nehal Wadhera": 1151273, "Prabhsimran Singh": 1161024, 
    "Aaron Hardie": 1124283, "Arshdeep Singh": 1125976, "Azmatullah Omarzai": 819429, "Vishnu Vinod": 732293, 
    "Xavier Bartlett": 1050545, "Shashank Singh": 377534, "Lockie Ferguson": 493773, "Josh Inglis": 662235, 
    "Vyshak Vijaykumar": 777815, "Pravin Dubey": 777515, "Yash Thakur": 1070196, "Shreyas Iyer": 642519, 
    "Marcus Stoinis": 325012, "Yuzvendra Chahal": 430246, "Glenn Maxwell": 325026, "Abhinandan Singh": 1449085, 
    "Swastik Chikara": 1403198, "Mohit Rathee": 1349361, "Suyash Sharma": 1350792, "Jacob Bethell": 1194959, 
    "Rasikh Salam": 1161489, "Yash Dayal": 1159720, "Manoj Bhandage": 1057399, "Nuwan Thushara": 955235, 
    "Romario Shepherd": 677077, "Tim David": 892749, "Devdutt Padikkal": 1119026, "Krunal Pandya": 471342, 
    "Rajat Patidar": 823703, "Jitesh Sharma": 721867, "Lungi Ngidi": 542023, "Philip Salt": 669365, 
    "Liam Livingstone": 403902, "Josh Hazlewood": 288284, "Bhuvneshwar Kumar": 326016, "Swapnil Singh": 232292, 
    "Virat Kohli": 253802, "Vaibhav Suryavanshi": 1408688, "Ashok Sharma": 1299879, "Kwena Maphaka": 1294342, 
    "Kunal Singh Rathore": 1339031, "Akash Madhwal": 1206039, "Shubham Dubey": 1252585, "Yudhvir Singh Charak": 1206052, 
    "Maheesh Theekshana": 1138316, "Dhruv Jurel": 1175488, "Kumar Kartikeya": 1159843, "Yashasvi Jaiswal": 1151278, 
    "FazalHaq Farooqi": 974175, "Riyan Parag": 1079434, "Tushar Deshpande": 822553, "Jofra Archer": 669855, 
    "Wanindu Hasaranga": 784379, "Nitish Rana": 604527, "Shimron Hetmyer": 670025, "Sandeep Sharma": 438362, 
    "Sanju Samson": 425943, "Aniket Verma": 1409976, "Eshan Malinga": 1306214, "K Nitish Reddy": 1175496, 
    "Abhinav Manohar": 778963, "Atharva Taide": 1125958, "Simarjeet- Singh": 1159722, "Rahul Chahar": 1064812, 
    "Abhishek Sharma": 1070183, "Kamindu Mendis": 784373, "Wiaan Mulder": 698189, "Zeeshan Ansari": 942371, 
    "Ishan Kishan": 720471, "Heinrich Klaasen": 436757, "Sachin Baby": 432783, "Travis Head": 530011, 
    "Adam Zampa": 379504, "Harshal Patel": 390481, "Pat Cummins": 489889, "Mohammed Shami": 481896, 
    "Jaydev Unadkat": 390484, "Shardul Thakur": 475281,'Ayush Mhatre': 1452455,'Dewald Brevis': 1070665,
}

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import xgboost as xgb
import warnings
import csv
import argparse
import os

warnings.filterwarnings("ignore", category=UserWarning)

def create_lag_features(data, lags):
    df_lags = pd.DataFrame({'target': data})
    for i in range(1, lags+1):
        df_lags[f'lag_{i}'] = df_lags['target'].shift(i)
    df_lags.dropna(inplace=True)
    df_lags["weight"] = 1 
    df_lags.loc[df_lags.index[-5:],'weight'] = 4
    return df_lags

def Predict(Data, lags):
    predictions = []
    if isinstance(Data, pd.Series):
        Data = Data.to_frame().T

    for col in Data.columns:
        data = Data[col]
        laggedData = create_lag_features(data,lags)
        if(len(laggedData) == 0) :
            p = [0] * 4
            return p
        x_train = laggedData.iloc[:,1:]
        y_train = laggedData.iloc[:,0]
        weights = laggedData['weight']
        test = laggedData.iloc[-1,:-1]
        dtrain = xgb.DMatrix(x_train, label=y_train, feature_names=x_train.columns.tolist(),weight=weights)
        dtest = xgb.DMatrix(test.values.reshape(1, -1), feature_names=x_train.columns.tolist())
        # laggedData = create_lag_features(data,lags)
        # if(len(laggedData) == 0):
        #     return [0] * 4

        # x_train = laggedData.drop(columns=['target', 'weight'])
        # y_train = laggedData['target']
        # weights = laggedData['weight']
        # test = laggedData.drop(columns=['target', 'weight']).iloc[-1]

        # dtrain = xgb.DMatrix(x_train, label=y_train, feature_names=x_train.columns.tolist(), weight=weights)
        # dtest = xgb.DMatrix(test.values.reshape(1, -1), feature_names=x_train.columns.tolist())
    
        params = {
            'objective': 'reg:squarederror',
            'max_depth': 5,
            'learning_rate': 0.1,
            'n_estimators': 100
        }
        model = xgb.train(params, dtrain, num_boost_round=100)
        y_pred = model.predict(dtest)
        predictions.append(y_pred[0])

    return predictions

def calcBattingPoints(arr) :
    points=0
    except_bound=arr[0]-arr[2]*4-arr[3]*6
    points=except_bound+arr[2]*8 +arr[3]*12
    if arr[0]>=25:
        points=points+4
    if arr[0]>=50:
        points=points+8
    if arr[0]>=75:
        points=points+12
    if arr[0]>=100:
        points=points+16
    if arr[1]>=10:
        if arr[4]>170:
            points=points+6
        if arr[4]<=170 and arr[4]>150.01:
            points=points+4
        if arr[4]<=150 and arr[4]>130:
            points=points+2
        if arr[4]<=70 and arr[4]>60:
            points=points-2
        if arr[4]<=59.99 and arr[4]>50:
            points=points-4
        if arr[4]<=50:
            points=points+6
    return points

def calcBowlingPoints(arr,playerName) :
    is_present = any(playerName in sublist for sublist in spinnersList)
    points=arr[1]*12 + arr[2]*30
    if(not is_present) :
        points += 4
    if arr[2]==3:
        points=points+4
    if arr[2]==4:
        points=points+8
    if arr[2]==5:
        points=points+12
    if arr[0]>2:
        if arr[3]<5:
            points=points+6
        if arr[3]>5 and arr[3]<=5.99:
            points=points+4
        if arr[3]>6 and arr[3]<=7:
            points=points+2
        if arr[3]>10 and arr[3]<=11:
            points=points-2
        if arr[3]>11.01 and arr[3]<=12:
            points=points-4
        if arr[3]>12 :
            points=points-6
    return points

def calcFeildingPoints(arr):
    points=arr[0]*8
    return points

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

import sys

matchNumber = sys.argv[1]

def getStats(url) :
        res = requests.get(url,headers=headers)
        soup = BeautifulSoup(res.text,"html.parser")
        data = soup.find_all("table",class_="engineTable")

        data = data[3]
        heading = []
        header_row = data.find("thead").find("tr")  

        for th in header_row.find_all("th"):
                header_text = th.get_text(strip=True)
                heading.append(header_text)

        stats = []
        for tr in data.find("tbody").find_all("tr") :
                arr = []
                for i in tr.find_all("td") :
                        arr.append(i.get_text(strip=True))
                stats.append(arr)

        df = pd.DataFrame(stats,columns=heading)
        return df

def fetchData_batting(playerId,playerType) :
        if playerType == "BAT" or playerType == "WK" or playerType =="ALL":
                battingUrl = f"https://stats.espncricinfo.com/ci/engine/player/{playerId}.html?class=6;host=6;orderby=start;orderbyad=reverse;template=results;type=batting;view=innings"
                playerStats = getStats(battingUrl)
                return playerStats

def fetchData_bowling(playerId, playerType):
        if playerType == "BOWL" or playerType=="ALL":
                bowlingUrl = f"https://stats.espncricinfo.com/ci/engine/player/{playerId}.html?class=6;host=6;orderby=start;orderbyad=reverse;template=results;type=bowling;view=innings"
                playerStats = getStats(bowlingUrl)
                return playerStats

def fetchData_fielding(playerId, playerType):
        fieldingUrl = f"https://stats.espncricinfo.com/ci/engine/player/{playerId}.html?class=6;host=6;orderby=start;orderbyad=reverse;template=results;type=fielding;view=innings"
        playerStats = getStats(fieldingUrl)
        return playerStats
            
def filter_rows(row):
    if any(str(cell).isalpha() for cell in row):
        return False
    if sum(cell == '-' for cell in row) > 4:
        return False
    return True

def safeConvert(value):
    try :
          return float(value)
    except :
          return np.nan

filePath = "SquadPlayerNames_IndianT20League.xlsx"
squadData = pd.read_excel(filePath, sheet_name=f"Match_{matchNumber}")
squadData.head()

fantasyPoints = {}
playerArr = {}
teamDict = {}

for index , row in squadData.iterrows() : 
        playerName = row["Player Name"]
        is_present = any(playerName in sublist for sublist in mapId)
        if(not is_present) :
            continue
        status = row["IsPlaying"]
        if status == "PLAYING" :
                playerArr.update({playerName : row["Player Type"]})
                teamDict.update({playerName : row["Team"]})
                statsData = fetchData_fielding(mapId[playerName],row["Player Type"])
                statsData = statsData["Dis"]
                statsData = statsData.to_frame()
                statsData = statsData.apply(safeConvert)
                statsData.fillna(statsData.mean(numeric_only=True),inplace=True)
                statsData = statsData.iloc[0:min(len(statsData),30)]
                statsData = statsData.iloc[::-1]
                fielding_points = calcFeildingPoints(Predict(statsData,5))
                if row["Player Type"]=="BAT" or row["Player Type"]=="WK" or row["Player Type"]=="ALL":
                        statsData = fetchData_batting(mapId[playerName],row["Player Type"])
                        unnecessary_col=["Mins","Pos","Dismissal","Inns","Opposition","Ground","Start Date",""]
                        statsData=statsData.drop(unnecessary_col,axis=1)
                        threshold = len(statsData.columns)/2
                        statsData=statsData.dropna(thresh=threshold+1)
                        statsData=statsData[statsData.apply(filter_rows,axis=1)]
                        statsData = statsData.apply(safeConvert)
                        statsData.fillna(statsData.mean(numeric_only=True),inplace=True)
                        statsData = statsData.iloc[0:min(len(statsData),30)]
                        statsData = statsData.iloc[::-1]
                        points = calcBattingPoints(Predict(statsData,5))
                        points=points + fielding_points
                        fantasyPoints.update({playerName : points})
                        if row["Player Type"]=="ALL":
                                statsData = fetchData_bowling(mapId[playerName],row["Player Type"])
                                unnecessary_col=["Runs","Pos","Inns","Opposition","Ground","Start Date",""]
                                statsData=statsData.drop(unnecessary_col,axis=1)
                                threshold = len(statsData.columns)/2
                                statsData=statsData.dropna(thresh=threshold+1)
                                statsData=statsData[statsData.apply(filter_rows,axis=1)]
                                statsData = statsData.apply(safeConvert)
                                statsData.fillna(statsData.mean(numeric_only=True),inplace=True)
                                statsData = statsData.iloc[0:min(len(statsData),30)]
                                statsData = statsData.iloc[::-1]
                                points = points + calcBowlingPoints(Predict(statsData,5),playerName)
                                fantasyPoints.update({playerName : points})
                elif row["Player Type"]=="BOWL":
                        statsData = fetchData_bowling(mapId[playerName],row["Player Type"])
                        unnecessary_col=["Runs","Pos","Inns","Opposition","Ground","Start Date",""]
                        statsData=statsData.drop(unnecessary_col,axis=1)
                        threshold = len(statsData.columns)/2
                        statsData=statsData.dropna(thresh=threshold+1)
                        statsData=statsData[statsData.apply(filter_rows,axis=1)]
                        statsData = statsData.apply(safeConvert)
                        statsData.fillna(statsData.mean(numeric_only=True),inplace=True)
                        statsData = statsData.iloc[0:min(len(statsData),30)]
                        statsData = statsData.iloc[::-1]
                        points = calcBowlingPoints(Predict(statsData,5),playerName)
                        points=points+fielding_points
                        fantasyPoints.update({playerName : points})

output_path = "/AI_Explorers_output.csv"
sortedData = sorted(fantasyPoints.items(),key=lambda x:x[1],reverse=True)

finalData = []
teamList = []

isBowler, isBatter, isAllrounder, isWk = False, False, False, False

processed_names = set()

for i in range(2):
    name, _ = sortedData[i]
    finalData.append(name)
    teamList.append(teamDict[name])
    processed_names.add(name)
    role = playerArr[name]
    if role == "BOWL":
        isBowler = True
    elif role == "ALL":
        isAllrounder = True
    elif role == "WK":
        isWk = True
    else:
        isBatter = True

if not isBowler:
    for name, val in sortedData[2:]:
        if name not in processed_names and playerArr[name] == "BOWL":
            finalData.append(name)
            teamList.append(teamDict[name])
            processed_names.add(name)
            break

if not isBatter:
    for name, val in sortedData[2:]:
        if name not in processed_names and playerArr[name] == "BAT":
            finalData.append(name)
            teamList.append(teamDict[name])
            processed_names.add(name)
            break

if not isWk:
    for name, val in sortedData[2:]:
        if name not in processed_names and playerArr[name] == "WK":
            finalData.append(name)
            teamList.append(teamDict[name])
            processed_names.add(name)
            break

if not isAllrounder:
    for name, val in sortedData[2:]:
        if name not in processed_names and playerArr[name] == "ALL":
            finalData.append(name)
            teamList.append(teamDict[name])
            processed_names.add(name)
            break

for name, val in sortedData[2:]:
    if len(finalData) == 15:
        break
    if name not in processed_names:
        finalData.append(name)
        teamList.append(teamDict[name])
        processed_names.add(name)

output_df = {
    "Player Name": finalData,
    "Team": teamList,
    "C/VC": ["C", "VC"] + ["NA"] * 13,
}

df = pd.DataFrame(output_df)

print(df)

df.to_csv(output_path,index=False)
