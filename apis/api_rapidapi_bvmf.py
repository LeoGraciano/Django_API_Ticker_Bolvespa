import requests
from typing import Dict


def get_ticker(ticker="PETR4") -> str:

    url = f"https://bvmf.p.rapidapi.com/bvmf/{ticker}"

    headers = {
        "X-RapidAPI-Host": "bvmf.p.rapidapi.com",
        "X-RapidAPI-Key": "44d04bf6e8msh63ae533faf01179p1004c4jsnab6f652a7f1e"
    }

    response = requests.request("GET", url, headers=headers)

    return response
