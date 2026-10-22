'''
Script to load geographical data into a pandas DataFrame,
and save it as a CSV file.
'''

from geopy.geocoders import Nominatim
import pandas as pd


def get_geolocator(agent='h501-student'):
    """
    Initiate a Nominatim geolocator instance given an `agent`.

    Parameters
    ----------
    agent : str, optional
        Agent name for Nominatim, by default 'h501-student'
    """
    return Nominatim(user_agent=agent, timeout=10)

def fetch_location_data(geolocator, loc):
    '''
    Use geolocator to fetch data for a given location, and return
    a dictionary with that data. For invalid locations, fill null values.
    '''
    try:
        location = geolocator.geocode(loc)

    except AttributeError as e:
        print(f"-- {e} --:\n\t-->", loc)
        return None
    
    if location is None:
        print("Location is None:\n\t-->", loc)
        return {"location": loc,
                "latitude": None,
                "longitude": None,
                "type": None}
            
    return {"location": loc,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "type": location.raw['type']}

def build_geo_dataframe(locations, geo):
    '''
    Call fetch_location_data for a list of locations and return a pandas
    DataFrame with the resulting data.
    '''
    geo_data = [fetch_location_data(geo, loc) for loc in locations]
    return pd.DataFrame(row for row in geo_data if row is not None)


if __name__ == "__main__":
    geo = get_geolocator()

    locations = ["Museum of Modern Art",
                 "iuyt8765(*&)", "Alaska",
                 "Franklin's Barbecue",
                 "Burj Khalifa"]

    df = build_geo_dataframe(locations, geo)

    df.to_csv("./geo_data.csv")
