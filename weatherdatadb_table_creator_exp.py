import math
import os
import random

from sympy import *

'''
Python script that writes temperature values according to made up(and way too cyclical) weather model
Model consists of superposed sine waves that approximate daily median temperatures, and the daily model consists of a cosine wave
Temperature values are written to sql statements along with timestamps into a text file

'''

def format_date(day, month, year):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if((months.index(month) + 1) < 10):
        if(day < 10):
            date = "'" + str(year) + "0" + str(months.index(month) + 1) + "0" + str(day) + "'"
        else:
            date = "'" + str(year) + "0" + str(months.index(month) + 1) + str(day) + "'"
    else:
        if(day < 10):
            date = "'" + str(year) + str(months.index(month) + 1) + "0" + str(day) + "'"
        else:
            date = "'" + str(year) + str(months.index(month) + 1) + str(day) + "'"

    return date

def format_time(i):

    if(i % 4 == 0):
        if(i / 4 < 10):
            time = "0" + str(int(i / 4)) + "0000"
        else:
            time = str(int(i / 4)) + "0000"
    else:
        if(i / 4 < 10):
            time = "0" + str(i // 4) + str((i % 4) * 15) + "00"
        else:
            time = str(i // 4) + str((i % 4) * 15) + "00"

    return time

def format_temp(i, slope, median_temp):
    #temperature datapoints follow cosine curve y = 2*cos(x*(2*PI/95)+0.7*PI)+20 where x is datapoint and y is the temperature value
    data_points_per_day = 96
    temp = str(2 * math.cos(i * (2 * math.pi/data_points_per_day) + 0.7 * math.pi) * random.uniform(0.8, 1.2) + slope * i/data_points_per_day + median_temp)
    return temp

def main():

    random.seed()

    if os.path.exists("dummyweatherdata_year.txt"):
        os.remove("dummyweatherdata_year.txt")
        print("File removed\n")
    else:
        print("File does not exists\n")


    file = open("dummyweatherdata_year.txt", "w+")

    # sql statements to create database and table
    # file.write("DROP DATABASE dummyweatherdatadb;\n")
    file.write("CREATE DATABASE IF NOT EXISTS dummyweatherdatadb;\n")
    file.write("USE dummyweatherdatadb;\n")
    file.write("DROP TABLE IF EXISTS weatherdata;\n")
    file.write("CREATE TABLE IF NOT EXISTS weatherdata (date DATE NOT NULL, time TIME NOT NULL, temperature FLOAT(24) NOT NULL);\n")

    days30 = ["April", "June", "September", "November"] # list of months with 30 days
    days31 = ["January", "March", "May", "July", "August", "October", "December"] # list of months with 31 days
    days29 = ["February"] # list of months with 29 days(leap year in 2020, must be edited if non-leap year is used)

    months = ["July", "August", "September", "October", "November", "December", "January", "February", "March", "April", "May", "June"] # months to iterate through
    year = 2019 # starting year, changes if January is not the first item in the months list
    days = 366  # days in a year including leap year day

    k = 0   # starting month index
    current_month = months[k] # the month that cycles
    days_spent = 0 # keeps count of the days that are spent, used to identify when the month changes
    data_points_per_day = 96 # number of datapoints in a day

    # possible temperature curves y1, y2 etc.
    # y1=15*sin(x*(2*PI/366)+c*PI)-15*sin(x*(2*3*PI/366)+d*PI)/3+2.5*sin(x*(2*20*PI/366)) // c=2.5, d=1.4, median_temp of the day, day has its own temp curve
    # https://www.mathopenref.com/graphfunctions.html?fx=15*sin(x*(2*PI/366)+c*PI)-15*sin(x*(2*3*PI/366)+d*PI)/3+2.5*sin(x*(2*20*PI/366))&xh=400&xl=-400&yh=30&yl=-30&a=0.9787234042553191&c=2.5&d=1.4
    # y2=15*sin(x*(2*PI/366)+c*PI)-15*sin(x*(2*3*PI/366)+d*PI)/3-2.5*sin(x*(2*20*PI/366))+15*sin(x*(2*5*PI/366)+a*PI)/5+15*sin(x*(2*7*PI/366)+b*PI)/7+5 // c=2.5, d=1.4, a=1.7, b=1.9
    # y3=15*sin(x*(2*PI/366)+a*PI)-15*sin(x*(2*3*PI/366)+b*PI)/3+15*sin(x*(2*5*PI/366)+c*PI)/5+15*sin(x*(2*7*PI/366)+d*PI)/7+2*sin(x*(2*20*PI/366))+6 // a=2.5, b=1.4, c=1.5, d=1.4
    # https://www.mathopenref.com/graphfunctions.html?fx=&gx=15 * sin(x * (2 * pi/366) + 2.5 * pi) - 15 * sin(x * (6 * pi/366) + 1.4 * pi) / 3 + 15 * sin(x * (10 * pi/366) + 1.7 * pi) / 5 + 15 * sin(x * (14 * pi/366) + 1.9 * pi)/7 - 2.5 * sin(x * (40 * pi/366)) + 5&hx=15*sin(x*(2*PI/366)+a*PI)-15*sin(x*(2*3*PI/366)+b*PI)/3+15*sin(x*(2*5*PI/366)+c*PI)/5+15*sin(x*(2*7*PI/366)+d*PI)/7+2*sin(x*(2*20*PI/366))+6&xh=400&xl=-400&yh=30&yl=-30&a=2.5&b=1.4&c=1.5&d=1.4

    a = 2.5
    b = 1.4
    c = 1.5
    d = 1.4

    for j in range(days):
        daily_median_temp = 15 * math.sin(j * (2 * math.pi/366) + a * math.pi) - 15 * math.sin(j * (6 * math.pi/366) + b * math.pi) / 3 + 15 * math.sin(j * (10 * math.pi/366) + c * math.pi) / 5 + 15 * math.sin(j * (14 * math.pi/366) + d * math.pi) / 7 + 2 * math.sin(j * (40 * math.pi/366)) + 6
        # gives the median temperature for the day
        # daily_median_temp = 15 * math.sin(j * (2 * math.pi/366) + 2.5 * math.pi) - 15 * math.sin(j * (6 * math.pi/366) + 1.4 * math.pi) / 3 + 15 * math.sin(j * (10 * math.pi/366) + 1.7 * math.pi) / 5 + 15 * math.sin(j * (14 * math.pi/366) + 1.9 * math.pi)/7 - 2.5 * math.sin(j * (40 * math.pi/366)) + 5

        x = Symbol('x')
        f_diff = diff(15 * sin(x * (2 * pi/366) + a * pi) - 15 * sin(x * (6 * pi/366) + b * pi) / 3 + 15 * sin(x * (10 * pi/366) + c * pi) / 5 + 15 * sin(x * (14 * pi/366) + d * pi) / 7 + 2 * sin(x * (40 * pi/366)) + 6, x)
        #f_diff = diff(15 * sin(x * (2 * pi/366) + 2.5 * pi) - 15 * sin(x * (6 * pi/366) + 1.4 * pi) / 3 + 15 * sin(x * (10 * pi/366) + 1.7 * pi) / 5 + 15 * sin(x * (14 * pi/366) + 1.9 * pi)/7 - 2.5 * sin(x * (40 * pi/366)) + 5, x)
        slope = float(f_diff.subs(x, j))

        days_spent += 1

        for i in range(data_points_per_day):
            # sql statement to create datapoints
            file.write("INSERT INTO weatherdata (date, time, temperature) VALUES ({}, {}, {});\n".format(format_date(days_spent, current_month, year), format_time(i), format_temp(i, slope, daily_median_temp)))

        if current_month in days31 and days_spent == 31:
            days_spent = 0
            k += 1
            if k < len(months):
                current_month = months[k]
                if current_month == "January" and months.index("January") != 0:
                    year += 1
        elif current_month in days30 and days_spent == 30:
            days_spent = 0
            k += 1
            if k < len(months):
                current_month = months[k]
        elif current_month in days29 and days_spent == 29:
            days_spent = 0
            k += 1
            if k < len(months):
                current_month = months[k]

    file.close()

if __name__ == "__main__":
    main()
