#Project 2 web scraping using BeautifulSoup4 and Requests 

import requests 
from bs4 import BeautifulSoup 

oyo_url="https://www.oyorooms.com/hotels-in-bangalore/"

req=requests.get(oyo_url)
content= req.content

soup= BeautifulSoup(content,"html.parser")

#Accesing the hotel cards
all_hotels= soup.find_all("div", {"class":"hotelCardListing"})
#Accessing individual Hotel names 
for hotel in all_hotels:
    hotel_name=hotel.find("h3",{"class":"listingHotelDescription__hotelName "}).text
    print(hotel_name)

##This is the project that I have trouble with. The code above isnt getting executed. I havent written the code for the complete project
