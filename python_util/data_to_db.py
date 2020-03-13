import os
import pandas as pd

def format_time(time):
    time = "'" + str(time) + ":00" + "'"
    return time

if os.path.exists("dummyweatherdata.sql"):
    os.remove("dummyweatherdata.sql")
    print("File removed\n")
else:
    print("File does not exists\n")

file = open("dummyweatherdata_year.sql", "w+")

# sql statements to create database and table
file.write("DROP DATABASE IF EXISTS dummyweatherdatadb;\n")
file.write("CREATE DATABASE IF NOT EXISTS dummyweatherdatadb;\n")
file.write("USE dummyweatherdatadb;\n")
file.write("DROP TABLE IF EXISTS weatherdata;\n")
file.write("CREATE TABLE IF NOT EXISTS weatherdata (date DATE NOT NULL, time TIME NOT NULL, temperature FLOAT(24) NOT NULL, humidity FLOAT(24) NOT NULL, pressure FLOAT(24) NOT NULL);\n")

weatherdata = pd.read_csv("/home/arttu/Koodaus/Visual-Studio-Code/Webkehitys/weather-server-node/api/python_util/weatherdata_cleaned.csv")

for index, row in weatherdata.iterrows():
    file.write("INSERT INTO weatherdata (date, time, temperature, humidity, pressure) VALUES ({}, {}, {}, {}, {});\n".format(row['date'], format_time(row['time']), row['temperature (degC)'], row['humidity (%)'], row['pressure (hPa)']))

file.close()