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
import os, sys

def window1():
    def find_songs(entry):
        search_field = entry

        def choose(_):
            with open('chosen_song.txt', 'w') as songfile:
                print(var.get(), file=songfile)
                window.destroy()

        var = tk.StringVar()

        song_list = tk.OptionMenu(window, var, *search_for_song.show_info(search_field), command=choose)
        song_list.pack()
        song_list.place(x=325, y=220)
        var.set('Please select the song you are looking for from the list below:')


    def search(entry):
        search_field = entry.widget.get()
        find_songs(search_field)


    def click(_):
        search_field = entry.get()
        find_songs(search_field)


    def close():
        exit()

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

    window.protocol("WM_DELETE_WINDOW", close)
    window.mainloop()
    window2()


def window2():

    def back(_):
        window2.destroy()
        window1()

    window2 = tk.Tk()
    window2.winfo_toplevel().title('Eurobeat program')
    window2.geometry('1024x768')
    window2.resizable(False, False)


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

    label2.place(x=513, y=1)
    label1.place(x=90, y=1)


    label2.place(x=513, y=1)
    label1.place(x=90, y=1)


    # бутон
    button = tk.Button(
        text="Back to search screen",
        width=32,
        height=2,
        bg="LemonChiffon2",
        fg="black",
        font='Verdana 14 bold italic',
    )
    button.place(x=300, y=670)
    button.bind('<Button-1>', back)

    song_info = search_for_song.print_song_info()

    print(song_info)

    song_name = str(song_info[0])

    sname = tk.Label(
        text=song_name,
        width= 150,
        height = 2,
        bg="chartreuse3",
        fg="black",
        font="Verdana 13 bold underline",
        anchor='w'
    )
    sname.pack()
    sname.place(x=100, y=120)

    window2.configure(background='chartreuse3')
    window2.mainloop()
    exit()

window1()

