import pandas as pd

weather_data = pd.read_csv("/home/arttu/Koodaus/Visual-Studio-Code/Webkehitys/weather-server-node/api/python_util/weatherdata.csv")

print(weather_data.isnull().sum())
weather_data["pressure (hPa)"].fillna( method ='ffill', inplace = True) 
weather_data["humidity (%)"].fillna( method ='ffill', inplace = True) 
weather_data["temperature (degC)"].fillna( method ='ffill', inplace = True)

print(weather_data.isnull().sum())

weather_data.to_csv("weatherdata_cleaned.csv")