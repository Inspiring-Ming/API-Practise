import requests
from flask import Flask, jsonify
import json

api = Flask(__name__)

def fetch_external_data():
    url = 'https://greenhouseaccounts.climatechange.gov.au/OData'
    response = requests.get(url)
    data = response.json()
    return data

@api.route('/api/data', methods=['GET'])
def get_data():
    data = fetch_external_data()
    return jsonify(data)

if __name__ == '__main__':
    api.run(debug=True)





#def save_data_as_json(data):
    #with open('data.json', 'w') as json_file:
        #json.dump(data, json_file)

#data = fetch_external_data()
#save_data_as_json(data)
