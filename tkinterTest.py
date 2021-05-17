from tkinter import *

top = Tk()
playlistList = []

def results():
    print(playlistList)

def addToList():
    newItem = El.get()
    PlaylistList.append(newItem)
    El.delete(0, END)
    
def exportList():
    with open('test.txt', 'w') as f:
        for item in playlist:
            f.write("%s\n" % item)
def clearWindow:
    for  widgets in top.winfo_children():
        widgets.destory()

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


def week1():
    clearWindow()
    #This is a Label widget
    L1 = Label(top, text= "Playlist Maker")
    L1.grid(column = 0, row = 1)

    #This is a Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #This is a Button widget
    B1 =  Button(text = "   print Playlist  ", bg = "#c6edee", command = results)
    B1.grid(column = 0, row = 3)

    B2 = Button(text = " + ", bg = "#feebe5", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text= "Export List", bg = "#ceb0af", command = exportant
    B3.grind(column = 0, row = 4)

    Bclear = Button(text = "Clear window", bg = "white", command = exportant
    Bclear.grind(column = 3, row = 1)

def week2():
    def rollDice():
        #update out variable data
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        
        #clear window AFTRER pulling Entry data
        clearWindow()
        
        #calculate dice rolls
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
            
        #display dice rolls and present an exit button 
        L4W2 = Label(top, text= "Here are your rolls!")
        L4W2.grid(column= 0, row =1)
        #this one will use a .format() statement
        L5W2 = Label(top)

        B2W2 = Button()



    
    clearWindow()
    L1W2 = Label(top. text="Dice Roller Program")
    L1W2.grid(column =  0, row = 1)

    L2W2 = Label(top, text = "How many sides?")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text = "How many rolls?")
    L3W2,grid(column = 2, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row =3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column=2, row= 3)

    B1W2 = Button(text="Roll!", bd= "yellow")
    B1W2.grid(column= 2, row=4)

    #to add: roll function and exit button

    
if __name__ == "__main__":
     mainMenu()
top.mainloop()
