import json
from Task2 import year_scrapped


def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:
        Mod=int(index)%10
        decade=int(index)-Mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=int(i)+9
        for x in movies:
            if int(x)<=dec10 and int(x)>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
    with open("decade_by_year.json","w") as decade_by_year:
        json.dump(moviedec,decade_by_year,indent=4)
        return (moviedec)
scrap=(group_by_decade(year_scrapped))