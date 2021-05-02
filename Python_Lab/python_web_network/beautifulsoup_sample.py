"""
#############################################################################
BeautifulSoup:Webスクレイピングのライブラリ
　→htmlからデータ（指定タグの中身などを取得する）
#############################################################################
"""

from bs4 import BeautifulSoup
import requests

URL = 'https://www.python.org/'

# 対象URLのWebページ（htmlファイル）を取得する
html = requests.get(URL)

# # HTMLのファイルを出力
# print(html.text)


soup = BeautifulSoup(html.text, 'html5lib')

# titleタグの部分を取得
titles = soup.find_all('title')

# #リストで返ってくる
#print(titles)
print(titles[0].text)

"""
<div class="introduction">
    <p>Python is a programming language that lets you work quickly <span class="breaker"></span>and integrate systems more effectively. <a class="readmore" href="/doc/">Learn More</a></p>
</div>タグのclassがintroduction部分を取得
"""
intro = soup.find_all('div', {'class': 'introduction'})
print(intro[0].text)