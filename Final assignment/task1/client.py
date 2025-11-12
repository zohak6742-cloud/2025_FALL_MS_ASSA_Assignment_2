import requests

server_url = "http://127.0.0.1:5000/message"


data = {"message": "I am client"}
response = requests.post(server_url, json=data)
if response.status_code == 200:
    print("Client says: I am client")
    print("Server says:", response.json()["reply"])


data = {"message": "Nice to meet you!"}
response = requests.post(server_url, json=data)
if response.status_code == 200:
    print("Client says: Nice to meet you!")
    print("Server says:", response.json()["reply"])
