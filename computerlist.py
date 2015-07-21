

def begin():
    with open('newterra agents.txt') as f:
       b=[]
       
       for i in f:
       
        i= i.split(' ') 
        print i
    return

if __name__ == '__main__':
        begin()