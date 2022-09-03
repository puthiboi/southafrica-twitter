from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np

"""
    geo.py takes a .csv containing the collected twitter data and tries to add 
    latitude and longitude data for every account within the dataframe.
"""

#### Initiate the geolocator app
geolocator = Nominatim(user_agent="southafrica_test")

#### Read and prepare the data

df = pd.read_csv("network_data.csv")
df.drop_duplicates(subset=['screen_name'], keep='first', inplace=True)
#print(df.shape)
df['location'].replace('', np.nan, inplace=True)
df.dropna(subset=['location'], inplace=True)
#print(df.shape)
df_len = len(df)

#### Add latitude & longitude data to the data frame

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

### Save to .csv File

df.to_csv ("location_map.csv", index = False, header=True)



