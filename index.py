#importing rand
from random import randint

#importing data
t = open("tvShow.txt", "a+")
t = open("tvShow.txt","r+")
m = open("movies.txt","a+")
m = open("movies.txt","r+")


#importing data into list
tvList = t.read()
tvList = list(tvList.split(","))

movieList = m.read()
movieList = list(movieList.split(","))

#menu
def menu():
    #prints out menu
    print("\t\tMenu")
    print("1)\tChoose a Random TV Show")
    print("2)\tChoose a Random Movie")
    print("3)\tAdd a TV Show to Watch")
    print("4)\tAdd a Movie to Watch")
    print("5)\tSaved Movies and TV shows")
    print("6)\tExit Program")

def chooseFromMenu():
    #takes in choice and validates it to see if in range
    while True:
        menu()
        choice = int(input("selection: "))
        if choice >= 0 and choice <= 6:
            return choice

def randomNum(choice):
    #picks a random number based on the list's range
    import random 
    if choice == 1:
        return(randint(0,len(tvList)-1))
    elif choice == 2:
        return(randint(0,len(movieList)-1))
    else: 
        return None

def addtoList(choice):
    #adds to data file
    if choice == 3:
        addingList = input("What do you want to add to list(split TV shows using ','):")
        t.write(addingList)
        tvList.append(addingList.split(","))
    if choice == 4:
        addingList = input("What do you want to add to list(split movies using ','):")
        m.write(addingList)
        movieList.append(addingList.split(","))
    else:
        return None

def printChoice(choice,rand):
    #prints out choice for the night
    if choice == 1:
        print(tvList[rand])
    elif choice == 2:
        print(movieList[rand])

def printLists(choice):
    #prints out all the TV shows and Movies Saved
    if choice == 5:
        print("TV Shows\n--")
        for index in tvList:
            print(index)
        print("-------------")
        print("Movies\n--")
        for index in movieList:
            print(index)

def main():
#main method
    choice = chooseFromMenu()
    while  choice != 6:
        randNum = randomNum(choice)
        addtoList(choice)
        printChoice(choice,randNum)
        printLists(choice)
        choice = chooseFromMenu()
           
main()


