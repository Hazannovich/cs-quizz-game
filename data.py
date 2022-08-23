import requests
param = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=param)
response.raise_for_status()
question_data = response.json()['results']
