import requests
city_name="Mumbai"
API_key="e93681196e533d13da14079287613186"



url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response=requests.get(url)
if response.status_code == 200:
    data=response.json()
    print('weather is',data['weather'][0]['description'])
    print('current temperature is ',data['main']['temp'])
    print('current temperature feels like is ',data['main']['feels_like'])
    print('current humidity is ',data['main']['humidity'])