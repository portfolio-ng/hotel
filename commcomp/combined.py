#!/usr/bin/python3
#uses the classes from frontdesk.py and booking.py to check if booking.com has been over charging fitz for commissions
##must change infile on both frontdesk.py and booking.py


from frontdesk import Frontdesk
from booking import Booking
from expedia import Expedia

import sys
import difflib


front = Frontdesk().process(str(sys.argv[1]))
bookd = Booking().process(str(sys.argv[1]))
exped = Expedia().process(str(sys.argv[1]))

#print(front)
#print(bookd)

bookdon=bookd.split("\n")
expedon=exped.split("\n")
fronton=front.split("\n")


def isnumb(numb):
  try:
    float(numb)
    return True
  except:
    return False


match=0
matcharr=[]
errarr=[]


#check each booking entry against only the frontdesk entries that share the same date
for ei,each in enumerate([bookdon,expedon]):
  if ei==0:
    company="booking.com"
  else:
    company="expedia.com"
  for ibo, itembo in enumerate(each):
    splib=each[ibo].split("+")
    if len(splib) == 4:  #if booking entry is date,bk#,name,money
      match=0
      for ifr, itemfr in enumerate(fronton):
        splif=fronton[ifr].split("+")
        if len(splif) == 4: #if frontdesk entry is date,bk#,name,money
          #print(splib[0],splif[0])
          if splib[0] == splif[0]: # if the dates match
            if len(splib[2].split(";")) > 1: #if the booking entry has many names listed
                splitwo=splib[2].split(";") #array of as many names listed
                for isc, itemsc in enumerate(splitwo): #check all of those names for matches
                  rati=difflib.SequenceMatcher(None,splitwo[isc],splif[2]).ratio() #closeness ratio
                  if rati > .7: # .7 seems like a good match, same name but with a space in the beginning is .8965 match
                    match=1 # made a match
                    #print(splitwo[isc],splif[2],rati)
                    #print(splif,rati)
                    if isnumb(splib[3]) and isnumb(splif[3]): # are these even numbers?, else drop in error array
                      if float(splib[3]) > float(splif[3]): # is booking charging too much commission
                        print("\n",splib,"\n",splif,rati)
                        print(company+":",splib[3]," > ",splif[3],":frontdesk")
                    else:
                      errarr.append(splib)
                      errarr.append(splif)

            else: # if the booking entry only has one name listed
              rati=difflib.SequenceMatcher(None,splib[2],splif[2]).ratio() #closeness ratio
              if rati > .7: # .7 seems like a good match, same name but with a space in the beginning is .8965 match
                match=1 # made a match
                #print(splif[2],rati)
                #print(splif,rati)
                if isnumb(splib[3]) and isnumb(splif[3]): # are these even numbers?, else drop in error array
                  if float(splib[3]) > float(splif[3]): # is booking charging too much commission
                      print("\n",splib,"\n",splif,rati)
                      print(company+":",splib[3]," > ",splif[3],":frontdesk")
                else:
                  errarr.append(splib)
                  errarr.append(splif)
      if match == 0: #if unmatched, drop into match array for human groking
        splib.append(rati)
        matcharr.append(splib)


print("\n\n\n :: investigate :: \n")
print("\n :: match fail :: \n")
for ima, itemma in enumerate(matcharr):
  print(matcharr[ima],"\n")
print("\n :: charge fail :: \n")
for iea, itemea in enumerate(errarr):
  print(errarr[iea],"\n")

