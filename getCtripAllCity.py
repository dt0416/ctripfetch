# coding:utf8
import json
from pyquery import PyQuery
import sys
import io
from pprint import pprint

'''
how to use
python3 getCtripAllCity.py http://you.ctrip.com/countrysightlist/japan100041.html ./output/cities/asia/japan.json
python3 getCtripAllCity.py http://you.ctrip.com/countrysightlist/china110000.html ./output/cities/china/china.json
'''

'''
Function
'''
def writefile(outputObject, filePath):
    pprint(filePath)
    with io.open(filePath, 'w', encoding='utf-8') as outfile:
        json.dump(outputObject, outfile, ensure_ascii=False)

def getCities(index, value):
    qList = PyQuery(value)
    city = {}
    city["cName"] = qList("dl > dt > a").text()
    city["url"] = qList(".gs2_more_arror").parent('a').attr('href')
    result["cities"].append(city)
    # if (result["cName"] == "中国"):
        # writefile(result, sys.argv[2].replace("asia", "china").replace(".json", "") + city["cName"] + ".json")
        # result["cities"] = []

'''
Main
'''
result = {}
def main(targetUrl, outputFileP):
    outputFile = outputFileP
    # targetUrl = args[0]
    # outputFileP = args[1]
    # pprint(targetUrl)
    # pprint(outputFileP)

    qFirstPage = PyQuery(targetUrl)
    numpage = qFirstPage('.numpage').text()
    result["eName"] = qFirstPage(".dest_toptitle div > div > p").text() # 國家英文
    result["cName"] = qFirstPage(".dest_toptitle div > div > h1 > a").text() # 國家中文
    result["cities"] = []
    if numpage == "":
        numpage = "2"
    for pageIndex in range(1, int(numpage)+1):
    # for pageIndex in range(1, 2):
        cityListUrl = targetUrl.replace('.html', '/') + 'p' + str(pageIndex) + '.html'
        pprint(cityListUrl)
        qPage = PyQuery(cityListUrl)
        # pprint(cityListUrl)
        qPage(".list_mod1").each(getCities)
        if (result["cName"] == "中国"): # china以分頁為單位輸出一個檔案，方便place分批處理
            writefile(result, outputFileP.replace(".json", "_") + str(pageIndex) + ".json")
            result["cities"] = []

    writefile(result, outputFileP)
    # pprint(result)

if __name__ == '__main__':
    # result = {}
    main(sys.argv[1], sys.argv[2])

