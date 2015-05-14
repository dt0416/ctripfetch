#!/bin/bash

# ===========================
# how to use
# sh importData.sh ./output/convert/africa
# sh importData.sh ./output/convert/asia
# sh importData.sh ./output/convert/china
# sh importData.sh ./output/convert/europe
# sh importData.sh ./output/convert/nanji
# sh importData.sh ./output/convert/northamerica
# sh importData.sh ./output/convert/oceania
# sh importData.sh ./output/convert/southamerica
# ===========================

for countryJson in $(find "$1" -name "*.json")
do
    echo $countryJson
    curl -X POST http://127.0.0.1:8080/ep/rest/v1/import/importPlace -H "Content-Type: application/json" -d @$countryJson
    echo "\n"
    echo `date "+%Y-%m-%d %H:%M:%S\n"`
done