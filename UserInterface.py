import tkinter as tk
import numpy as np

class Interface:
    def __init__(self, master):
        self.master = master
        master.title("Counting Colorings")

        self.label = tk.Label(master, text="GUI!").pack()

        self.addVertex_button = tk.Button(master, text="Add Row", command=master.quit).pack()
        self.deleteVertex_button = tk.Button(master, text="Add Row", command=master.quit).pack()

        self.entryWidgets = tk.Checkbutton(master,text="SAMPLE").pack()

root = tk.Tk()
my_gui = Interface(root)
root.mainloop()