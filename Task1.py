import json
from bs4 import BeautifulSoup
import pprint
import requests



def scrap_of_movies():
    url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    a=requests.get(url)
    htmlcontent=a.content
    soup=BeautifulSoup(htmlcontent,'html.parser')

    table=soup.find("table", class_="table")    
    tr=table.find_all("tr")
# print(tr)
    top_movie=[]
    # serno=1
    for i in tr:
        rank_of_movie=i.find_all("td",class_="bold")
        for j in rank_of_movie:
            rank=j.get_text()
            # print(rank)
        rating_of_movie=i.find_all("span",class_="tMeterScore")
        for rate in rating_of_movie:
            rating=rate.get_text().strip()
        name_of_movie=i.find_all("a",class_="unstyled articleLink")
        for name in name_of_movie:
            title=name.get_text().strip()
            list=title.split()
            length_name=len(list)-1
            name=""
            for l in range(length_name):
                name+=list[l]
            name_of_movie=name
        reviews=i.find_all("td",class_="right hidden-xs")
        for revi in reviews:
            reviews=revi.get_text()
            # print(reviews)
        url1=i.find_all("a",class_="unstyled articleLink")
        for i in url1:
            # print(i)
            link=i["href"]
            movies_link="https://www.rottentomatoes.com"+link
            newurl=requests.get(movies_link)
            htmlcon=newurl.content
            soup1=BeautifulSoup(htmlcon,"html.parser")
            div=soup1.find("div",class_="col mob col-center-right col-full-xs mop-main-column")
            div1=div.find("div",class_="thumbnail-scoreboard-wrap").p.get_text()
            year=div1[:4]
            print(movies_link)
            details_of_movie={"movie_rank":"","movie_rating":"","movie_name":"","movie_reviews":"","movie_url":"","year":""}
            details_of_movie["movie_rank"]=rank
            details_of_movie["movie_rating"]=rating
            details_of_movie["movie_name"]=name_of_movie
            details_of_movie["movie_reviews"]=reviews
            details_of_movie["movie_url"]=movies_link
            details_of_movie["year"]=year
            top_movie.append(details_of_movie)
            pprint.pprint(top_movie)
    with open("top_movies.json","w")as file:
        json.dump(top_movie,file,indent=4)
        return top_movie
scrapped=scrap_of_movies()