import requests

url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/stories/list"

querystring = {"template":"CURRENCY","id":"usdjpy"}

headers = {
	"X-RapidAPI-Key": "eb21bd951dmshaed0488412b34a8p117709jsnf792d21be51a",
	"X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())