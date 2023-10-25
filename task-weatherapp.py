import requests, json
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


owm = OWM('0e0ae0e9399b2438109ede2a43cbba73')
mgr = owm.weather_manager()


observation = mgr.weather_at_place('city')
w = observation.weather

w.detailed_status         
w.wind()                  

api_key = "0e0ae0e9399b2438109ede2a43cbba73"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

	y = x["main"]

	current_temperature = y["temp"]

	current_humidity = y["humidity"]

	z = x["weather"]

	weather_description = z[0]["description"]

	print("Current Conditions:" +
					str(weather_description) +
	    "\nTemperature: " +
					str(current_temperature) +
		"\nHumidity: " +
					str(current_humidity) +
		"\nWind Speed: " + 
		            str(w.wind()) +
		"\nShort Forecast: " + 
		            str(w.detailed_status))

else:
	print(" City Not Found ")
