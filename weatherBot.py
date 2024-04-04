import requests
import datetime
def getResults(place):
	url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

	querystring = {"aggregateHours": "24", "location": place, "contentType": "json", "unitGroup": "us",
				   "shortColumnNames": "0"}

	headers = {
		"X-RapidAPI-Key": "",
		"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	response = response.json()

	data = response['locations'][place]['currentConditions']

	currentCondition = "Weather Report : \n\n"
	currentCondition = currentCondition + "Location : " + place + "\n"

	currentCondition = currentCondition + "Temperature : " + str(data['temp']) + " F" + "\n"
	currentCondition = currentCondition + "Heat Index : " + str(data['heatindex']) + " F" + "\n"
	currentCondition = currentCondition + "Wind Speed : " + str(data['wspd']) + " mph" + "\n"
	currentCondition = currentCondition + "Visibility : " + str(data['visibility']) + " mi" + "\n"
	currentCondition = currentCondition + "Humidity : " + str(data['humidity']) + " %" + "\n"
	currentCondition = currentCondition + "Precipitation : " + str(data['precip']) + "\n"
	time_only = datetime.datetime.strptime(data['sunrise'], '%Y-%m-%dT%H:%M:%S%z').time()
	currentCondition = currentCondition + "Sunrise : " + str(time_only) + "\n"
	time_only = datetime.datetime.strptime(data['sunrise'], '%Y-%m-%dT%H:%M:%S%z').time()
	currentCondition = currentCondition + "Sunset : " + str(time_only) + "\n"

	return (currentCondition)
