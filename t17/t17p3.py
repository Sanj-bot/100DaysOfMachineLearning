import requests

url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/get-cross-currencies"

querystring = {"id":"aed,aud,brl,cad,chf,cnh,cny,cop,czk,dkk,eur,gbp,hkd,huf,idr,ils,inr,jpy,krw,mxn,myr,nok,nzd,php,pln,rub,sek,sgd,thb,try,twd,usd,zar"}

headers = {
	"X-RapidAPI-Key": "eb21bd951dmshaed0488412b34a8p117709jsnf792d21be51a",
	"X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())