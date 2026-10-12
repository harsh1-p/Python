import requests

a = requests.get("https://api.github.com/")

print(a.text) # Return in string  format

print(a.json()) #Returns in Dict format
