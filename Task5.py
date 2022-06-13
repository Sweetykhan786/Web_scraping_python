import json
import requests
from bs4 import BeautifulSoup
# import pprint


# movie_list=[]
def get_movie_list_details(movie_list):
    with open("top_movies.json","r") as f1:
        data=json.load(f1)
        # pprint.pprint(data)
        for i in range(80,100):
            # print(i)
            url=requests.get(data[i]["movie_url"])
            htmlcon=url.content
            # print(htmlcon)
            soup=BeautifulSoup(htmlcon,"html.parser")
            # pprint.pprint(soup) 
            ul=soup.find("ul",class_="content-meta info")
            # print(ul)
            li=ul.find_all("li",class_="meta-row clearfix")
            dict={}
            h1=soup.find('h1',class_='scoreboard__title').get_text()
            dict.update({"movie name":h1}) 
            for i in li:
                key=i.find("div",class_="meta-label subtle").get_text().strip().replace(":", "")
                Value=i.find("div",class_="meta-value").get_text().strip().replace("\n","").replace(" ","")
                if key!="Genre" and key!="Original Language"  and key!="Director" and key!="Writer":
                    dict.update({key:Value})
                else:
                    new_value=Value.replace(",","")
                    value_list=new_value.split()
                    dict.update({key:value_list})
            movie_list.append(dict)
            # print(a)
        print(movie_list)   
        with open("5thTaskResult.json","w") as file:
            json.dump(movie_list,file,indent=4)     

get_movie_list_details([])