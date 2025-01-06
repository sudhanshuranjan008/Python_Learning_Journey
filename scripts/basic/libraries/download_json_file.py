# ------------------------------------------------------
# File: download_json_file.py
# Date: 2025-01-05
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Fetch data from a public API and download the JSON response using requests

import requests
import json

# Specify the URL of the JSON file
url = "https://jsonplaceholder.typicode.com/todos/1"

# Send a GET request to fetch the JSON data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Save the JSON data to a file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)  # Write the JSON with indentation
    print("JSON file downloaded successfully!")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
