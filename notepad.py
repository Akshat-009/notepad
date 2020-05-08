from tkinter import *
import os 
from tkinter.filedialog import askopenfilename,asksaveasfilename
import tkinter.messagebox as ms 
root=Tk()
root.geometry("644x533")
root.title("Notepad")
text=Text(root)
text.pack(fill=BOTH,expand=True)
file=None
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files ","*.*")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ "-Notepad")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())    
        f.close 
def savefile():
    print("saving")
    global file 
    if file ==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ "-Notepad")

    else:
        f.open(file,"w")
        f.write(text.get(1.0,END))
        f.close()        
        
def newfile():
    text.delete(1.0,END)
    
def cut():
    text.event_generate("<<Cut>>")
def copy():
    text.event_generate("<<Copy>>")
def paste():
    text.event_generate("<<Paste>>")
mainmenu=Menu(root)
filemenu=Menu(mainmenu,tearoff=0)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_command(label="New",command=newfile)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=quit)
mainmenu.add_cascade(label="File",menu=filemenu)
editmenu=Menu(mainmenu,tearoff=0)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
mainmenu.add_cascade(label="Edit",menu=editmenu)
root.config(menu=mainmenu)
#scroll bar
scrollbar=Scrollbar(text)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)


root.mainloop()