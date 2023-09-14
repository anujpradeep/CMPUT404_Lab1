import requests

print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/anujpradeep/CMPUT404_Lab1/master/Lab1/lab1.py")


print("Status Code is {}".format(resp.status_code))

print(resp.text)