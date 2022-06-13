import json
from Task1 import scrapped
years=[]
def group_by_year(movies):
    for i in movies:
        year=i["year"]
            # print(year1)
        if year not in years:
            years.append(year)
    movie_dict={i:[] for i in years}
    for i in movies:
            # name=i
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    with open("year_of_movies.json","w") as separate_movie:
        json.dump(movie_dict,separate_movie,indent=4)
        return movie_dict
year_scrapped=(group_by_year(scrapped))                
                