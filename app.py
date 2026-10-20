import tkinter as tk
from models import create_known_faces_table, get_known_faces

create_known_faces_table()

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


def show_known_faces():
    new_window = tk.Toplevel(window)
    new_window.title("Known Faces")
    new_window.geometry("400x300")

    title = tk.Label(new_window, text="Known Faces")
    title.pack(pady=30)


visitor_button = tk.Button(window, text="View the Visitors", command=show_visitors)
visitor_button.pack(pady=10)

person_button = tk.Button(window, text="Add a known visitor", command=add_visitor)  
person_button.pack(pady=10)

known_faces_button = tk.Button(window, text="View Known Faces", command=show_known_faces)
known_faces_button.pack(pady=10)


window.mainloop()

#create my database table before friday lesson.


