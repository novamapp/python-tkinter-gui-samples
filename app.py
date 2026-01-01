import tkinter as tk
from tkinter import ttk

# def submit():
#     name_label. 

# create main window
root = tk.Tk()
root.title("Pack Layout Sample")

# set size of window
root.geometry("640x480")

name_variable = tk.StringVar(value="Unknown")

name_label = ttk.Label(root, foreground="white", background="black", textvariable=name_variable)
name_label.configure(anchor="center")
name_label.pack(fill="both", expand=True)

prompt_label = ttk.Label(root, text="Enter Name:")
prompt_label.pack(side="left", padx=10, ipady=10)

name_entry = ttk.Entry(textvariable=name_variable)
name_entry.pack(side="left", fill="x", expand=True, padx=5, pady=10)
name_entry.focus()

# submit_btn = ttk.Button(text="Submit", command=submit)
# submit_btn.pack(side="left", padx=5, pady=10)

# release to event loop
root.mainloop()