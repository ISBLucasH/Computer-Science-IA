import tkinter as tk

window = tk.Tk()
window.title("Facial Recognition App")
window.geometry("400x300")

title = tk.Label(window, text= "Facial Recognition App ", font = ("Times New Roman", 20))
title.pack(pady = 30)

status = tk.Label(window, text="The Facial Recognition is Ready")
status.pack()



def show_visitors():
    status.config(text="Visitor Log")


def add_visitor():
    status.config(text="Add a known visitor")


visitor_button = tk.Button(window, text="View the Visitors", command=show_visitors)
visitor_button.pack(pady=10)

person_button = tk.Button(window, text="Add a Known Visitor", command=add_visitor)  
person_button.pack(pady=10)

window.mainloop()