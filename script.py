import requests

print(requests.__version__)

r = requests.get('http://www.google.com')
print(r)

scr = requests.get('https://raw.githubusercontent.com/kalegar/cmput404-lab-1/master/script.py')
print(scr.text)
