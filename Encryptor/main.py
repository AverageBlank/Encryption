# Imports
from hashes import *
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter.filedialog import asksaveasfile


# Class
class Call5Dia(simpledialog.Dialog):

    def __init__(self, parent, title=None, text=None):
        self.text = None
        self.data = text
        simpledialog.Dialog.__init__(self, parent, title=title)

    def body(self, parent):
        self.text = Text(self, width=40, height=4)
        self.text.pack(fill="both", expand=True)

        self.text.insert("1.0", self.data)

        return self.text


# Callbacks
def call1():
    global inp
    inp = filedialog.askopenfilename(initialdir="~", title="Select file",
                                     filetypes=(("All Files", "*."), ("All Files", "*.*")))
    print(inp)
    file = open(inp, 'r')
    l = file.readlines()
    inp = ''
    for index in l:
        inp += index
    main.destroy()
    return inp


def call2():
    def temp(a):
        global inp
        inp = a.get("1.0", "end-1c")
        main2.destroy()

    global inp
    main.destroy()
    main2 = Tk()
    main2.geometry('1280x720')
    main2.title('Encryptor')
    main2.config(background='#666666')
    l = Label(
        main2,
        background='#272727',
        foreground='#ffffff',
        text='What do you want to encrypt?',
        font=("Arial", 15)
    )
    inp = Text(
        main2,
        height=10000,
        width=10000,
        background="#272727",
        foreground="#ffffff",
        borderwidth=0,
        font=("Arial", 15),
        insertbackground="#ffffff"
    )
    but3 = Button(
        main2,
        background='#373737',
        foreground='#ffffff',
        activebackground='#878787',
        activeforeground='#ffffff',
        font=('Arial', 12),
        text='Encrpyt',
        borderwidth=0,
        command=lambda: temp(inp)
    )
    l.pack(side=TOP)
    but3.pack(fill=Y, side=BOTTOM)
    inp.pack()
    main2.mainloop()


def call3(n):
    global hash
    global decr
    global op
    op = ''
    if n == 1:
        hash, decr = lvl1()
    elif n == 2:
        hash, decr = lvl2()
    elif n == 3:
        hash, decr = lvl3()
    for var in inp:
        op += hash[var]
    op += decr
    op += 'ymc'
    main3.destroy()
    return op


def call4(op):
    filetype = [('Text Document', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')]
    temp = asksaveasfile(filetypes=filetype, defaultextension=filetype)
    temp.write(op)
    quit()


def call5(op):
    Call5Dia(main4, title="Output", text=op)
    quit()


# Encrypt From File Or Not.
## Tkinter
main = Tk()
main.geometry('325x75')
main.title('Encrpyptor')
main.resizable(0, 0)
main.config(background='#272727')
## Config
label = Label(
    main,
    background='#272727',
    foreground='#ffffff',
    text='Do you want to encrypt a text file?',
    font=("Arial", 15)
).pack()
but1 = Button(
    main,
    background='#373737',
    foreground='#ffffff',
    activebackground='#878787',
    activeforeground='#ffffff',
    font=('Arial', 12),
    text='Yes',
    borderwidth=0,
    command=lambda: call1()
).pack(ipadx=30, side=LEFT, padx=10)
but2 = Button(
    main,
    background='#373737',
    foreground='#ffffff',
    activebackground='#878787',
    activeforeground='#ffffff',
    font=('Arial', 12),
    text='No',
    borderwidth=0,
    command=lambda: call2(),
).pack(ipadx=30, side=RIGHT, padx=10)
## Running 
main.mainloop()

# Removing Empty whitespace
if inp[-1] == '\n' or inp[-1] == ' ':
    inp = inp[:-1]

# Level of encryption
## Tkinter
main3 = Tk()
main3.geometry('415x75')
main3.title('Encrpyptor')
main3.resizable(0, 0)
main3.config(background='#272727')
## Config
l1 = Label(
    main3,
    background='#272727',
    foreground='#ffffff',
    text='What level do you want to encrypt at?',
    font=("Arial", 15)
).pack()
but4 = Button(
    main3,
    background='#373737',
    foreground='#ffffff',
    activebackground='#878787',
    activeforeground='#ffffff',
    font=('Arial', 12),
    text='Level 1',
    borderwidth=0,
    command=lambda: call3(1)
).pack(ipadx=30, side=LEFT, padx=10)
but5 = Button(
    main3,
    background='#373737',
    foreground='#ffffff',
    activebackground='#878787',
    activeforeground='#ffffff',
    font=('Arial', 12),
    text='Level 3',
    borderwidth=0,
    command=lambda: call3(3),
).pack(ipadx=30, side=RIGHT, padx=10)
but6 = Button(
    main3,
    background='#373737',
    foreground='#ffffff',
    activebackground='#878787',
    activeforeground='#ffffff',
    font=('Arial', 12),
    text='Level 2',
    borderwidth=0,
    command=lambda: call3(2),
).pack(ipadx=30, side=RIGHT, padx=10)
## Running
main3.mainloop()

# Saving output
## Tkinter
main4 = Tk()
main4.geometry('425x75')
main4.title('Encrpyptor')
main4.resizable(0, 0)
main4.config(background='#272727')
## Config
l2 = Label(
    main4,
    background='#272727',
    foreground='#ffffff',
    text='Do you want to save the output to a text file?',
    font=("Arial", 15)
).pack()
but1 = Button(
    main4,
    background='#373737',
    foreground='#ffffff',
    activebackground='#878787',
    activeforeground='#ffffff',
    font=('Arial', 12),
    text='Yes',
    borderwidth=0,
    command=lambda: call4(op)
).pack(ipadx=30, side=LEFT, padx=10)
but2 = Button(
    main4,
    background='#373737',
    foreground='#ffffff',
    activebackground='#878787',
    activeforeground='#ffffff',
    font=('Arial', 12),
    text='No',
    borderwidth=0,
    command=lambda: call5(op),
).pack(ipadx=30, side=RIGHT, padx=10)
## Running
main4.mainloop()
