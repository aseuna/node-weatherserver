import pandas as pd

weather_data = pd.read_csv("/home/arttu/Koodaus/Visual-Studio-Code/Webkehitys/weather-server-node/api/python_util/saadata.csv")

print(weather_data.isnull().sum())
weather_data["ilmanpaine (hPa)"].fillna( method ='ffill', inplace = True) 
weather_data["suhteellinen kosteus (%)"].fillna( method ='ffill', inplace = True) 
weather_data["ilman lampotila (degC)"].fillna( method ='ffill', inplace = True)

print(weather_data.isnull().sum())