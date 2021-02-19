# create a weather report for the current day (& hour) for a city (Bucharest, Timisoara, Oradea, Suceava, Brasov)
# you can use the API from https://www.weatherbit.io/
# url for current day: https://api.weatherbit.io/v2.0/current
# params: city and key; for key you can use mine 1ab5e9499298416b97674b2facdaeb1c or make a free account on the site
# save the weather report in a file & make a class which can reconstruct the object from the file
# every weather report is appended to its city, we never delete a previous day
# weather report should contain a description of the weather, temperature, clouds metric & sunset time
import requests
import json
#

def print_weather(city):
    url = 'https://api.weatherbit.io/v2.0/current'
    params = {'city': city, 'key': '1ab5e9499298416b97674b2facdaeb1c'}
    output = requests.get(url, params)
    print(output)
    body = json.loads(output.content)
    # print(body)
    data = body['data'][0]
    print('Clouds: ' + str(data['clouds']))
    print('Description: ' + data['weather']['description'])
    print('Temperature: ' + str(data['temp']) + 'C')

print_weather('Roma,IT')
print_weather('Bucharest,RO')
print_weather('Paris,FR')
