# coding:utf8
import json
from pyquery import PyQuery
import sys
import io
from pprint import pprint

'''
how to use
python3 getCtripAllCity.py http://you.ctrip.com/countrysightlist/japan100041.html ./output/cities/asia/japan.json
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

'''
Main
'''
result = {}
def main(targetUrl, outputFile):
    # targetUrl = args[0]
    # outputFile = args[1]
    # pprint(targetUrl)
    # pprint(outputFile)

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

    writefile(result, outputFile)
    # pprint(result)

if __name__ == '__main__':
    # result = {}
    main(sys.argv[1], sys.argv[2])
