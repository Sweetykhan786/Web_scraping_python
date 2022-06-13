import json
from pprint import pprint
# from pprint import pprint
from bs4 import BeautifulSoup
import requests


movie_details=[]
def scrap_movie_details(movie_url):
    d={}
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,'html.parser')
    # print(soup)
    
    title1=soup.find('div',class_="col mob col-center-right col-full-xs mop-main-column")
    # print(title1)
    
    til=title1.find('div',class_="thumbnail-scoreboard-wrap")
    # print(til)
    
    h1=til.find('h1',class_="scoreboard__title").get_text()
    # print(h1)
    d['name']=h1
    # print(d)
    movie_bio=soup.find('div',class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
    # print(movie_bio)
    d["bio"]=movie_bio
    ul=soup.find('ul',class_="content-meta info")
    # print(ul)
    
    li=ul.find_all('li',class_="meta-row clearfix")
    # print(li)
    for i in li:
        d[i.find('div',class_='meta-label subtle').text]="".join(i.find('div',class_="meta-value").text.split())
        movie_details.append(d)
        # print(d)
        
    with open("movie_details_of_task4.json","w") as f1:
        json.dump(movie_details[::14],f1,indent=4)
        
    with open("movie_details_of_task4.json","r") as f3:
        d=json.load(f3)
        print(d[::14])
        
data=scrap_movie_details("https://www.rottentomatoes.com/m/black_panther_2018") 
pprint(data)
    