import tkinter as tk
from ttkbootstrap import ttk
import numpy as np

## COLORS ##

USA_BLUE = '#00205B'
USA_RED =  '#BF0D3E'
WHITE =    '#FFFFFF'



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main Setup
        self.title("Counting Colorings")
        self.geometry("600x600")
        self.minsize(600,600)
        self.resizable(True, True)

        # Widgets
        self.topBar = TopBar(self)
        self.vertex = VertexSection(self)

        self.mainloop()

class TopBar(ttk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            
            self.grid(row=0, column=0, sticky='NEW', columnspan=4)
            self.columnconfigure(1, weight=1)
            self.columnconfigure(2, weight=2)

            ttk.Button(self, text= "Add Vertex").grid(row=0, column=0, sticky='WE')
            ttk.Button(self, text= "Delete Vertex").grid(row=0, column=1, sticky='WE')

class VertexSection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(anchor='n')

app = App()