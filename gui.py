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
import webbrowser


def search(entry):
    search_field = entry.widget.get()
    print(search_field)

def click(_):
    print('Click')

def url():
    url=webbrowser.open_new("www.pythonlake.com")

# създавам прозорец
window = tk.Tk()
window.geometry('1024x768')


# някакъв лейбъл
label1 = tk.Label(
    text="EURO",
    fg="midnight blue",
    bg="yellow",
    width=10,
    height=2,
	font = 'Verdana 45 bold italic',
    anchor = 'e'
)


label2 = tk.Label(
    text="BEAT",
    fg="red",
    bg="yellow",
    width=10,
    height=2,
	font = 'Verdana 45 bold italic',
    anchor = 'w'
)

search_label = tk.Label(
    text="Search for a song, artist, year or label",
    fg="black",
    bg="yellow",
    width=40,
    height=1,
	font = 'Verdana 10 bold',
    anchor = 'c'
)

label2.place(x=513, y=1)
label1.place(x=90, y=1)
search_label.place(x=318, y=140)

# # бутон
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# button.pack()
# button.bind('<Button-1>', click)
#
# button=tk.Button(window, text="pythonlake.com", command=url)
# button.pack()
#
entry = tk.Entry(fg="black", bg="lawn green", width=50, text='Search for a song, artist, year or label')
# Retrieving text with .get()
# Deleting text with .delete()
# Inserting text with .insert()
entry.place(x=350, y=170)
entry.bind('<Return>', search)

window.configure(background='yellow')
window.mainloop()
