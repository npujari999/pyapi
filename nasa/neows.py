#!/usr/bin/python3
import requests
from pprint import pprint

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    startdate = input("Enter Start Date - XXXX-XX-XXX : ")
    
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)
    
    # strip off json attachment from our response
    neodata = neowrequest.json()
        
    ## display NASAs NEOW data
    pprint(neodata)
    
if __name__ == "__main__":
    main()

