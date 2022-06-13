import json
with open("5thTaskResult.json","r") as file:
    data=json.load(file)

def analysis_movie_language(movie_list):
    language_list=[]
    list=[]
    for i in range(len(movie_list)):
        for j in range(len(movie_list[i]["Original Language"])):
            if movie_list[i]["Original Language"][j] not in language_list:
                language_list.append(movie_list[i]["Original Language"][j])
                # print(language)
            list.append(movie_list[i]["Original Language"][j])
    language_d={i:"" for i in language_list}
    for x,y in language_d.items():
        count=0
        for i in range(len(list)):
            if x==list[i]:
                count+=1
                language_d[x]=count
    print(language_d)
    with open("analysis_language.json","w") as filename:
        json.dump(language_d,filename,indent=4)

analysis_movie_language(data)
