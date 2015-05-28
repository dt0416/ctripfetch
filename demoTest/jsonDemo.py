import urllib
# from urllib.request import urlopen
import json
from pprint import pprint

response = urllib.urlopen('http://you.ctrip.com/Destinationsite/TTDSecond/Photo/AjaxPhotoDetailList?districtId=439&type=2&pindex=2&resource=13349')
# response = urlopen('http://you.ctrip.com/Destinationsite/TTDSecond/Photo/AjaxPhotoDetailList?districtId=439&type=2&pindex=2&resource=13349')
data = json.load(response)   
pprint(data)