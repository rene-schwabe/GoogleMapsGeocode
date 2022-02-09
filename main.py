import json
import pandas as pd
import requests

# Enter API Key
api_key = ''


# Read CSV Input
csv_input = pd.read_csv('Input_test.csv', sep=';', dtype = str)


def getlatitude(adress):
	r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+adress+"&key="+api_key)
	json_data = json.loads(r.text)
	latitude = json_data['results'][0]['geometry']['location']['lat']
	print(latitude)
	return latitude

def getlongitude(adress):
	r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+adress+"&key="+api_key)
	json_data = json.loads(r.text)
	longitude = json_data['results'][0]['geometry']['location']['lng']
	return longitude
	
# Add row lat and long with value from function
csv_input['lat'] = csv_input['Adresse'].apply(getlatitude)
csv_input['long'] = csv_input['Adresse'].apply(getlongitude)
# Export CSV to file
csv_input.to_csv('output.csv', index=False)	
