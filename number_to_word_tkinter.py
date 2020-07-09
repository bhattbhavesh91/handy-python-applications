import tkinter as tk
import num2words as n2w
from functools import partial

def call_result(label_result, n1):
    num1 = (n1.get())
    result = n2w.num2words(int(num1), lang="en_IN")
    label_result.config(text="Result is {}".format(result))
    return

root = tk.Tk()
root.geometry('600x300')
root.title('Number to Word Calculator')
number1 = tk.StringVar()
labelTitle = tk.Label(root, text="Simple Calculator").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Enter a number").grid(row=1, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
call_result = partial(call_result, labelResult, number1)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)
root.mainloop()