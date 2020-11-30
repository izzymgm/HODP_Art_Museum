#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:06:57 2020

@author: isabellagm
"""



import requests
import json


def pagination(url):
    r = requests.get(url)

    # Convert data to jSON format
    data = r.json()
    
    
  
    # Extract the info and records
    info = data['info']
    records = data['records']
    
   

    # For each record of objects, print the title and classification

    for item in records:
                  
        # Get any people info associated with artwork
        peopleArray = item.get('people')

        # Create empty array to append information to
        peopleInfo = []

        # If there are people associated with object,
        if peopleArray:
          # Go through each person (if several),
          for person in peopleArray:
            # And append gender and role to a list
            gender = person.get('gender')
            role = person.get('role')
            peopleInfo.append([gender, ';', role])

        # Convert created list to string for printing
        peopleInfoString = ';'.join(map(str, peopleInfo))
              
        print(str(item['objectid']) + ';' + item['dated'] + ';' + peopleInfoString )
       
        
    try:
        # If there is a next page, repeat pagination function
        if (info['next']):
            pagination(info['next'])
    # If next page doesn't work, end function
    except:
        pass


# Query to find all objects that have cat in the title
url = "https://api.harvardartmuseums.org/object?q=accessionyear:[2008%20TO%202020]%20AND%20accessionmethod:Purchase&apikey=7c2d8233-3970-4f32-b1d3-f405159bd403&size=100"

# Perform Pagination function defined above on the query
pagination(url)

#+ item['classification'] + ';' + item['dated']
#str(item['objectid']) + ';' + 

#';' + str(item['accessionyear'])  +  ';'  + (item['classification']) + ';'

