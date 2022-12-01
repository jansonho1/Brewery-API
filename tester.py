import pip._vendor.requests as requests

BASE = "http://127.0.0.1:5000/"
response = requests.put(BASE + "janson", {'id': 1, 'state': 'PA', 'hobbies': 'music'})
print(response)
