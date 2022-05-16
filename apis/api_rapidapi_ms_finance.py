import requests

url = "https://ms-finance.p.rapidapi.com/market/v2/auto-complete"

querystring = {"q":"PETR"}

headers = {
	"X-RapidAPI-Host": "ms-finance.p.rapidapi.com",
	"X-RapidAPI-Key": "44d04bf6e8msh63ae533faf01179p1004c4jsnab6f652a7f1e"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)