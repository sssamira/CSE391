import requests
import json

def fetch_and_save_data(url, filename):
  try:
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()

    with open(filename, 'w') as f:
      json.dump(data, f, indent=4) 

    print(f"Data fetched and saved to {filename}")

  except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")

api_url = "https://api.quotable.io/random" 
filename = "quotes.json"
fetch_and_save_data(api_url, filename)