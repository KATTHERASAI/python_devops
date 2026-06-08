import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

outputs = response.json()

for i in range(len(outputs)):
    print(outputs[i]["user"]["login"])
 
