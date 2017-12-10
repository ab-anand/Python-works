from Tkinter import *
from gnewsclient import gnewsclient, utils

top = Tk()
client = gnewsclient()
def func(value):
    print(value)



L1 = Label(top, text="Edition", wraplength=200)
L1.pack(side = LEFT)
options_edition = [key for key in utils.editionMap]
var = StringVar()
drop = OptionMenu(top, var, *options_edition, command=func)
drop.pack(side=	RIGHT, padx = 5, pady = 5)

L2 = Label(top, text="Topic", wraplength=200)
L2.pack(side = LEFT)
options_topic = [key for key in utils.topicMap]
var = StringVar()
drop = OptionMenu(top, var, *options_topic, command=func)
drop.pack(side=	RIGHT, padx = 5, pady = 5)

L3 = Label(top, text="Language", wraplength=200)
L3.pack(side = LEFT)
options_lang = [key for key in utils.langMap]
var = StringVar()
drop = OptionMenu(top, var, *options_lang, command=func)
drop.pack(side=	RIGHT, padx = 5, pady = 5)

L4 = Label(top, text="Location", wraplength=200)
L4.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT, padx = 5, pady = 5)
# Code to add widgets will go here...


    
top.maxsize(width=666, height=666)
top.resizable(width=False, height=False)
top.mainloop()
