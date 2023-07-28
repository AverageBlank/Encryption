# Imports
from hashes import *
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter.filedialog import asksaveasfile

# Class
class call5dia(simpledialog.Dialog):

    def __init__(self, parent, title=None, text=None):
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
    inp = filedialog.askopenfilename(initialdir = "~",title = "Select file",filetypes = ((
        ('Text Document', '*.txt'), 
        ('Python Files', '*.py'), ('All Files', '*.*'))))
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
    main2.title('Decryptor')
    main2.config(background='#666666')
    l = Label(
        main2,
        background='#272727',
        foreground='#ffffff',
        text='What do you want to decrypt?',
        font=("Arial", 15)
    )
    inp = Text(
        main2,
        height = 10000,
        width =  10000,
        background = "#272727",
        foreground = "#ffffff",
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
        text='Decrypt',
        borderwidth=0,
        command=lambda: temp(inp)
    )
    l.pack(side=TOP)
    but3.pack(fill=Y,side=BOTTOM)
    inp.pack()
    main2.mainloop()
def call3():
    def temp(a): 
        global inp
        inp = a.get("1.0", "end-1c")
        main3.destroy()
    global inp
    main3 = Tk()
    main3.geometry('1280x720')
    main3.title('Decryptor')
    main3.config(background='#666666')
    l1 = Label(
        main3,
        background='#272727',
        foreground='#ffffff',
        text='Please type in a valid encryption key',
        font=("Arial", 15)
    )
    inp = Text(
        main3,
        height = 10000,
        width =  10000,
        background = "#272727",
        foreground = "#ffffff",
        borderwidth=0,
        font=("Arial", 15),
        insertbackground="#ffffff"
    )
    but4 = Button(
        main3,
        background='#373737',
        foreground='#ffffff',
        activebackground='#878787',
        activeforeground='#ffffff',
        font=('Arial', 12),
        text='Decrypt',
        borderwidth=0,
        command=lambda: temp(inp)
    )
    l1.pack(side=TOP)
    but4.pack(fill=Y,side=BOTTOM)
    inp.pack()
    main3.mainloop()
def call4(op):
    type = [('Text Document', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')]
    temp = asksaveasfile(filetypes = type, defaultextension = type)
    temp.write(op)
    quit()
def call5(op):
    call5dia(main4, title="Output", text=op)
    quit()
# Decrypt From File Or Not.
## Tkinter
main = Tk()
main.geometry('325x75')
main.title('Decryptor')
main.config(background='#272727')
## Config
label = Label(
    main,
    background='#272727',
    foreground='#ffffff',
    text='Do you want to decrypt a text file?',
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
).pack(ipadx=30, side=LEFT,padx=10)
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
).pack(ipadx=30, side=RIGHT,padx=10)
## Running 
main.mainloop()

# Error Checking
if inp[-1] == '\n' or inp[-1] == ' ':
    inp = inp[:-1]
if len(inp) >= 5:
    b = inp[-3:]
    c = inp[-4]
    inp = inp[:-4]
    op = ''
    while b != 'ymc' or c not in 'abcdefghijklmno':
        call3()
        if len(inp) >= 5:
            b = inp[-3:]
            c = inp[-4]
            inp = inp[:-4]
            op = ''
        else:
            continue
else:
    while b != 'ymc' or c not in 'abcdefghijklmno':
        call3()
        if len(inp) >= 5:
            b = inp[-3:]
            c = inp[-4]
            inp = inp[:-4]
            op = ''
        else:
            continue
if c in 'abcde':
    hash = lvl1(a=c)
elif c in 'fghij':
    hash = lvl2(a=c)
elif c in 'klmno':
    hash = lvl3(a=c)

# Decrypting
for var in inp:
    op += hash[var]

# Saving Output
## Tkinter
main4 = Tk()
main4.geometry('425x75')
main4.title('Encrpyptor')
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
).pack(ipadx=30, side=LEFT,padx=10)
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
).pack(ipadx=30, side=RIGHT,padx=10)
## Running
main4.mainloop()