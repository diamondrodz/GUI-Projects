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

    
if __name__ == "__main__":
     mainMenu()
top.mainloop()
