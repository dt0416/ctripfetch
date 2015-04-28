from pyquery import PyQuery
import getCtripAllCity
import sys
from pprint import pprint

'''
how to use
python3 getLineAllCities.py http://you.ctrip.com/sitelist/asia120001.html ./output/cities/asia
python3 getLineAllCities.py http://you.ctrip.com/sitelist/europe120002.html ./output/cities/europe
python3 getLineAllCities.py http://you.ctrip.com/sitelist/northamerica120004.html ./output/cities/northamerica
python3 getLineAllCities.py http://you.ctrip.com/sitelist/southamerica120005.html ./output/cities/southamerica
python3 getLineAllCities.py http://you.ctrip.com/sitelist/oceania120003.html ./output/cities/oceania
python3 getLineAllCities.py http://you.ctrip.com/sitelist/africa120006.html ./output/cities/africa
python3 getLineAllCities.py http://you.ctrip.com/sitelist/nanji120481.html ./output/cities/nanji
todo 南極的place要獨立去抓，因為南極沒有國家
todo 有些國家不在這7個洲裡，需再確認是否要全抓
'''

'''
Main
'''
targetUrl = sys.argv[1]
outputDirectory = sys.argv[2]

qList = PyQuery(targetUrl)
for element in qList('.normalbox')('li > a'):
    countryUrl = PyQuery(element).attr('href').replace('/place', '/countrysightlist')
    targetJson = outputDirectory + "/" + countryUrl.split('/')[2].replace('.html', '') + ".json"
    countryUrl = "http://you.ctrip.com" + countryUrl
    # if (countryUrl == "http://you.ctrip.com/countrysightlist/southkorea100042.html"):
    pprint(countryUrl)
    pprint(targetJson)
    getCtripAllCity.main(countryUrl, targetJson)
