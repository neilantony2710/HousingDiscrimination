# Import
import numpy as np
import pandas as pd

# Loading data into chunks (neccesary due to large size of data file)
reader = pd.read_csv("data/2022_public_lar.csv", chunksize=1000000, low_memory=False)

# Pre-Processing Chunks 
chunks = []
for chunk in reader:
    chunks.append(chunk)

# Combining Chunks to one data frame
df = pd.concat(chunks)
print(df.shape)

# Splitting data into two dataframes, one for white applicants, and one for black applicants
W = df[df["applicant_race_1"] == 5]
B = df[df["applicant_race_1"] == 3]


# Generating percentages of applicants denied based on race

# Raw percentages
def rawData(whiteData, blackData):
    whiteDenied = whiteData[whiteData["action_taken"] == 3]
    blackDenied = blackData[blackData["action_taken"] == 3]
    whiteDeniedPercentage = len(whiteDenied) / len(whiteData)
    blackDeniedPercentage = len(blackDenied) / len(blackData)
    return [whiteDeniedPercentage, blackDeniedPercentage]

# Controlling the data for income, then finding the percentage of applicants denied 
def normalizedIncomeData(whiteData, blackData):
    whiteDenied = whiteData[whiteData["action_taken"] == 3]
    blackDenied = blackData[blackData["action_taken"] == 3]
    whiteGroups = []
    blackGroups = []
    whiteGroups.append(
        len(whiteDenied[whiteDenied["income"] < 10])
        / len(whiteData[whiteData["income"] < 10])
    )
    blackGroups.append(
        len(blackDenied[blackDenied["income"] < 10])
        / len(blackData[blackData["income"] < 10])
    )

    for i in range(1, 10):
        wDenied = whiteDenied[
            (whiteDenied["income"] >= (i * 10))
            & (whiteDenied["income"] < ((i + 1) * 10))
        ]

        bDenied = blackDenied[
            (blackDenied["income"] >= (i * 10))
            & (blackDenied["income"] < ((i + 1) * 10))
        ]

        wTotal = whiteData[
            (whiteData["income"] >= (i * 10)) & (whiteData["income"] < ((i + 1) * 10))
        ]

        bTotal = blackData[
            (blackData["income"] >= (i * 10)) & (blackData["income"] < (i + 1) * 10)
        ]

        whiteGroups.append((len(wDenied) / len(wTotal)))
        blackGroups.append((len(bDenied) / len(bTotal)))

    whiteGroups.append(
        len(whiteDenied[whiteDenied["income"] >= 100])
        / len(whiteData[whiteData["income"] >= 100])
    )

    blackGroups.append(
        len(blackDenied[blackDenied["income"] >= 100])
        / len(blackData[blackData["income"] >= 100])
    )

    return [whiteGroups, blackGroups]

