# First thing we'll do is import the requests library
import requests

# Define a variable with the URL of the API
api_url = "http://shibe.online/api/shibes?count=1"

# Call the root of the api with GET, store the answer in a response variable
# This call will return a list of URLs that represent dog pictures
response = requests.get(api_url)

# Get the status code for the response. Should be 200 OK
# Which means everything worked as expected
print(f"Response status code is: {response.status_code}")

# Get the result as JSON
response_json = response.json()

# Print it. We should see a list with one image URL.
print(response_json)

# Passing in a non-existant URL will result in a 404 (not found)
bad_response = requests.get("http://shibe.online/api/german-shepards")
print(f"Bad Response Status Code is: {bad_response.status_code}")  # Status code is 404, meaning that resource doesn’t exist.

