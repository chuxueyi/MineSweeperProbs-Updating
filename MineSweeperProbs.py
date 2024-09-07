from queue import Empty


c=15
r=10
cr=c*r
m=[m for m in range(start=1,stop=cr+1,step=2)]

ba=[]

class Board:
    b=[]
    ra=[]
    def __init__(self,last_board,c,r,cr,m) -> None:
        b=[' 'for x in range(start=0,stop=cr)]
        if last_board is Empty:
            for i in range(start=0,stop=m):
                b[i]='*'
        else:


            def last_mine():
                for i in range(start=cr-1,stop=-1,step=-1):


        
    




for i in range(start=0,stop=cr):
    if b[i]==' ':
        rt=Route(i,m,cr)
        ra.append(rt)           


class Route:
    r=[]
    p=0.0
    def __init__(self,start,mines,total) -> None:
        r.clear
        r.append(start)
        p=(total-mines)/total
    def sweep_sure()->None:
