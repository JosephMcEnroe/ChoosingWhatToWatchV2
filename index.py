#Importing Data
import os
from random import randint

"""
    PROGRAM CONSTANTS
"""
TV_SHOWS = 1
MOVIES = 2

TV_SHOWS_FILENAME = "tvShows.txt"
MOVIES_FILENAME = "movies.txt"

"""
    Keep track of the tv show and movie lists
"""
tv_shows = []
movies = []


"""
    This method will take the name of a file, open it in appending more, read the contents
    and returns a list of contents in the file
"""
def load_list_from_file(filename):
    if not filename:
        raise "file name cannot be null or empty"
    
    contents = []
    with open(filename, "r+") as file:
        lines = file.readlines()
        for line in lines:
            for item in line.strip().split(","):
               contents.append(item)
    file.close()
    return contents

    


"""
    This takes a movie or tv show and add it to the file
"""
def write_to_file(filename, content):
    if not filename:
        raise "file name cannot be null or empty"
    
    if not content:
        raise "The movie or show to add to the file cannot be empty"
    
    file = open(filename, "a")
    #we dont want to add , to a file if we are writing to it for the first time
    if os.stat(filename).st_size == 0:
        file.write(content)
    else:
        file.write("," + content)
    
    file.close()

"""
    This show the menu options
"""

def menu():
    #prints out menu
    print("\t\tMenu")
    print("1)\tChoose a Random TV Show")
    print("2)\tChoose a Random Movie")
    print("3)\tAdd a TV Show to Watch")
    print("4)\tAdd a Movie to Watch")
    print("5)\tSaved Movie and TV shows")
    print("6)\tExit Program")


def pick_random_item_to_watch(choice):
    if choice!=TV_SHOWS and choice!=MOVIES:
        raise "Invalid choice"
    
    if choice == TV_SHOWS and tv_shows:
        pick = randint(0, len(tv_shows)-1)
        print(tv_shows[pick])
    elif choice == MOVIES and movies:
        pick = randint(0, len(movies) - 1)
        print(movies[pick])
    
    else:
        item_type =  'TV Show'
        if choice == MOVIES:
            item_type = 'movie'
        print(f'No available {item_type} to show as the list is empty')


def show_all():
    print("TV Shows\n--")
    for show in tv_shows:
        print(show)
    
    print("-------------")
    print("Movies\n--")
    for movie in movies:
        print(movie)
        
def add_to_list(item_type):
    list_type = "TV shows"
    filename = TV_SHOWS_FILENAME
    if item_type == MOVIES:
        list_type = "movies"
        filename = MOVIES_FILENAME
    
    seperator = "','"
    recommendations = input(f'What do you want to add to the list(split {list_type} using {seperator}):')
    if not recommendations:
        print(f'skipping writing recommendation(s) of {list_type} since it is empty...')
        return False
    
    write_to_file(filename, recommendations)

    #update the appropriate list
    if item_type == TV_SHOWS:
        tv_shows.extend(recommendations.split(','))
    else:
        movies.extend(recommendations.split(','))
    return True


def main():
    tv_shows.extend(load_list_from_file(TV_SHOWS_FILENAME))
    movies.extend(load_list_from_file(MOVIES_FILENAME))
    while True:
        menu()
        choice = int(input("selection: "))
        match choice:
            case 1:
                pick_random_item_to_watch(TV_SHOWS)
            case 2:
                pick_random_item_to_watch(MOVIES)
            case 3:
                add_to_list(TV_SHOWS)
            case 4:
                add_to_list(MOVIES)
            case 5:
                show_all()
            case 6:
                break
            case _:
                print("Invalid choice! Please pick a choice between 1-6")

    print("Thank You for using my program :D")
    print("Created by Joseph McEnroe")

main()

