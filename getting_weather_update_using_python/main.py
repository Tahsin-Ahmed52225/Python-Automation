from http.client import ResponseNotReady
import requests

API_KEY = "64875f82f482fc9a529978336241f4fc"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

lat = input("Enter a lat :")
lon = input("Enter a lon :")
requests_url = BASE_URL+"?lat="+lat+"&lon="+lon+"&appid="+API_KEY
response = requests.get(requests_url)


if response.status_code == 200:
    data = response.json()
    weather = data["weather"]
    temp = round(data['main']['temp'] -273.15,2)
    print("Weather:",weather)
    print("Tempeture:",temp,"celcius")

else:
    print("Something went wrong")