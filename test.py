import requests


r = requests.get('http://127.0.0.1:5000/races/2010')


jsons = r.json()

gp = jsons['Race 2010'][0]

print(gp)