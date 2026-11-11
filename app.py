import tkinter as tk
from models import create_known_faces_table, get_known_faces
from PIL import Image, ImageTk
from tkinter import filedialog

create_known_faces_table()

window = tk.Tk()
window.title("Facial Recognition App")
window.geometry("720x540")

title = tk.Label(window, text= "Facial Recognition App ", font = ("Times New Roman", 30, "bold"))
title.pack(pady = 30)

status = tk.Label(window, text="The Facial Recognition is Ready")
status.pack()

faces = ["a1.jpg", "a2.jpg", "b1.jpg"]

def scan():
    new_window = tk.Toplevel(window)
    new_window.title("Scanner")
    new_window.geometry("720x540")


def add_visitor():
    status.config(text="Add a known visitor")
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    

def settings():
    new_window = tk.Toplevel(window)
    new_window.title("Settings")
    new_window.geometry("720x540")

    title = tk.Label(new_window, text="Settings", font=("Times New Roman", 30, "bold"))
    title.pack(pady=30)

    logout_button = tk.Button(new_window, text="Log Out", command=window.destroy)
    logout_button.pack(pady=10)

    account_information_button = tk.Button(new_window, text = "Account Information")
    account_information_button.pack(pady=10)

    clear_known_faces_button = tk.Button(new_window, text="Clear Known Faces")
    clear_known_faces_button.pack(pady=10)

    clear_visitor_log_button = tk.Button(new_window, text="Clear Visitor Log")
    clear_visitor_log_button.pack(pady=10)

    back_button = tk.Button(new_window, text=" <--- Back", command=new_window.destroy)
    back_button.place(x=10, y=10)


def show_known_faces():
    new_window = tk.Toplevel(window)
    new_window.title("Known Faces")
    new_window.geometry("720x540")

    title = tk.Label(new_window, text="Known Faces")
    title.pack(pady=30)
    for i in faces:
        photo = ImageTk.PhotoImage(Image.open(f"uploads/{i}").resize((200, 150)))
        label = tk.Label(new_window, image=photo)
        label.pack()
        label.image = photo

    back_button = tk.Button(new_window, text=" <--- Back", command=new_window.destroy)
    back_button.place(x=10, y=10)

settings_button = tk.Button(window, text="Settings", command=settings)
settings_button.place(x=600, y=10)


scan_button = tk.Button(window, text="Scan", command=scan)
scan_button.config(font=("Times New Roman", 10))
scan_button.pack(pady=10)

person_button = tk.Button(window, text="Add a known visitor", command=add_visitor)  
person_button.pack(pady=10)

known_faces_button = tk.Button(window, text="View Known Faces", command=show_known_faces)
known_faces_button.pack(pady=10)
    

    
window.mainloop()

