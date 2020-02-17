import tkinter as tk
import threading
from python.python.testpython.thread.threadAndGui.test1_stopFreezingGui.backEndProcess import Arithmatic
class test(tk.Tk):
    def __init__(self):
        super().__init__()
        self.result_var = tk.StringVar()
        self.input_var = tk.IntVar()
        self.geometry("500x500")
        self.backEndProcess = Arithmatic()
        self.thread1 = None
        input_label = tk.Label(self, text="Input the number: ")
        input_label.grid(row=0, column=0)
        input_entry = tk.Entry(self, textvariable=self.input_var)
        input_entry.grid(row=0, column=1, columnspan=3, sticky="WE")
        result_label = tk.Label(self, text="result: ")
        result_label.grid(row=1, column=0)
        result_entry = tk.Entry(self, textvariable=self.result_var, state="readonly", width=50)
        result_entry.grid(row=1, column=1, columnspan=5, sticky="WE")
        process_sumButton = tk.Button(self, text="SUM PRESS", command=self.summing)
        process_sumButton.grid(row=2, column=0, columnspan=3, sticky="WE")
        process_mulButton = tk.Button(self, text='MUL PRESS', command=self.multiplying)
        process_mulButton.grid(row=3, column=0, columnspan=3, sticky="WE")

    def summing(self):
        self.thread1 = threading.Thread(target=self.backEndProcess.summing,
                                        args=(self.input_var.get(),), daemon=True)
        self.thread1.start()
        self.showResult()

    def multiplying(self):
        self.thread1 = threading.Thread(target=self.backEndProcess.multi,
                                        args=(self.input_var.get(),), daemon=True)
        self.thread1.start()
        self.showResult()

    def showResult(self):
        if self.thread1.is_alive():
            print("*")
            self.after(1000, self.showResult)
        else:
            print("result")
            self.result_var.set(self.backEndProcess._total)
            self.thread1 = None


if __name__ == "__main__":
    test = test()
    test.mainloop()

