import requests


url = "http://0.0.0.0:2224/fast"
count=0
for x in range(205):
    r = requests.get(url)
    count+=1
    print(count, r.status_code)
    



