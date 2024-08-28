import requests
import os
from dotenv import load_dotenv

load_dotenv()

class Access:
    def __init__(self, query, country, sort, p_condition):
        try:
            self.url = "https://real-time-amazon-data.p.rapidapi.com/search"
            self.commons_parameters = {"query": query, "country": country, "sort_by": sort,
                                   "product_condition": p_condition, "is_prime": "false"}
            # Burada aslında query, page, country, sort_by, product_condition hepsi parametre olarak girecez.
            self.querystring = {}

            self.headers = {
            "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
            "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
            }
        except Exception as e: print(e)
    def responsefunc(self):
        self.querystring = {**self.commons_parameters, "page": "1"}
        response = requests.get(self.url, headers=self.headers, params=self.querystring).json()
        print(response)
        return response

