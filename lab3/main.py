import sys
import requests
n = len(sys.argv)

Request = "http://localhost:5000/" + sys.argv[2] + "?"

for i in range(3, n):
    Request += sys.argv[i]
    if i != n - 1:
        Request += "&"

response = ""
if sys.argv[1] == "get":
    response = requests.get(Request)
if sys.argv[1] == "post":
    response = requests.post(Request)
if sys.argv[1] == "patch":
    response = requests.patch(Request)
if sys.argv[1] == "put":
    response = requests.put(Request)
if sys.argv[1] == "delete":
    response = requests.delete(Request)

print("Status code:", response.status_code)
print("Response:", response.json())
