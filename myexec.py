



def show_by_seconds(dd):
    fh = ''
    if dd <0:
        dd = -dd
        fh = '-'

    S = dd % 60
    dd = int(dd / 60)

    xx = dd
    M = dd % 60

    dd = int(dd / 60)

    H = dd % 60
    H = dd % 24

    day = int(dd / 24)
    return 'rest %s%s:%02d:%02d:%02d'%(fh,day,H,M,S)

# from datetime import datetime
d1 = datetime.datetime.strptime('20181206 15:21:24', '%Y%m%d %H:%M:%S')



d2 = models.Label.objects.get(id=4).create_date + datetime.timedelta(hours=8)
print(d2)



x = time.mktime(d1.timetuple())
x2 = time.mktime(d2.timetuple())
zz = (time.time()-x)
print(show_by_seconds(zz))



