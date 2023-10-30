import requests
import pandas as pd


class Base:
    """
    Class that handles all connection to API object and returns dataframe from its initialization

    meothods:
    return_URL: shows url we are currently working with
    get_data: scrapes data from API and returns a dataframe

    """

    def __init__(self, url="https://api.scryfall.com/bulk-data"):
        self.__api_url = url  # dunder means nobody can call and look at it directly, but only if they call the see_url method
        self.get_data()  # yep! methods can be called on init!

    def get_data(self):
        """scrapes data from the api"""
        self.df = pd.DataFrame.from_dict(
            requests.get(
                requests.get(self.__api_url).json()["data"][0]["download_uri"]
            ).json()
        )
        return self.df

    def see_url(self):
        return self.__api_url


# if this file is run directly, do the following:

if __name__ == "__main__":
    c = Base()
    print(c.df)
