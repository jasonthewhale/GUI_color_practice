"""
Simple GUI programming exercise to demonstrate component layout
and event handling.
"""

__copyright__ = "Copyright 2018, University of Queensland"


from curses import COLOR_BLUE
import tkinter as tk
from tkinter import messagebox


class SampleApp(object) :
    def __init__(self, master) :
        self._master = master
        master.title("Hello!")
        master.minsize(430, 200)

        self._lbl = tk.Label(master, text="Choose a button")
        self._lbl.pack(side=tk.TOP, expand=tk.TRUE)

        btn_frame = tk.Frame(master)
        btn_frame.pack(side=tk.TOP)

        colour_frame = tk.Frame(master)
        colour_frame.pack(side=tk.TOP, pady=10, fill=tk.X)

        blue_btn = tk.Button(btn_frame, text="Change to Blue!", 
        command=self.turn_blue)
        blue_btn.pack(side=tk.LEFT)

        green_btn = tk.Button(btn_frame, text="Change to Green!", 
        command=self.turn_green)
        green_btn.pack(side=tk.LEFT)

        part_1 = tk.Label(colour_frame, text="Change thecolour to: ")
        part_1.pack(side=tk.LEFT)

        self.part_2 = tk.Entry(colour_frame)
        self.part_2.pack(side=tk.LEFT, fill=tk.X, expand=1)

        part_3 = tk.Button(colour_frame, text="Change it!", command=self.change_colour)
        part_3.pack(side=tk.LEFT)

    def say_hello(self) :
        print('Hello! Thanks for clicking!')

    def turn_blue(self):
        self._lbl.config(text="The label is blue",
        bg="Blue")
    
    def fetch_colour(self):
        colour = self._entry_filed.get()

        self._lbl.config(bg=colour,
        text=f"The lable is{colour}")

    def turn_green(self):
        self._lbl.config(text="The label is green",
        bg="Green")

    def change_colour(self):
        colour = self.part_2.get()
        try:
            self._lbl.config(text=f"The label is {colour}",
            bg=colour)
        except tk.TclError:
            messagebox.showerror("Invalid Colour", f"{colour} is not a colour!")



if __name__ == "__main__" :
    root = tk.Tk()
    app = SampleApp(root)
    root.mainloop()
