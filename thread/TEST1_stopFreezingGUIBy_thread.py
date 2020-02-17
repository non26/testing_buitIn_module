import tkinter as tk
from tkinter import messagebox
import time
import threading
class BackendProcess:
    def __init__(self):
        print(2)
        self.finished = False

    def task(self):
        print(5)
        time.sleep(2)
        print(8)
        print('finished')
        self.finished = True

    def run(self):
        print(4)
        thread = threading.Thread(target=self.task, daemon=True)
        thread.start()

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        print(1)
        self.process = BackendProcess()
        tk.Button(self, text='Run', command=self.run).pack()

    def run(self):
        print(3)
        self.process.run()
        print(6)
        self.check_process()

    def check_process(self):
        """ Check every 1000 ms whether the process is finished """
        print(7)
        if self.process.finished:
            messagebox.showinfo('Info', 'Process completed')
        else:
            self.after(1000, self.check_process)


if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()