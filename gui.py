# https://realpython.com/python-gui-tkinter/
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://www.geeksforgeeks.org/python-gui-tkinter/
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
# https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python
# https://github.com/CSSE120StartingCode/TkinterPractice/tree/master/more_examples
# http://www.pythonlake.com/tkintertkgeometry
# https://www.python-course.eu/tkinter_layout_management.php
# https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

import tkinter as tk


def search(entry):
	search_field = entry.widget.get()
	print(search_field)

def click(_):
	print('Click')


# създавам прозорец
window = tk.Tk()
window.geometry('1024x768')


# някакъв лейбъл
label1 = tk.Label(
    text="EURO",
    fg="blue",
    bg="yellow",
    width=10,
    height=2,
	font = 'Verdana 40 bold italic'
)

label2 = tk.Label(
    text="BEAT",
    fg="blue",
    bg="yellow",
    width=10,
    height=2,
	font = 'Verdana 40 bold italic'
)


label1.place(x=1, y=1)
label2.place(x=600, y=1)


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
entry.bind('<Return>', search)

window.mainloop()


