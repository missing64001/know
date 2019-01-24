


def get_m(x,bll,has):

    lst = list(range(QS,END+1,1))

    totle = sum(lst)

    bl = 2000 / totle
    bl = bll
    # print (bl)
    last_c = 0
    totle_c = 0
    for l in lst:
        last_c = (l-totle_c) *bl
        totle_c += last_c
        if round(l-totle_c,0) == x:
            print(l,round(l-totle_c,0),round(totle_c-has,0))

    return (totle_c)





def get_start():

    start = 1
    bc = 0.05
    last = 0
    last_now = 0
    for i in range(200):
        now = get_m(MB,start,0)
        if now > MB:
            start = start*(1-bc)
            if last == -1:
                bc = bc / 4
            last = 1
        else:
            start = start*(1+bc)
            if last == 1:
                bc = bc / 4
            last = -1
        print(now,start)
        if last_now == now:
            print(i)
            break
        last_now = now


MB = 2000
QS = 200
END = 5000

# get_start()

has = 0+3

print (round(get_m(2000,0.00022541628,has),-1))