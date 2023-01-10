import requests
#print current python version
print(requests.__version__)
#print google home page information
print(requests.get("http://www.google.com").text)

print(requests.get("https://raw.githubusercontent.com/JiaYiChe/404lab1/main/find_version.py").text)
