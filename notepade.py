from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

app_root = Tk()

def newFile():
    global file
    app_root.title("Untitleed - Notepad")
    file = None
    text.delete(1.0, END)

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()

            app_root.title(os.path.basename(file) + " - Notepade")
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        app_root.title(os.path.basename(file) + " - Notepade")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()



def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def find():
    pass

def helpus():
    pass

def rateus():
    pass



app_root.geometry("800x600")
#app_root.minsize(200,200)
#app_root.maxsize(2000,1600)

scb = Scrollbar(app_root)
scb.pack(side=RIGHT, fill=Y)
text = Text(app_root, yscrollcommand = scb.set)
file = None
text.pack(fill="both", expand=True)
scb.config(command=text.yview)


mainmenu = Menu(app_root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New", command=newFile)
m1.add_command(label="Save", command=saveFile)
m1.add_separator()
m1.add_command(label="Open", command=openFile)
app_root.config(menu=mainmenu)

mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=cut)
m2.add_command(label="Copy", command=copy)
m2.add_separator()
m2.add_command(label="Paste", command=paste)
m2.add_command(label="Find", command=find)
app_root.config(menu=mainmenu)

mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="help", command=helpus)
m3.add_command(label="Rate", command=rateus)
app_root.config(menu=mainmenu)

mainmenu.add_cascade(label="Help", menu=m3)

m4 = Menu(mainmenu, tearoff=0)
m4.add_command(label="Exit", command=quit)
app_root.config(menu=mainmenu)
mainmenu.add_cascade(label="Exit", menu=m4)


app_root.mainloop()