# Normalizing the data for debt to income ratio, then finding the percentage of applicants denied 
def normalizedDTIData(whiteData, blackData):
    whiteDenied = whiteData[whiteData["action_taken"] == 3]
    blackDenied = blackData[blackData["action_taken"] == 3]
    whiteGroups = []
    blackGroups = []
    wDenied = 0
    bDenied = 0
    wTotal = 0
    bTotal = 0

    # DTI < 20%
    wDenied = len(whiteDenied[whiteDenied["debt_to_income_ratio"] == "<20%"])
    bDenied = len(blackDenied[blackDenied["debt_to_income_ratio"] == "<20%"])
    wTotal = len(whiteData[whiteData["debt_to_income_ratio"] == "<20%"])
    bTotal = len(blackData[blackData["debt_to_income_ratio"] == "<20%"])
    if wTotal <= 0:
        whiteGroups.append(-1)
    else:
        whiteGroups.append(wDenied / wTotal)
    if bTotal <= 0:
        blackGroups.append(-1)
    else:
        blackGroups.append(bDenied / bTotal)

    # 20% < DTI < 30%
    wDenied = len(whiteDenied[whiteDenied["debt_to_income_ratio"] == "20%-<30%"])
    bDenied = len(blackDenied[blackDenied["debt_to_income_ratio"] == "20%-<30%"])
    wTotal = len(whiteData[whiteData["debt_to_income_ratio"] == "20%-<30%"])
    bTotal = len(blackData[blackData["debt_to_income_ratio"] == "20%-<30%"])
    if wTotal <= 0:
        whiteGroups.append(-1)
    else:
        whiteGroups.append(wDenied / wTotal)
    if bTotal <= 0:
        blackGroups.append(-1)
    else:
        blackGroups.append(bDenied / bTotal)

    # 30% < DTI < 40%
    wDenied = len(whiteDenied[whiteDenied["debt_to_income_ratio"] == "30%-<36%"])
    bDenied = len(blackDenied[blackDenied["debt_to_income_ratio"] == "30%-<36%"])
    wTotal = len(whiteData[whiteData["debt_to_income_ratio"] == "30%-<36%"])
    bTotal = len(blackData[blackData["debt_to_income_ratio"] == "30%-<36%"])
    for i in range(36, 40):
        ii = str(i)
        wDenied += len(whiteDenied[whiteDenied["debt_to_income_ratio"] == ii])
        wTotal += len(whiteData[whiteData["debt_to_income_ratio"] == ii])
        bDenied += len(blackDenied[blackDenied["debt_to_income_ratio"] == ii])
        bTotal += len(blackData[blackData["debt_to_income_ratio"] == ii])
    if wTotal <= 0:
        whiteGroups.append(-1)
    else:
        whiteGroups.append(wDenied / wTotal)
    if bTotal <= 0:
        blackGroups.append(-1)
    else:
        blackGroups.append(bDenied / bTotal)

    # 40% < DTI < 50%
    wDenied = 0
    bDenied = 0
    wTotal = 0
    bTotal = 0
    for i in range(40, 50):
        ii = str(i)
        wDenied += len(whiteDenied[whiteDenied["debt_to_income_ratio"] == ii])
        wTotal += len(whiteData[whiteData["debt_to_income_ratio"] == ii])
        bDenied += len(blackDenied[blackDenied["debt_to_income_ratio"] == ii])
        bTotal += len(blackData[blackData["debt_to_income_ratio"] == ii])
    if wTotal <= 0:
        whiteGroups.append(-1)
    else:
        whiteGroups.append(wDenied / wTotal)
    if bTotal <= 0:
        blackGroups.append(-1)
    else:
        blackGroups.append(bDenied / bTotal)

    # 50% < DTI < 60%
    wDenied = len(whiteDenied[whiteDenied["debt_to_income_ratio"] == "20%-<30%"])
    bDenied = len(blackDenied[blackDenied["debt_to_income_ratio"] == "20%-<30%"])
    wTotal = len(whiteData[whiteData["debt_to_income_ratio"] == "20%-<30%"])
    bTotal = len(blackData[blackData["debt_to_income_ratio"] == "20%-<30%"])
    if wTotal <= 0:
        whiteGroups.append(-1)
    else:
        whiteGroups.append(wDenied / wTotal)
    if bTotal <= 0:
        blackGroups.append(-1)
    else:
        blackGroups.append(bDenied / bTotal)

    # DTI > 60%
    wDenied = len(whiteDenied[whiteDenied["debt_to_income_ratio"] == ">60%"])
    bDenied = len(blackDenied[blackDenied["debt_to_income_ratio"] == ">60%"])
    wTotal = len(whiteData[whiteData["debt_to_income_ratio"] == ">60%"])
    bTotal = len(blackData[blackData["debt_to_income_ratio"] == ">60%"])
    if wTotal <= 0:
        whiteGroups.append(-1)
    else:
        whiteGroups.append(wDenied / wTotal)
    if bTotal <= 0:
        blackGroups.append(-1)
    else:
        blackGroups.append(bDenied / bTotal)

    return [whiteGroups, blackGroups]


# function to truncate all data values to 2 decimal places
def truncate(num):
    num = num * 10000
    num = int(num)
    num /= 100.0
    return num


# Writing to a file to access while building React Front-end
rawPercentages = rawData(W, B)
NIPercentages = normalizedIncomeData(W, B)
DTIPercentages = normalizedDTIData(W, B)

f = open("processed.txt", "w")
f.write("Raw")
f.write("\n")
f.write(str(truncate(rawPercentages[0])) + "," + str(truncate(rawPercentages[1])))
f.write("\n")
f.write("Normalized for Income")
f.write("\n")
f.write("White - [")
for i in range(0, 11):
    f.write(str(truncate(NIPercentages[0][i])))
    if i != 10:
        f.write(",")
f.write("]\n")
f.write("Black - [")
for i in range(0, 11):
    f.write(str(truncate(NIPercentages[1][i])))
    if i != 10:
        f.write(",")
f.write("]\n")

f.write("Normalized for DTI")
f.write("\n")
f.write("White - [")
for i in range(0, 6):
    f.write(str(truncate(DTIPercentages[0][i])))
    if i != 5:
        f.write(",")
f.write("]\n")
f.write("Black - [")
for i in range(0, 6):
    f.write(str(truncate(DTIPercentages[1][i])))
    if i != 5:
        f.write(",")
f.write("]\n")

