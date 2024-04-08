
import requests
from bs4 import BeautifulSoup
import lxml
import json

# urlc = 'https://cheb.ru'
#
hed = {
    'Accept': '*/*',

    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
#
#
# reg = requests.get(url=urlc, headers=hed)
#
# text_htm = reg.text
# print(text_htm)
# with open('index.html', 'w') as file:
#     file.write(text_htm)

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file, 'lxml')


a_ref = soup.find_all('a', class_='anim mdown')
linc_href = {}
for i in a_ref:

    if str(i.get('href'))[0] =='h':
        linc_href[i.text] = i.get('href')
print(linc_href)

with open('my_href.json', 'w') as file:
    json.dump(linc_href, file, indent=4, ensure_ascii=False)

with open('my_href.json', 'r') as jf:
    load_j = json.load(jf)
    print(load_j)
    count = 0
    for name, link in load_j.items():
        reqe = requests.get(url=link, headers=hed)
        with open(f'shets/{count}_{name}.html', 'w') as file:
            file.write(reqe.text)


