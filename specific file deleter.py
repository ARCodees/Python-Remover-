import os
import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget

def Delete():
	inp = inputtxt.get(1.0, "end-1c")
	lbl.config(text = "Provided Input: "+inp)
    cwd = os.getcwd()
    lst = os.listdir(cwd)
    for i in lst:
        if i.endswith(inp):
            os.remove(os.path.join(cwd,i))
            
inputtxt = tk.Text(frame,
				height = 5,
				width = 20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
						text = "Delete",
						command = Delete)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()


cwd = os.getcwd()
lst = os.listdir(cwd)

a = input("Enter the extention you want to delete with .")
for i in lst:
    if i.endswith(a):
        os.remove(os.path.join(cwd,i))

