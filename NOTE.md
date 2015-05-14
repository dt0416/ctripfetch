STEP
=====
1. getLineAllCities.py
  mkdir -p ./output/cities/asia
  ex: python3 getLineAllCities.py http://you.ctrip.com/sitelist/asia120001.html ./output/cities/asia
2. getLineAllPlaces.sh
  ex:sh getLineAllPlaces.sh ./output/cities/africa ./output/places/africa
3. convertZ簡轉繁
4. importData.sh
  ex: sh importData.sh ./output/convert/africa

CITY
=====
## get city from country
http://you.ctrip.com/countrysightlist/china110000.html
* command
iojs getCtripAllCity.js http://you.ctrip.com/countrysightlist/japan100041.html > ./citys/japan.json
python3 getCtripAllCity.py http://you.ctrip.com/countrysightlist/japan100041.html > ./citys/japan.json

PLACE
======
## get place list from city
http://you.ctrip.com/sightlist/tokyo294.html
* 分頁
http://you.ctrip.com/sightlist/tokyo294/s0-p1.html
* command
iojs getCtripPlaceList ./citys/EU/austria_one.json ./eu/austria.json
python3 getCtripPlaceList.py ./citys/EU/austria_one.json ./eu/austria_p.json

* get place detail
http://you.ctrip.com/sight/vienna439/13349.html
* get place detail-traffic
http://you.ctrip.com/sight/vienna439/13349-traffic.html

* imgurl
http://you.ctrip.com/Destinationsite/TTDSecond/Photo/AjaxPhotoDetailList?districtId=439&type=2&pindex=2&phsid=19305339&resource=13349
http://you.ctrip.com/Destinationsite/TTDSecond/Photo/AjaxPhotoDetailList?districtId=439&type=2&pindex=2&resource=13349
http://you.ctrip.com/Destinationsite/TTDSecond/Photo/AjaxPhotoDetailList?districtId={439}&type=2&pindex={2}&resource={13349}
http://you.ctrip.com/Destinationsite/TTDSecond/Photo/AjaxPhotoDetailList?districtId={districtId}&type=2&pindex={pindex}&resource={resource}

排名
======
TODO 再查要從哪裡取得所有城市的Place排名

call import REST API
======
curl -X POST http://127.0.0.1:8080/ep/rest/v1/import/importPlace -H "Content-Type: application/json" -d ./output/convert/africa/egypt100030.json
curl -X POST http://127.0.0.1:8080/ep/rest/v1/import/importPlace -H "Content-Type: application/json" -d ./output/convert/simple.json

Amazon Ec2
======
ssh -i jp-test.pem ubuntu@52.68.199.52

command
======
ps aux | grep getLineAllPlaces.sh
ps aux | grep python3
tail -f logs/log.txt
find ./ -name "*.json"