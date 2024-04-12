import requests

url = "https://covid-193.p.rapidapi.com/countries"

headers = {
	"X-RapidAPI-Key": "eb21bd951dmshaed0488412b34a8p117709jsnf792d21be51a",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())