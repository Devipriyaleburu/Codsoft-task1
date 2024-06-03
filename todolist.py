#importing modules
from tkinter import *
from tkinter import messagebox
#creating functions
def enter():
    tasks = entry.get()
    if tasks != "":
        Listbox1.insert(END, tasks)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Enter any task.")

def removeTask():
    Listbox1.delete(ANCHOR)

 #creating window   
window= Tk()
window.geometry('550x450+550+300')
window.title('Codsoft_todolist')
window.config(bg='#008080')
window.resizable(width=False, height=False)
#creating a frame 
f= Frame(window)
f.pack(pady=15)
#creating list box storing tasks
Listbox1 = Listbox(
    f,
    width=30,
    height=8,
    font=('Times', 15),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#C0C0C0',
    activestyle="none",
    )
Listbox1.pack(side=LEFT, fill=BOTH)
# code for adding tasks into listbox1
list=[

]

for i in list:
    Listbox1.insert(END, i)
#code for scroll bar
scrollbar= Scrollbar(f)
scrollbar.pack(side=RIGHT, fill=BOTH)

Listbox1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Listbox.yview)

entry = Entry(
    window,
    font=('times', 20),
    text='enter a new text'
    )

entry.pack(pady=20)

#code for creating button frames 
bframe = Frame(window)
bframe.pack(pady=20)
#addbutton for adding tasks
addbutton = Button(
    bframe,
    text='ADDTASK',
    font=('times 14'),
    bg='#00FFFF',
    padx=20,
    pady=10,
    
    command=enter
)
addbutton.pack(fill=BOTH, expand=True, side=LEFT)
#button removing tsks
deleletebutton = Button(
    bframe,
    text='REMOVETASK',
    font=('times 14'),
    bg='#FFFF00',
    padx=20,
    pady=10,
    command=removeTask
    )
deleletebutton.pack(fill=BOTH, expand=True, side=LEFT)


window.mainloop()