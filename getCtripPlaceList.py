# coding:utf8
import json
from pyquery import PyQuery
import sys
import io
import logging
from urllib.error import HTTPError

'''
todo
* 取得城市中文，var city/INTERFACE.poo_city_name
'''

'''
how to use
python3 getCtripPlaceList.py ./output/cities/eu/austria_one.json ./output/places/eu/austria_p.json
python3 getCtripPlaceList.py ./output/cities/asia/japan_p.json ./output/places/asia/japan_p.json
python3 getCtripPlaceList.py ./output/cities/asia/azerbaijan20375.json ./output/places/asia/azerbaijan20375.json
python3 getCtripPlaceList.py ./output/cities/china/china丁青.json ./output/places/china/china丁青.json
python3 getCtripPlaceList.py ./output/cities/china_0/china_1.json ./output/places/china_0/china_1.json
python3 getCtripPlaceList.py ./output/cities/china/china_1.json ./output/places/china/china_1.json
python3 getCtripPlaceList.py ./output/cities/africa/zimbabwe100150.json ./output/places/africa/zimbabwe100150.json
python3 getCtripPlaceList.py ./output/cities/oceania/newzealand100078.json ./output/places/oceania/newzealand100078.json
python3 getCtripPlaceList.py ./output/cities/europe_f/italy100026.json ./output/places/europe/italy100026_f.json
'''

'''
Function
'''
def writeFile(outputObject):
    with io.open(outputFile, 'w', encoding='utf-8') as outfile:
        json.dump(outputObject, outfile, ensure_ascii=False)

def writeFailFile(outputObject):
    with io.open(outputFailFile, 'w', encoding='utf-8') as outfile:
        json.dump(outputObject, outfile, ensure_ascii=False)

def parseTraffic(url, place):
    logger.info(url)
    qTraffic = PyQuery(url)
    place["traffic"] = qTraffic(".detailcon > div > p").html()

def parseDetail(url, place):
    logger.info(url)
    qDetail = PyQuery(url)
    place["pNmEng"] = qDetail(".dest_toptitle > div > div > p").remove('span').text().strip()
    try:
        place["pDesc"] = qDetail(".toggle_l:first > .text_style").html().strip()
    except Exception as ex:
        logger.error(ex)
    # mapSrc = qDetail(".s_sight_map > a > img").attr('src').split('%7C')[1].split('&')[0]
    # place["lng"] = mapSrc.split(',')[1]
    # place["lat"] = mapSrc.split(',')[0]
    place["lng"] = qDetail("#Lon").val()
    place["lat"] = qDetail("#Lat").val()
    ctypeAList = qDetail(".s_sight_con:first > a")
    place["viewTypes"] = []
    for element in ctypeAList[:3]:
        viewType = {}
        viewHref = PyQuery(element).attr("href")
        viewType["codeId"] = viewHref.split("/")[-1].split(".")[0].replace("s", "")
        viewType["codeName"] = PyQuery(element).text()
        place["viewTypes"].append(viewType)
    try:
        place["contactTel"] = PyQuery(qDetail(".s_sight_con")[2]).text().strip()
        place["website"] = PyQuery(qDetail(".s_sight_con")[3])("a").text()
    except Exception as ex:
        logger.error(ex)
    place["openHours"] = ""
    for element in qDetail("dt:contains('开放时间')").nextAll("dd"):
        place["openHours"] += PyQuery(element).outerHtml()
    place["expense"] = ""
    for element in qDetail("dt:contains('门票信息')").nextAll("dd"):
        place["expense"] += PyQuery(element).outerHtml()
    place["districtid"] = qDetail("#ctmdistrict").val() # 取得圖片用ID, #JS_DistrictId的值一樣
    place["resourceid"] = qDetail("#wentClickID").attr("dataresource-cat") # 取得圖片用ID
    place["totalImgCount"] = qDetail(".r_text").text().replace("全部", "").replace("张照片", "") # 取得圖片用，數量
    place["countryEngName"] = inputCountryJson["eName"]
    # place["countryChnName"] = PyQuery(qDetail("i.arrow")[1]).parent('a').text() # 國家中文
    place["countryChnName"] = inputCountryJson["cName"] # 國家中文
    place["cityEngName"] = qDetail("#EName").val() # city英文

def getItem(index, value):
    # try:
        qList = PyQuery(value)
        place = {}
        place["pNm"] = qList(".rdetailbox > dl > dt > a").text()
        place["url"] = qList(".rdetailbox > dl > dt > a").attr('href')
        # place["sImg"] = qList(".leftimg > a > img").attr('src')
        place["imgId"] = qList(".leftimg > a > img").attr('img-id')
        place["address"] = qList(".rdetailbox > dl > dd.ellipsis").text().strip()
        # todo 排名改抓城市的，這裡的排名非城市排名
        # place["popOrder"] = qList(".rdetailbox > dl > dt > s").text().strip().replace("第", "").replace("名", "")
        # place["s_img"] = 

        detailUrl = 'http://you.ctrip.com' + place["url"]
        parseDetail(detailUrl, place)
        trafficUrl = 'http://you.ctrip.com' + place["url"].replace('.html', '-traffic.html')
        parseTraffic(trafficUrl, place)

        city["places"].append(place)
        # pprint(place)
    # except HTTPError:
        # pass

def getListPage(url):
    logger.info(url)
    qFirstPage = PyQuery(url)
    numpage = qFirstPage('.numpage').text()
    if numpage == "":
        numpage = "2"
    for pageIndex in range(1, int(numpage)+1):
    # for pageIndex in range(1, 2):
        placeListUrl = url.replace('.html', '/') + 's0-p' + str(pageIndex) + '.html'
        logger.info(placeListUrl)
        qPage = PyQuery(placeListUrl)
        if len(qPage(".list_mod2")) > 0:
            qPage(".list_mod2").each(getItem)

'''
Main
'''
logger = logging.getLogger( 'getCtripPlaceList' )
targetFile = sys.argv[1]
outputFile = sys.argv[2]
outputFailFile = sys.argv[2].replace("places", "fails") # 錯誤輸出的檔案
# logger.info(targetFile)
# logger.info(outputFile)

# Produce formater first
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Setup Handler
fileHandler = logging.FileHandler("logs/log.txt")
fileHandler.setFormatter(formatter)

# Setup Logger
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)


# 打開國家檔
with open(targetFile, encoding='utf-8') as data_file:
    inputCountryJson = json.load(data_file)
# logger.info(type(inputCountryJson))
# logger.info(inputCountryJson)

result = []
failCities = [];
for eachCity in inputCountryJson["cities"] :
    city = {}
    city["cName"] = eachCity["cName"]
    city["url"] = "http://you.ctrip.com" + eachCity["url"]
    city["places"] = []
    try:
        getListPage(city["url"])
        result.append(city)
    except Exception as ex:
        failCities.append(eachCity)
        logger.error(ex)

writeFile(result)
if failCities != [] :
    inputCountryJson["cities"] = failCities
    writeFailFile(inputCountryJson)
# logger.info(result)
