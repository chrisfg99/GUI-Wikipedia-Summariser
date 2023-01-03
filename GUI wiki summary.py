#Christopher Greer
#GUI Wikipedia Summariser
#02/01/2023

from tkinter import *
from tkinter.messagebox import showerror
from mediawiki import MediaWiki
wiki = MediaWiki()

#function to summarise wiki article
def summarise():
    try:
        summary.delete(1.0, END)
        topic = keyword.get()
        p = wiki.page(topic)
        summary.insert(INSERT, p.summary)
    except Exception as error:
        showerror("Error", error)

#initialise window
root = Tk()
root.title("Wikipedia Summariser")
root.geometry("770x650")
root.resizable(False, False)
root.configure(bg="grey")

#intialise search bar area
top_bar = Frame(root, bg="grey")
top_bar.pack(side="top", fill="x", padx=50, pady=10)

keyword = Entry(top_bar, font=("Arial", 12, "bold"), width=50, bd=4)
keyword.pack(side="left", ipady=6)

search = Button(top_bar, text="Summarise", font=("Arial", 16, "bold"),
    width=20, bd=4, command=summarise)
search.pack(side="right")

#initialise paragraph area
paragraph_box = Frame(root, bg="grey")
paragraph_box.pack(side="top", fill="x", padx=10, pady=10)

scroll = Scrollbar(paragraph_box)
scroll.pack(side="right", fill="y")

summary = Text(paragraph_box, font=("Arial", 12), fg="black",
              width=85, height=30, bd=5, yscrollcommand=scroll.set)
summary.pack(side="left", fill="y")

#loop program
root.mainloop()
