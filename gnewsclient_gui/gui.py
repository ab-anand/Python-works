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

def create_window():
    window = Toplevel(top)
    # L1 = Label(window, text="Edition", fg="red")
    # L1.grid(row=0, pady=10)
    # options_edition = [key for key in utils.editionMap]
    # var = StringVar()
    # var.set(edition)
    # drop = OptionMenu(window, var, *options_edition, command=edition_func)
    # drop.grid(row=0, column=1, pady=10)


# edition filter
L1 = Label(top, text="Edition", fg="red")
L1.grid(row=0, pady=10)
options_edition = [key for key in utils.editionMap]
var = StringVar()
var.set(edition)
drop = OptionMenu(top, var, *options_edition, command=edition_func)
drop.grid(row=0, column=1, pady=10)


# topic filter
L2 = Label(top, text="Topic", fg="red")
L2.grid(row=1, pady=10)
options_topic = [key for key in utils.topicMap]
var = StringVar()
var.set(topic)
drop = OptionMenu(top, var, *options_topic, command=topic_func)
drop.grid(row=1, column=1, pady=10)


# language filter
L3 = Label(top, text="Language", fg="red")
L3.grid(row=2, pady=10)
options_lang = [key for key in utils.langMap]
var = StringVar()
var.set(language)
drop = OptionMenu(top, var, *options_lang, command=lang_func)
drop.grid(row=2, column=1, pady=10)


# location filter
L4 = Label(top, text="Location", fg="red")
L4.grid(row=3, pady=10)
E1 = Entry(top, bd =5)
E1.grid(row=3, column=1, pady=10)

# submit button
submit_button = Button(top, text="Submit", command=create_window)
submit_button.grid(row=4, column=0, pady=10, columnspan=4)


top.minsize(width=266, height=200)    
top.maxsize(width=666, height=666)
top.resizable(width=False, height=False)
top.mainloop()
