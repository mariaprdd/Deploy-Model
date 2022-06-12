import os
import requests


resp = requests.post("https://getpredictionskin-oyfrikhusa-et.a.run.app/",files=open(str(os.getcwd) + '\test modell\herpes zoster.jpg','rb'))

print(os.getcwd())