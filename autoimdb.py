import imdb
from spinner import Spinner
import os
import sys

#Yoo hello, guess you are from the future
#This program adds the imdb score of your pirated movies. It renames files and folders
#make sure to install IMDbpy
#python3 {dir to this file} {dir to your movies folder}
#good luck
#jul 24 2021 23:03

#colors for colored terminal outs
class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    c = '\033[96m'#cyan
    g = '\033[92m'#green
    y = '\033[93m'#yellow
    r = '\033[91m'#red
    e = '\033[0m'#END thing
    b = '\033[1m'#bold
    u = '\033[4m'#underline

#july neydi!?!?!?

is_test = False

def cleanName(s,is_file):

    stoppers = ['(','20','[','.20','19']

    if(is_file):
        i_end = s.rfind('.')
        s = s[:i_end]

    s = s.replace('.',' ')
    
    for c in stoppers:
        i = s.find(c)
        if(i != -1):
            break    

    if(i != -1):
        s = s[:i]

    return s

def getRating(movie_name):
    print(f"Getting rating for: {bc.b}{movie_name}{bc.e}")
    movie = None

    with Spinner():
        try:
            movies = ia.search_movie(movie_name)

            movie = movies[0]

            ia.update(movie)
        except:
            print(f'{bc.y}Error on: {movie_name}{bc.e}')
            return None

    # return movie
    director = "None"
    try:
        director = movie['director'][0]['name']
    except:
        pass

    if('rating' in movie and 'title' in movie):
        print(f"{movie['title']} by {director}: {bc.c}{bc.b}{movie['rating']}{bc.e}{bc.e}")
        return movie['rating']
    
    print(f'{bc.y}Error getting vals on {movie_name}{bc.e}')

    return None

def editFile(file_name,movie_name):
    rating = getRating(movie_name)

    if rating is None:
        return
    
    new_name = f"{rating} {file_name}"

    os.rename(f"{dir}/{file_name}",f"{dir}/{new_name}")

try:
    ia = imdb.IMDb()
except:
    raise('Error on initing imdb')

if(not is_test):
    dir = sys.argv[1]
else:
    dir = 'movies'

dirs = os.listdir(dir)

if(not is_test):
    print(f"Starting process in {bc.b}{dir}{bc.e} on {len(dirs)} movies?")
    print(f"{bc.g}y{bc.e} or {bc.r}n{bc.e}")

    if(input() != 'y'):
        raise('Canceled')

for d in dirs:
    if(d[0] == '.'):
        continue
    
    is_file = os.path.isfile(f"{dir}/{d}")

    # print(is_file)
    # print(cleanName(d,is_file))
    # clean up the name
    n = cleanName(d,is_file)
    
    editFile(d,n)