# ------------------------------------------------------
# File: requests_intro.py
# Date: 2025-01-05
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Fetch data from a public API and display the JSON response using requests

import requests
import json

# The API endpoint
url = "https://jsonplaceholder.typicode.com/todos/1"

# Send a GET request to the API endpoint
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    # Convert and prettify the JSON response
    data = response.json()
    print("JSON Response:")
    print(json.dumps(data, indent=4))
else:
    print("Failed to fetch data. HTTP Status Code:", response.status_code)


