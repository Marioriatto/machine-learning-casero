from perceptron import *
from tkinter import *

root = Tk()
root.title('Machine Learning Casero')
root.minsize(600, 600)
root.resizable(width=NO, height=NO)

perceptron = Perceptron(root, generate_separable_data(67))

root.mainloop()