import requests

url = "https://www.dsm-dms.com/"
response = requests.get(url)
print(type(response))
print(dir(response))
print(response.status_code)
print(response.text)
