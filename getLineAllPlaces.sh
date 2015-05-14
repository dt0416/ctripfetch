#!/bin/bash

# ===========================
# how to use
# sh getLineAllPlaces.sh ./output/cities/africa ./output/places/africa
# sh getLineAllPlaces.sh ./output/cities/asia ./output/places/asia
# sh getLineAllPlaces.sh ./output/cities/asia_n ./output/places/asia_n
# sh getLineAllPlaces.sh ./output/cities/china ./output/places/china
# sh getLineAllPlaces.sh ./output/cities/china_big ./output/places/china_big

# sh getLineAllPlaces.sh ./output/cities/china_0 ./output/places/china_0
# sh getLineAllPlaces.sh ./output/cities/china_1 ./output/places/china_1
# sh getLineAllPlaces.sh ./output/cities/china_2 ./output/places/china_2
# sh getLineAllPlaces.sh ./output/cities/china_3 ./output/places/china_3
# sh getLineAllPlaces.sh ./output/cities/china_4 ./output/places/china_4
# sh getLineAllPlaces.sh ./output/cities/china_5 ./output/places/china_5
# sh getLineAllPlaces.sh ./output/cities/china_6 ./output/places/china_6
# sh getLineAllPlaces.sh ./output/cities/china_7 ./output/places/china_7
# sh getLineAllPlaces.sh ./output/cities/china_8 ./output/places/china_8
# sh getLineAllPlaces.sh ./output/cities/china_9 ./output/places/china_9
# sh getLineAllPlaces.sh ./output/cities/china_10 ./output/places/china_10
# sh getLineAllPlaces.sh ./output/cities/china_11 ./output/places/china_11
# sh getLineAllPlaces.sh ./output/cities/china_12 ./output/places/china_12
# sh getLineAllPlaces.sh ./output/cities/china_13 ./output/places/china_13
# sh getLineAllPlaces.sh ./output/cities/china_14 ./output/places/china_14
# sh getLineAllPlaces.sh ./output/cities/china_15 ./output/places/china_15
# sh getLineAllPlaces.sh ./output/cities/china_16 ./output/places/china_16
# sh getLineAllPlaces.sh ./output/cities/china_17 ./output/places/china_17
# sh getLineAllPlaces.sh ./output/cities/china_18 ./output/places/china_18
# sh getLineAllPlaces.sh ./output/cities/china_19 ./output/places/china_19

# sh getLineAllPlaces.sh ./output/cities/europe ./output/places/europe
# sh getLineAllPlaces.sh ./output/cities/nanji ./output/places/nanji
# sh getLineAllPlaces.sh ./output/cities/northamerica ./output/places/northamerica
# sh getLineAllPlaces.sh ./output/cities/oceania ./output/places/oceania
# sh getLineAllPlaces.sh ./output/cities/southamerica ./output/places/southamerica
# ===========================

mkdir -p "$2" # 成功輸出資料夾
mkdir -p "${2/places/fails}" # 錯誤輸出資料夾
for cityJson in $(find "$1" -name "*.json")
do
    FNAME=`basename $cityJson`
    echo $cityJson
    echo "$2/$FNAME"
    python3 getCtripPlaceList.py $cityJson "$2/$FNAME"
done