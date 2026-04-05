import requests

url = "http://localhost:8000/predict"
data = {
        #text gây ra báo spam
        "text": "Congratulations! You've won a free ticket to the Bahamas! Click here to claim your prize."
}
response = requests.post(url, json=data)
if response.status_code == 200:
        print(response.json())
else:
        print(f"Error: {response.status_code}, {response.text}")
