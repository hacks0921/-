import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=335885"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

### 만화제목 / 링크 가지고 오기
# cartoons = soup.find_all("td", attrs={"class":"title"})
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com"+ cartoon.a["href"]
#     print(title, link)

### 평점구하기
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
total_rates = 0
print(cartoons)
for cartoon in cartoons:
    # index = cartoon.find("strong")
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates +=float(rate)

print("전체점수: ", total_rates)
print("평균점수: ", total_rates/len(cartoons))

# </div>, <div class="rating_type">
# <span class="star"><em style="width:99.60%">평점</em></span>
# <strong>9.96</strong>


# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title, "https://comic.naver.com" + link)

# '''<td class="title">
# <a href="/webtoon/detail.nhn?titleId=335885&amp;no=252&amp;weekday=mon" onclick="nclk_v2(event,'lst.title','335885','252')">250화 상식씨!</a>
# </td>
# '''


# print(cartoons)
# print("-"*100)
# print(cartoons[0])
# print("-"*100)
# print(cartoons[0].a)
# print("-"*100)
# title = cartoons[0].a.get_text()
# print(title)