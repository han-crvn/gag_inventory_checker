# main.py

import tkinter as tk
from front_end import MainApp

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()