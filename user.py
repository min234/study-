import requests

res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()

with open("nadocoing.html","w",encoding="utf-8") as f :
    f.write(res.text)