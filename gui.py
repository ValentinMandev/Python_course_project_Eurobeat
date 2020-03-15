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
import search_for_song


def find_songs(entry):
    search_field = entry

    def callback(selection):
        a = selection
        song_list.destroy()
        print(a)

    var = tk.StringVar()
    song_list = tk.OptionMenu(window, var, *search_for_song.show_info(search_field), command=callback)
    song_list.pack()
    song_list.place(x=325, y=220)
    var.set('Please select the song you are looking for from the list below:')



def search(entry):
    search_field = entry.widget.get()
    find_songs(search_field)



def click(_):
    search_field = entry.get()
    find_songs(search_field)



# създавам прозорец
window = tk.Tk()
window.winfo_toplevel().title('Eurobeat program')
window.geometry('1024x768')
window.resizable(False, False)


# някакъв лейбъл
label1 = tk.Label(
    text="EURO",
    fg="midnight blue",
    bg="chartreuse3",
    width=10,
    height=2,
    font='Verdana 45 bold italic',
    anchor='e'
)


label2 = tk.Label(
    text="BEAT",
    fg="red",
    bg="chartreuse3",
    width=10,
    height=2,
    font='Verdana 45 bold italic',
    anchor='w'
)

search_label = tk.Label(
    text="Search for a song, artist, year or label",
    fg="black",
    bg="chartreuse3",
    width=40,
    height=1,
    font='Verdana 10 bold',
    anchor='c'
)



label2.place(x=513, y=1)
label1.place(x=90, y=1)
search_label.place(x=320, y=135)


#
entry = tk.Entry(fg="black", bg="white", width=50, text='Search for a song, artist, year or label')
entry.place(x=325, y=170)
entry.bind('<Return>', search)


# бутон
button = tk.Button(
    text="Search",
    width=6,
    height=1,
    bg="dodger blue",
    fg="black",
    font='Verdana 8 bold italic',
)
button.place(x=635, y=167)
button.bind('<Button-1>', click)




window.configure(background='chartreuse3')

window.mainloop()
