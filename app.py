import tkinter as tk
from models import create_known_faces_table, get_known_faces
from PIL import Image, ImageTk

create_known_faces_table()

window = tk.Tk()
window.title("Facial Recognition App")
window.geometry("1920x1080")

title = tk.Label(window, text= "Facial Recognition App ", font = ("Times New Roman", 20))
title.pack(pady = 30)

status = tk.Label(window, text="The Facial Recognition is Ready")
status.pack()

faces = ["a1.jpg", "a2.jpg", "b1.jpg"]

def show_visitors():
    status.config(text="Visitor Log")


def add_visitor():
    status.config(text="Add a known visitor")


def show_known_faces():
    new_window = tk.Toplevel(window)
    new_window.title("Known Faces")
    new_window.geometry("1920x1080")

    title = tk.Label(new_window, text="Known Faces")
    title.pack(pady=30)
    for i in faces:
        photo = ImageTk.PhotoImage(Image.open(f"uploads/{i}").resize((200, 150)))
        label = tk.Label(new_window, image=photo)
        label.pack()
        label.image = photo


visitor_button = tk.Button(window, text="View the Visitors", command=show_visitors)
visitor_button.pack(pady=10)

person_button = tk.Button(window, text="Add a known visitor", command=add_visitor)  
person_button.pack(pady=10)

known_faces_button = tk.Button(window, text="View Known Faces", command=show_known_faces)
known_faces_button.pack(pady=10)


window.mainloop()

