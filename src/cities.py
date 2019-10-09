import os
import json
# print(os.getcwd()
# cities_data = open('requirements.txt')
# cities_data = open('./src/cities.json') # this is read-only

my_list = {
    "my_list": [1, 2, 3, 4, 5]
}
print(json.dumps(my_list))


with open('./src/cities.json') as cities_data:
    print(type(cities_data))
    contents = cities_data.read()
    print(contents)
