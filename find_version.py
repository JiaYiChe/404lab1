import requests
//print current python version
print(requests.__version__)
//print google home page's information
print(requests.get("http://www.google.com").text)