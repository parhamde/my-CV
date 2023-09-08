#imports library
from tkinter import *
from tkinter import filedialog

#window
root=Tk()
root.geometry("500x600")
root.title("Notpad")
root.iconbitmap("icons8-notepad-70.ico")

#function button save
def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()
#function  button clear
def clear():
    print('')
#function button open_file
def open_file():
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)

#great lebel
I1 = Label(root,bg="black",width=500,height=3)
I1.grid(sticky="w")
#save button 
b1=Button(root,text="save file",command= save_file)
b1.place(x=10,y=10)
#clear button
b2=Button(root,text="clear",command=clear)
b2.place(x=74,y=10)
#open file
b3=Button(root,text="open file",command= open_file)
b3.place(x=120,y=10)
#entry box
entry=Text(root,height=30,width=58,wrap=WORD ,fg="black",bg="GRAY")
entry.place(x=10,y=65)

root.mainloop()