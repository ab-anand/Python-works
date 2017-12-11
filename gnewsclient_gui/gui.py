from Tkinter import *
from gnewsclient import gnewsclient, utils

top = Tk()
client = gnewsclient()
top.title('GNEWSCLIENT')

edition = 'United States (English)'
topic = 'top stories'
language = 'english'
location = None

def edition_func(value):
    global edition
    edition = value

def topic_func(value):
    global topic
    topic = value

def lang_func(value):
    global language
    language = value

def submit():
	print(E1.get())

L1 = Label(top, text="Edition", padx=5, pady=5,fg="red")
L1.pack( fill=X)
options_edition = [key for key in utils.editionMap]
var = StringVar()
drop = OptionMenu(top, var, *options_edition, command=edition_func)
drop.pack(padx = 5, pady = 5, fill=X)

L2 = Label(top, text="Topic",fg="red")
L2.pack(fill=X)
options_topic = [key for key in utils.topicMap]
var = StringVar()
drop = OptionMenu(top, var, *options_topic, command=topic_func)
drop.pack(padx = 5, pady = 5, fill=X)

L3 = Label(top, text="Language",fg="red")
L3.pack(fill=X)
options_lang = [key for key in utils.langMap]
var = StringVar()
drop = OptionMenu(top, var, *options_lang, command=lang_func)
drop.pack(padx = 5, pady = 5, fill=X)

L4 = Label(top, text="Location",fg="red")
L4.pack(fill=X)
E1 = Entry(top, bd =5)
E1.pack(padx = 5, pady = 5, fill=X)


submit_button = Button(top, text="Submit", command=submit)
submit_button.pack(fill=X)
# Code to add widgets will go here...


top.minsize(width=266, height=300)    
top.maxsize(width=666, height=666)
top.resizable(width=False, height=False)
top.mainloop()
