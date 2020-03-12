# https://realpython.com/python-gui-tkinter/
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://www.geeksforgeeks.org/python-gui-tkinter/

import tkinter as tk


def search(entry):
	print(entry.widget.get())

def click(_):
	print('Click')

# създавам прозорец
window = tk.Tk()


# някакъв лейбъл
label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
label.pack()


# бутон
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()
button.bind('<Button-1>', click)


entry = tk.Entry(fg="yellow", bg="green", width=50)
# Retrieving text with .get()
# Deleting text with .delete()
# Inserting text with .insert()
entry.pack()






window.mainloop()


