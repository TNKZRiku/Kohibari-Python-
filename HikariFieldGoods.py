#https://store.hikarifield.co.jp/goods?game_id=0&category_id=0&page=1

import pandas
import requests
from lxml import html


def get_all_securls(url) -> list:
    response = requests.get(url)
    data = html.fromstring(response.content)
    securls = data.xpath('//div[contains(@class,"photo-inside")]/a[@class="link"]/@href')
    return securls


def get_price(url):
    response = requests.get(url)
    data = html.fromstring(response.text)
    price = data.xpath('//*[@id="app"]/main/div[3]/div[2]/div[2]/div[2]/span[2]/text()')
    return price[0].strip()


def get_style(url):
    response = requests.get(url)
    data = html.fromstring(response.text)
    style = data.xpath('//*[@id="app"]/main/div[3]/div[4]/div/div[1]/table/tbody/tr[2]/td[1]/text()')
    return style[0].strip()

def get_specification(url):
    response = requests.get(url)
    data = html.fromstring(response.text)
    specification = data.xpath('//*[@id="app"]/main/div[3]/div[4]/div/div[1]/table/tbody/tr[2]/td[2]/text()')
    return specification[0].strip()


def get_copyright(url):
    response = requests.get(url)
    data = html.fromstring(response.text)
    copyright = data.xpath('//*[@id="app"]/main/div[3]/div[4]/div/div[1]/table/tbody/tr[1]/td[2]/text()')
    return copyright[0].strip()


def get_name(url):
    response = requests.get(url)
    data = html.fromstring(response.text)
    name = data.xpath('//*[@id="app"]/main/div[3]/div[4]/div/div[1]/table/tbody/tr[1]/td[1]/text()')
    return name[0].strip()

base_url = 'https://store.hikarifield.co.jp/goods?game_id=0&category_id=0&page='

goods_list = []
co = 1
for i in range(1, 4+1):
    url = base_url + str(i)
    sec_urls:list = get_all_securls(url)
    for sec_url in sec_urls:
        goods_dict = {}
        price = get_price(sec_url)
        name = get_name(sec_url)
        style = get_style(sec_url)
        specification = get_specification(sec_url)
        copyright = get_copyright(sec_url)
        goods_dict['name'] = name
        goods_dict['price'] = price
        goods_dict['style'] = style
        goods_dict['specification'] = specification
        goods_dict['copyright'] = copyright
        goods_list.append(goods_dict)
        print("第{}个:".format(co),style)
        co += 1

pd = pandas.DataFrame(goods_list)
pd.to_excel(
    'HikariFieldGoods.xlsx',
    index=False
)







