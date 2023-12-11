# extract some data from json file. 

import json                         # json data is the input thats why we need to import json module
import requests                     # end point hit
from socket import timeout

import logging                      #logs 

def hit_endpoint(url):
    list=[]
    if(url!="null"):
        data=requests.get(url)       # gets data from url into the data, alternative to >> curl -x get (shell scripting)
        jsondump=data.json()             # parse into a json format and store it to dump
        print(jsondump["count"])


        for entry in jsondump["entries"]:
            # print(entry['Link'])
            try:
                checkres=requests.get(entry['Link'],timeout=10)
                if (checkres.status_code==200):
                    list.append[entry['Link']]  
                    # print(f"{entry['Link']} is a valid link")
                else:
                    print(f"{entry['Link']} - status code is not 200")
            except requests.exceptions.Timeout:
                logging.error(f"{entry['Link']} timed out.")
            
            break  # for testing purpose breaking else it runs more than 1400 urls.
    else:
        print("url is null")

                
hit_endpoint("https://api.publicapis.org/entries")