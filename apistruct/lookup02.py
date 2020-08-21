#!/usr/bin/env python3
import requests
from pprint import pprint

def main():
  mytoken = 'f5169deef8f38d27e2708dd164d5128e018fd76b066e8c5f'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken
  print(mybuiltapi)

  ## ask user for a brand to search on
  brand = input("What brand of device are you searching for?")
  brand = "&brand=" + brand
  
  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi + brand).json()
  print(myjson)
  ## Display a list of what inside our JSON
  for x in myjson:
    pprint(x)
  
if __name__ == '__main__':
  main()

