#!/usr/bin/env python3
#takes in a csv and returns a simplified table of only the interesting bits: date, booking#, name, charge
##must change name of infile

class Frontdesk:
  def process(self,thismo):
    infile = open(thismo+'.frontdesk.csv')

    lines = infile.readlines()

    infile.close()
    def thedate( arrn ):
      dated=arrn[3]
      return dated

    def thebook( arrn ):
      booked=arrn[1]
      return booked

    def thename( arrn ):
      named=arrn[2].lower()
      return named

    def themony( arrn ):
      moneyd=arrn[12]
      return moneyd

    shim=""
    tosrt=[""]
    for i, item in enumerate(lines):
      if lines[i] != "+++++++++++++\n":
        spli=lines[i].split('+')
        print(spli)
        td=thedate(spli)
        tb=thebook(spli)
        tn=thename(spli)
        tm=themony(spli)
        trb=td+"+"+tb+"+"+tn+"+"+tm
        print(trb)
        tosrt.append(trb)

    sortd="\n".join(sorted(tosrt))
    return sortd

#shagf = Frontdesk().process()
#print(shagf)



