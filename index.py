import requests

# Define the URL of your Google Apps Script web app for retrieving data
google_apps_script_url = 'https://script.google.com/macros/s/AKfycbyyx5jYFLfrTY6TnZGAngcT9CC4BQzEt_41v_N-Zj6stm31m3gKXOeRKi6NV_6EqskU6Q/exec'

# Send a GET request to the Google Apps Script web app
response = requests.get(google_apps_script_url, headers={'Content-Type': 'application/json'})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    retrieved_data = response.json()
    
    # Print the retrieved data (optional)
    print("Retrieved Data:", retrieved_data)
else:
    print("Error:", response.text)
