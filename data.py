import re
import requests
import json
from flask import Flask , render_template , request
from bs4 import BeautifulSoup

userData = input("Enter the city name")
# print(userData)
event_title = []


def remove_html_tags(textList):
	"""Remove html tags from a string"""
	clean = re.compile('<.*?>')
	textList = list(map(lambda i:re.sub(clean, '', str(i)),textList))
	clean = re.compile('\s+')
	textList = list(map(lambda i:re.sub(clean, ' ', str(i)),textList))
	return textList

def cityEvents():

    eventsUrl = "https://allevents.in/" + userData + "/all?ref=cityhome-popular" 
    # print(eventsUrl)
    eventFile = "Event.json"
    eventData = []
    eventResponse = requests.get(eventsUrl)
    # print(eventResponse)
    eveSoup = BeautifulSoup(eventResponse.text , "lxml")
    try:

        event = eveSoup.find_all("div" , {"class":"events-style-resgrid default-event-list"})
        # print(event)
    except AttributeError:
        pass


    for events in event:
        

        title = remove_html_tags(events.find_all( class_ = "title")[0:5]) 
        # print(title[1])
        date =  remove_html_tags(events.find_all( class_ = "meta-left")[0:5]) 
        venue = remove_html_tags(events.find_all( class_ = "up-venue toh")[0:5]) 
        ticket = remove_html_tags(events.find_all( class_ = "tick-price")[0:5]) 
        event_title.append(title)
        # combine = title + date + venue + ticket

        

            # print(final)

            
    #     eventData.append({
    #         "Title":remove_html_tags(title),
    #         "Date": remove_html_tags(date),
    #         "Venue":remove_html_tags(venue),
    #         "Ticket":remove_html_tags(ticket)

    #     })

    # with open(eventFile,"w") as jsonFile:
    #     jsonFile.write(json.dumps( eventData, indent=4))

    
    # print(eventData)
print(event_title)
cityEvents()





                
    
        





        
    
        
        
        
