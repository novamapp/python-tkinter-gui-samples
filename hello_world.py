import tkinter as tk

# ttk - new set of controls that are themeable; make app look more native
from tkinter import ttk

# create main window
root = tk.Tk()

# add element to the window
#   - pass parent into the constructor, where the control will be placed
#   - .pack(), use the Pack manager to put the label into the container
#   - padding(horizontal padding, vertical padding)
ttk.Label(root, text="Hello, World!", padding=(30, 80)).pack()

# pause Python code here, while event loop takes over
root.mainloop()