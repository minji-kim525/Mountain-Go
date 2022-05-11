from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
import requests


client = MongoClient('mongodb+srv://inseong0620:jiji9400@cluster0.vz0y2.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

driver = webdriver.Chrome('./chromedriver.exe')

url = "https://map.naver.com/v5/favorite/myPlace/folder/13050764?c=13949059.7471931,4268858.6047797,6,0,0,0,dh"

driver.get(url)
time.sleep(5)

req = driver.page_source
driver.quit()

soup = BeautifulSoup(req, 'html.parser')

maps = soup.select('#container > shrinkable-layout > div > favorite-layout > favorite-list > favorite-place-bookmark-list > div.scroll_area > place-list-item > ul > li')

for map in maps:

    name = map.select_one("div > a > div > span.result_name").text
    address = map.select_one("span.result_address").text
    print(name,address)

    headers = {
        "X-NCP-APIGW-API-KEY-ID": "q65brv2d98",
        "X-NCP-APIGW-API-KEY": "GP8gYoSZFGAhSygjehJSLmu19cSPK2KvmGBlQAWf"
    }
    r = requests.get(f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}", headers=headers)
    response = r.json()
    if response["status"] == "OK":
        if len(response["addresses"]) > 0:
            x = float(response["addresses"][0]["x"])
            y = float(response["addresses"][0]["y"])
            print(name, address, x, y)
            doc = {
                "name": name,
                "address": address,
                "mapx": x,
                "mapy": y
            }
            db.mountains.insert_one(doc)


        else:
            print(name, "좌표를 찾지 못했습니다")