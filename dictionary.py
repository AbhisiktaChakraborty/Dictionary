import json
from difflib import get_close_matches

collection = json.load(open("collection.json"))


from tkinter import *
m=Tk(className="Dictionary")
l1=Label(m, text='Enter word').grid(row=0)
box = Entry(m)
box.grid(row=0, column=1)

def callback():
    word=box.get()
    word = word.lower()
    if word in collection:
        output =collection[word]
    elif len(get_close_matches(word, collection.keys())) > 0:
        newword = get_close_matches(word, collection.keys())[0]
        print("Searching for the word --> %s" % newword)
        output=collection[newword]
    else:
        print("No word entered")
    if type(output) == list:
            for item in output:
                print(item)
    
b = Button(m, text="get", width=10, command=callback)
b.grid(row=1,column=1)
m.mainloop()
