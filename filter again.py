import pandas as pd
import matplotlib as plt

columns = ["row_num","star_name","distance","mass","radius","gravity"]
df  = pd.read_csv("main1.csv",names=columns)
df = df.iloc[1: , :]
del df["row_num"]

distance = df["distance"].tolist()
distance.pop(0)
distance_list = []
for data in distance:
    if float(data) < 100.0:
        distance_list.append(data)


for index,data in enumerate(distance_list):
    df.at[index,"distance"] = data

gravity = df["gravity"].tolist()
gravity.pop(0)
gravity_list = []
for data in gravity:
    if float(data) >150.0 and float(data)<350.0:
        gravity_list.append(data)


for index,data in enumerate(gravity_list):
    df.at[index,"gravity"] = data

df = df[df["mass"].notna()]
df = df[df["radius"].notna()]
df = df[df["distance"].notna()]
df = df[df["star_name"].notna()]
df = df[df["gravity"].notna()]

df.to_csv("main3.csv")

