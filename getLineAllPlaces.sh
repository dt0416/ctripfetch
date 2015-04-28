# ===========================
# how to use
# sh getLineAllPlaces.sh ./output/cities/africa ./output/places/africa
# sh getLineAllPlaces.sh ./output/cities/asia ./output/places/asia
# sh getLineAllPlaces.sh ./output/cities/europe ./output/places/europe
# sh getLineAllPlaces.sh ./output/cities/nanji ./output/places/nanji
# sh getLineAllPlaces.sh ./output/cities/northamerica ./output/places/northamerica
# sh getLineAllPlaces.sh ./output/cities/oceania ./output/places/oceania
# sh getLineAllPlaces.sh ./output/cities/southamerica ./output/places/southamerica
# ===========================

mkdir -p "$2"
for cityJson in $(find "$1" -name "*.json")
do
    FNAME=`basename $cityJson`
    echo $cityJson
    echo "$2/$FNAME"
    python3 getCtripPlaceList.py $cityJson "$2/$FNAME"
done