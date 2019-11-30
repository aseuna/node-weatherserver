
import math
import os
import random

def formatTime(i):
    
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

def formatTemp(i):
    #temperature datapoints follow cosine curve y = 2*cos(x*(2*PI/95)+0.7*PI)+20 where x is datapoint and y is the temperature value
    random.seed()
    temp = str((2 * math.cos(i * (2*math.pi/96) + 0.7*math.pi) * random.uniform(0.8, 1.2) + 20))
    return temp

def main():

    if os.path.exists("dummyweatherdata.txt"):
        os.remove("dummyweatherdata.txt")
        print("File removed\n")
    else:
        print('File does not exists')


    file = open("dummyweatherdata.txt", "w+")

    file.write("drop database dummyweatherdatadb;\n")
    file.write("create database if not exists dummyweatherdatadb;\n")
    file.write("use dummyweatherdatadb;\n")
    file.write("create table if not exists dailydata (time time not null, temperature float(24) not null);\n")

    for i in range(96):

        file.write("insert into dailydata (time, temperature) values ({}, {});\n".format(formatTime(i), formatTemp(i)))

    file.close()

if __name__ == "__main__":
    main()