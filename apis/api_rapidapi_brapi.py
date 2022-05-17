import requests
import re
import json
import requests
from typing import Dict


def get_ticker(ticker=None) -> str:

    if not ticker or ticker == "PETR4":
        ticker = "PETR4,MGLU3"
    elif ticker == "MGLU3":
        ticker = "MGLU3,PETR4"
    elif not ',' in ticker:
        ticker = f"{ticker},PETR4"

    while True:
        url = f"https://brapi.p.rapidapi.com/api/quote/{ticker}"

        querystring = {"range": "1mo",
                       "fundamental": "true", "interval": "1d"}

        headers = {
            "X-RapidAPI-Host": "brapi.p.rapidapi.com",
            "X-RapidAPI-Key": "44d04bf6e8msh63ae533faf01179p1004c4jsnab6f652a7f1e"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        if 'error' in json.loads(response.text).keys() and "Não encontramos a ação" in json.loads(response.text).get('error'):
            rmv_ticker = json.loads(response.text).get(
                'error', None).replace("Não encontramos a ação ", "")
            ticker = re.sub(rmv_ticker, "", ticker)
            ticker = ticker.replace(",,", ",")
        else:
            # with open('list_ticker.json', 'w') as f:
            #     f.write(response.text)
            break

    return response


def list_ticker() -> str:
    url = "https://brapi.p.rapidapi.com/api/quote/list"

    querystring = {"sortBy":"volume","sortOrder":"desc","limit":"1000"}

    headers = {
        "X-RapidAPI-Host": "brapi.p.rapidapi.com",
        "X-RapidAPI-Key": "44d04bf6e8msh63ae533faf01179p1004c4jsnab6f652a7f1e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)


    return response
