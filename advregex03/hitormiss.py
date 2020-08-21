#!/usr/bin/env python3
import re
mytxt = open('grimm.txt') # open file ojbect

allLines = mytxt.readlines() # read out of buffer into list

#print(allLines[0])

mytxt.close() # close file

#lookingfor = re.compile(r'wol[vf][es]?\w+') # compile
                               ## a search expression
lookingfor = re.compile(r'co[m|n].$')
for oneline in allLines:   # search through the lines
    mymatchobj = lookingfor.search(oneline) # call
                      ## search() and pass oneline 
    if mymatchobj: # if mymatchobj has a value (if a match, then...)
            print(mymatchobj.group(), '***', oneline, end='') # Print
                 ## what was matched on, ***, then the string matched

