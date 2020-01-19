import pandas as pd

weather_data = pd.read_csv("saadata.csv")

print(weather_data.isnull().sum())

weather_data.close()