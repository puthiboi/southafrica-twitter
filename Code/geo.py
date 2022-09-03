from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np

geolocator = Nominatim(user_agent="southafrica_test")

df = pd.read_csv("bigfileSA .csv")
df.drop_duplicates(subset=['screen_name'], keep='first', inplace=True)
print(df.shape)
df['location'].replace('', np.nan, inplace=True)
df.dropna(subset=['location'], inplace=True)
print(df.shape)
df_len = len(df)

location_list = df['location'].tolist()
long, lat = [], []
count = 0
for loc in location_list:
    try:
        location = geolocator.geocode(loc)
        lat.append(location.latitude)
        long.append(location.longitude)
        
        print((location.latitude, location.longitude))
    except:
        print("No location found")
        lat.append("No location found")
        long.append("No location found")
        pass
        
    count += 1
    print(count / df_len * 100, "%")


df["latidude"] = lat
df["longitude"] = long

df.to_csv ("bigfileloca.csv", index = False, header=True)



