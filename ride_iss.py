#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json
from pprint import pprint

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachement (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    # show that at this point, our data is str
    # we want to convert this to list / dict
    pprint(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))
    helmetson['number'] = 4
    helmetson['people'][3]['craft'] = 'ISS'
    helmetson['people'][3]['name'] = 'Eddie Kopra'
   # helmetson['people'][4]['craft'] = 'ISS'
   # helmetson['people'][4]['name'] = 'James Peake'
   # helmetson['people'][5]['craft'] = 'ISS'
   # helmetson['people'][5]['name'] = 'Yuri Kopra'
   # helmetson['people'][6]['craft'] = 'ISS'
   # helmetson['people'][6]['name'] = 'Buzz Aldrin'

    # this should say str
    print(type(helmet))

    pprint(helmetson)

    # this should say dict
    print(type(helmetson))

    print(helmetson["number"])

    # this returns a LIST of the people on this ISS
    print(helmetson["people"])

    # list the FIRST astro in the list
    print(helmetson["people"][0])

    # list the SECOND astro in the list
    print(helmetson["people"][1])

    # list the LAST astro in the list
    print(helmetson["people"][-1])

    # display every item in a list
    for astro in helmetson["people"]:
        # display what astro is
        print(astro)

    # display every item in a list
    for astro in helmetson["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"])

if __name__ == "__main__":
    main()

