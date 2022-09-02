
#importing data
t = open("tvShow.txt", "a+")
m = open("movies.txt","a+")

tvList = t.read()
tvList = list(tvList.split(","))