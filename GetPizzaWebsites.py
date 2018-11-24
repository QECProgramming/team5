
import requests as r
import json
def getWebsiteAddress(placeId):
    url ='https://maps.googleapis.com/maps/api/place/details/json?placeid='
    url = url+ placeId +'&fields=website&key=AIzaSyCj_G9qmavdz7xUQsi3C0N7R2_JZMR6K8E'
    response = r.get(url)
    data = response.json()
    result = data["result"]
    if(len(data["result"])>0):
            return result.get("website");
    

def getPlaceIds(long, lat, radius):  
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    key = 'AIzaSyCj_G9qmavdz7xUQsi3C0N7R2_JZMR6K8E'
    url = url + 'location=' +str(lat)+','+ str(long) + '&' + 'radius=' + str(radius) + '&' + 'type=restaurant&keyword=pizza&key='+key
    response = r.get(url)
    data = response.json()
    websites =[]
    for place in data["results"]:
        websites.append(getWebsiteAddress(place.get("place_id")))
    return websites
         

def getPlacesList(address, radius):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    addressArray =address.split(' ')
    for addressComp in addressArray:
        url = url + addressComp + '+'
    url = url[:-1]
    url = url +'&key=AIzaSyCj_G9qmavdz7xUQsi3C0N7R2_JZMR6K8E'
    response = r.get(url)
    data = response.json()
    data = data.get("results")[0]
    geometry = data["geometry"]
    lat = geometry.get("location").get("lat")
    long = geometry.get("location").get("lng")
    websites = getPlaceIds(long, lat, radius)
    print(websites)
    

  
   


        
getPlacesList('245 Albert SSt Kingston',5000)