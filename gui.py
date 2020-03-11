# https://realpython.com/python-gui-tkinter/
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://www.geeksforgeeks.org/python-gui-tkinter/

import tkinter as tk

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

entry = tk.Entry(fg="yellow", bg="green", width=50)
# Retrieving text with .get()
# Deleting text with .delete()
# Inserting text with .insert()
entry.pack()

entry.bind('<Return>', search_field = entry.get())

window.mainloop()



# import tkinter as tk
#
#
# def on_change(e):
#     print(e.widget.get())
#
# root = tk.Tk()
#
# e = tk.Entry(root)
# e.pack()
# # Calling on_change when you press the return key
# e.bind("<Return>", on_change)
#
# root.mainloop()