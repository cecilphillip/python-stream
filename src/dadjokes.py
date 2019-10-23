import requests

api_base = 'https://icanhazdadjoke.com/'

headers = {'accept': 'application/json'}

print('---------HERE ARE 10 JOKES HAHAHAHA------------')
for x in range(10):
    response = requests.get(api_base, headers)

    if response.status_code == 200:
        resp_as_json = response.json()
        print(resp_as_json['joke'])
    else:
        print('Oops... didn\'t work')
