import requests

resp = requests.post("https://localhost:5000", files={'file': open('herpes zoster.jpg', 'rb')})

print(resp.json())