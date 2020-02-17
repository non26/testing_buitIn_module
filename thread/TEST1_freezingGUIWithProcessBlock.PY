import tkinter as tk
from tkinter import messagebox
import time
class BackendProcess:
    def __init__(self):
        self.finished = False
    def run(self):
        time.sleep(10)
        self.finished = True
class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.process = BackendProcess()
        tk.Button(self, text='Run', command=self.run).pack()
    def run(self):
        self.process.run()
        messagebox.showinfo('Info', 'Process completed!')
if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
