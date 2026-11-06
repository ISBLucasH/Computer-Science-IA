import tkinter as tk

window = tk.Tk()
window.title(" Welcome to the Facial Recognition App")
window.geometry("720x540")

title = tk.Label(window, text=" Welcome to the Facial Recognition App ", font=("Times New Roman", 20))
title.pack(pady=30)

status = tk.Label(window, text="", font=("Times New Roman", 12))
status.pack(pady=10)


def create_account():
    status.config(text="Create an account")


register_button = tk.Button(window, text="Register an account", command=register_an_account)
register_button.pack(pady=10)

