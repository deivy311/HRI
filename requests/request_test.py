import requests
import json

# url = "https://hri-app-sapienza.herokuapp.com/get_patient_info"
url = "http://127.0.0.1:5000/get_more_info"
data = {'patient_id': 1}
data = json.dumps(data)

x = requests.post(url, data = data)

print(x.text)