"""
Program goals:
3. Pull the values stored at specific indexes
4. Covert input to INTs
5. Put all action in a while loop
6. Add an exit option 

"""
import random
myList = []
unique_list = []


def mainProgram():
    #build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("Please choose from the following options. Type the number of the choice")
        choice = input("""1. Add to list,
2. Add bunch of numvers,
3. Get an item at an index 
4. Sort list 
5. Random Search
6. Linear Search
7. Recursive Binary Search
8. Iterative Binary Search
9. Print List 
10. Quit  """)
        if chocie == "1":
            addToList()
        elif choice == "2":
            addABunch()
        elif choice == "3":
            indexValues()
        elif choice == "4":
            sortList(myList)
        elif choice == "5":
            randomSearch()
        elif choice == "6":
            linearSearch()
        elif choice == "7":
            binSearch = input("What number are you looking for? ")
            recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
        elif choice == "8":
            binSearch = input("What number are you loking for?  ")
            result = iterativeBinarySearch(unique_list, int(binSearch))
            if result != -1:
                print("Your number is at index position {}".format(result))
            else:
                print("Your number is not found in that list, bud!")

        elif choice == "9":
            printLists()
        else:
            break


def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    myList.append(int(newItem))
    #we need to think about errors!

def addABunch():
    print("We are going to add a bunch of numbers to your list!")
    numToAdd = input ("How many new integers would you like to add?  ")
    numRange = input ("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is complete!")

def sortList(myList):
    #note that this is the first function we've bult here that takes ARGUMENTS
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Would you like to see the unique valyes in your list? Y/N ")
    if showMe.lower() =="y":
        print(unique_list)

        

def randomSearch():
    print("LOL hiii!!!")
    print(myList[random.randint(0, len(myList)-1)]
                          

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Your number is at index position{}".fomat(mid))
            return mid
         elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid-1, x)
         else:
            return recursiveBinarySearch(unique_list, mid +1, high, x)
         else:
         print("Your number isn't here!")

def mainMenu():
    clearWindow()
    LMain = Label(top, text= "Block 5 GUI projects")
    LMain.grid(column = 2, row = 1)

    B1Main = Button(text = "Week 1", bg = "white" )
    B1Main.grind(column = 2, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "white")
    B2Main.grind(column = 2, row = 3)
    
    B3Main = Button(text = "Week 3", bg = "white")
    B3Main,grind(column = 2, row = 4)
    

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:   ")
    print(myList[int(indexPos)])


def printLists():
    if len (unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see? Sorted or un-sorted? ")
        if whichOne.lower() == "sorted":
            print(unique_list)


if __name__ == "__main__":
    mainProgram()
