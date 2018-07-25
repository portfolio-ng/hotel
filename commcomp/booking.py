#!/usr/bin/env python3
#takes in a csv and returns a simplified table of only the interesting bits: date, booking#, name, charge
##must change name of infile


class Booking():
  def process(self,thismo):
    infile = open(thismo+'.booking.csv') #split('+')

    lines = infile.readlines()
    infile.close()
    numb=len(lines)

    def thedate( arrn ):
      dated=arrn[4] #split('+')
      if ( len(dated.split('/')) == 3 ):
        dated=dated.split('/')
        if ( int(dated[0]) < 10 ):
          if ( int(dated[1]) < 10 ):
            nd=dated[2]+"-0"+dated[0]+"-0"+dated[1]
          else:
            nd=dated[2]+"-0"+dated[0]+"-"+dated[1]
        else:
          if ( int(newdate[1]) < 10 ):
            nd=dated[2]+"-"+dated[0]+"-0"+dated[1]
          else:
            nd=dated[2]+"-"+dated[0]+"-"+dated[1]

      if nd.split("-")[0] == "15":  ## only accounts for 2015 dates
        sp=nd.split("-")
        nd="20"+sp[0]+"-"+sp[1][-2:]+"-"+sp[2][-2:]

      if ( len(nd.split("-")) == 3 ):
          nd = nd.split(" ")[0]
          return nd
      else:
        print(dated)
        print(arrn)

    def thebook( arrn ):
      booked=arrn[0]
      return booked

    def thename( arrn ):
      named=arrn[3] #split('+')
      if ( named == "; " ):
        lastfirst=arrn[2].split(',')
        firstlast=lastfirst[1]+" "+lastfirst[0]
        named=firstlast
      named=named.lower()
      return named

    def themony( arrn ):
      moneyd=arrn[7] #split('+')
      moneyd=moneyd[4:]
      return moneyd

    tosrt=[""]
    for i, item in enumerate(lines):
      spli=lines[i].split('+')
      if ( spli[6] == "ok" ):
        td=thedate(spli)
        tb=thebook(spli)
        tn=thename(spli)
        tm=themony(spli)
        if ( td ):
          trb=td+"+"+tb+"+"+str(tn)+"+"+str(tm)
          tosrt.append(trb)
    sortd="\n".join(sorted(tosrt))
    return sortd

#shagb = Booking().process()
#print(shagb)

