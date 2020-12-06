import requests
starships = requests.get("https://swapi.dev/api/starships").json()
for ship in starships['results']:
    print('Name of ship:',ship['name'])
    for pilot in ship['pilots']:
        print('\n')
        e = requests.get(pilot).json()['name']
        print('Pilots:', e)
    if len(ships['pilots'])
print('This is a test.')hullo my name is nik