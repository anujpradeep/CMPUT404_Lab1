import requests

print(requests.__version__)

resp = requests.get("https://www.google.com")


print("Status Code is {}".format(resp.status_code))

print(resp.text)