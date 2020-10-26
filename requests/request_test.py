import requests
import json

# url = "https://hri-app-sapienza.herokuapp.com/get_patient_info"
url = "http://127.0.0.1:5000/get_patient_info"
data = {'patient_id': 1}
data = json.dumps(data)

x = requests.post(url, data = data)

print(x.text)


print("\n===========================\n")


# url = "https://hri-app-sapienza.herokuapp.com/get_test_results"
url = "http://127.0.0.1:5000/get_test_results"
data = {'patient_id': 1}
data = json.dumps(data)

x = requests.post(url, data = data)

print(x.text)
# url = "https://hri-app-sapienza.herokuapp.com/get_patient_info"
url = "http://127.0.0.1:5000/get_more_info"
data = {'patient_id': 1}
data = json.dumps(data)

x = requests.post(url, data = data)

print(x.text)