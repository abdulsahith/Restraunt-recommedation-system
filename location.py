import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from geopy.distance import geodesic

df_hotels=pd.read+_csv('pothumada.csv')

def calculate_distance(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).kilometers


user_location = (11.264977064601846, 77.60187695291722)


X = df_hotels[['Latitude', 'Longitude']]


knn = NearestNeighbors(n_neighbors=3, algorithm='ball_tree', metric='haversine')


X_rad = np.radians(X)


knn.fit(X_rad)


user_location_rad = np.radians([user_location])


distances, indices = knn.kneighbors(user_location_rad)


distances_km = distances * 6371


nearest_hotels = df_hotels.iloc[indices[0]]


nearest_hotels['distance_km'] = distances_km[0]

print(nearest_hotels[['Restaurant Name', 'Rating','City','Address', 'distance_km']])



print(calculate_distance(11.26495749922651,77.60175777568693,11.266092220497912, 77.60056796548936))
df_hotels.head()
