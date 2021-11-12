from flask import Flask
import requests
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

BASE = "http://geomapguessr.me:"

geocodeQuality = "COUNTRY"
mapQuestGetRequest = requests.get("http://www.mapquestapi.com/geocoding/v1/reverse?"
                                  "key=P6SlkwXEUSNGa2y0MdU45AXA3LADkReB&location="
                                  "-55.671610,-3.914930"
                                  "&includeRoadMetadata=true&includeNearestIntersection=true");

while geocodeQuality != "STREET":
    responseOmer = requests.get(BASE + "5000/hello")
    randCoordinate = responseOmer.json()

    latitude = randCoordinate['latitude']
    longitude = randCoordinate['longitude']

    mapQuestGetRequest = requests.get("http://www.mapquestapi.com/geocoding/v1/reverse?"
                                  "key=P6SlkwXEUSNGa2y0MdU45AXA3LADkReB&location="
                                  + latitude + "," + longitude +
                                  "&includeRoadMetadata=true&includeNearestIntersection=true");

    randResult = mapQuestGetRequest.json()
    geocodeQuality = randResult['results'][0]['locations'][0]['geocodeQuality']
    print(geocodeQuality)

print(mapQuestGetRequest.json())
resultGetRequest = requests.get(BASE + "5001/Result")
resultPutRequest = requests.put(BASE + "5001/Result")

if __name__ == '__main__':
    app.run()