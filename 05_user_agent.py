import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()  # 문제 발생시 에러 코드
print("응답코드:", res.status_code) # 200이면 정상
with open("nadocoding.html","w",encoding="utf8") as f:
    f.write(res.text)
