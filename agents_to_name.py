

def begin():
    with open('outputfile.txt') as f:
       b=[]
       
       for i in f:
          spot = i.find(',')
          computername = i[:spot]#b=  b.split(',',1)
          date= i[spot+1:len(i)]
          print "Name %s ==>Date %s" %(computername, date)
    return

if __name__ == '__main__':
        begin()