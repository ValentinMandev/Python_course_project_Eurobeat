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
import webbrowser
import os


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
        song_list.place(x=325, y=250)
        var.set('Please select the song you are looking for from the list below:')


    def search(entry):
        search_field = entry.widget.get()
        find_songs(search_field)


    def click(_):
        search_field = entry.get()
        find_songs(search_field)


    def upddb(_):

        os.system('update_songs_database.py')
        updms = tk.Message(window,
            text='Database updated successfully. Please restart the application, so changes could take effect and you have the most up-to-date eurobeat information. :)',
            font='verdana 13 bold')
        updms.pack()
        updms.place(x=400, y=300)


    def close():
        exit()


    window = tk.Tk()
    window.winfo_toplevel().title('Eurobeat song guide')
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

    label3 = tk.Label(
        text="song guide",
        fg="midnight blue",
        bg="chartreuse3",
        width=20,
        height=1,
        font='Verdana 24 bold italic',
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
    label3.place(x=480, y=105)

    search_label.place(x=320, y=175)

    #
    entry = tk.Entry(fg="black", bg="white", width=50, text='Search for a song, artist, year or label')
    entry.place(x=325, y=210)
    entry.bind('<Return>', search)

    # бутон
    search = tk.Button(
        text="Search",
        width=6,
        height=1,
        bg="dodger blue",
        fg="black",
        font='Verdana 8 bold italic',
    )
    search.place(x=635, y=207)
    search.bind('<Button-1>', click)


    # бутон
    update = tk.Button(
        text="Update database",
        width=14,
        height=4,
        bg="LemonChiffon2",
        fg="black",
        font='Verdana 12 bold italic',
    )
    update.place(x=85, y=660)
    update.bind('<Button-1>', upddb)


    updinfo = tk.Label(
        text="<= Database update takes about 2-3 minutes, so please be patient - it's worth it. You don't need to do it too often.",
        width= 65,
        height = 4,
        bg="chartreuse3",
        fg="black",
        font="Verdana 13 bold underline",
        wraplength=600,
        anchor='c'
    )
    updinfo.pack()
    updinfo.place(x=250, y=660)


    contacts = tk.Label(
        text="Contacts:\nValentin Mandev\nemail: valentin.vkm@gmail.com\nNet IT project",
        width= 30,
        height = 4,
        bg="chartreuse3",
        fg="black",
        font="Verdana 10 bold",
        anchor='c'
    )
    contacts.pack()
    contacts.place(x=740, y=50)

    window.configure(background='chartreuse3')

    window.protocol("WM_DELETE_WINDOW", close)
    window.mainloop()
    window2()


def window2():

    def back(_):
        window2.destroy()
        window1()

    def youtube(url):
        webbrowser.open_new(url)

    window2 = tk.Tk()
    window2.winfo_toplevel().title('Eurobeat program')
    window2.geometry('1024x768')
    window2.resizable(False, False)


    # някакъв лейбъл
    label1 = tk.Label(
        text="EURO",
        fg="midnight blue",
        bg="chartreuse3",
        width=8,
        height=2,
        font='Verdana 45 bold italic',
        anchor='e'
    )


    label2 = tk.Label(
        text="BEAT",
        fg="red",
        bg="chartreuse3",
        width=8,
        height=2,
        font='Verdana 45 bold italic',
        anchor='w'
    )


    label3 = tk.Label(
        text="song guide",
        fg="midnight blue",
        bg="chartreuse3",
        width=20,
        height=1,
        font='Verdana 24 bold italic',
        anchor='w'
    )


    label2.place(x=353, y=1)
    label1.place(x=10, y=1)
    label3.place(x=320, y=108)




    # бутон
    button = tk.Button(
        text="Back to search screen",
        width=32,
        height=2,
        bg="LemonChiffon2",
        fg="black",
        font='Verdana 14 bold italic',
    )
    button.place(x=125, y=650)
    button.bind('<Button-1>', back)

    song_info = search_for_song.print_song_info()


    song_name = str(song_info[0])
    song_year = str(song_info[1])
    song_label = str(song_info[2])
    song_producer = str(song_info[3])
    song_writer = str(song_info[4])
    song_link = str(song_info[5])
    song_duration_m = str(song_info[6].split(':')[2]) if song_info[6] != 'Song duration: Unknown' else ''
    song_duration_s = str(song_info[6].split(':')[3]) if song_info[6] != 'Song duration: Unknown' else ''
    song_lyrics = str(song_info[7])
    # youtube_logo = tk.PhotoImage(file = 'youtube_logo.png')
    # yphoto = tk.Label(window2, compound = tk.CENTER, image = youtube_logo, bg = 'chartreuse3')
    # yphoto.pack()
    # yphoto.place(x=400, y=400)

    sname = tk.Label(
        text=song_name,
        width= 40,
        height = 2,
        bg="chartreuse3",
        fg="black",
        font="Verdana 13 bold underline",
        wraplength=400,
        anchor='c'
    )
    sname.pack()
    sname.place(x=100, y=160)

    syear = tk.Label(
        text=song_year,
        width= 20,
        height = 2,
        bg="chartreuse3",
        fg="black",
        font="Verdana 10 bold",
        anchor='c'
    )
    syear.pack()
    syear.place(x=250, y=225)


    slabel = tk.Label(
        text=song_label,
        width= 30,
        height = 2,
        bg="chartreuse3",
        fg="black",
        font="Verdana 10 bold",
        anchor='c'
    )
    slabel.pack()
    slabel.place(x=200, y=280)


    sproducer = tk.Label(
        text=song_producer,
        width= 40,
        height = 2,
        bg="chartreuse3",
        fg="black",
        font="Verdana 10 bold",
        anchor='c'
    )
    sproducer.pack()
    sproducer.place(x=160, y=335)


    swriter = tk.Label(
        text=song_writer,
        width= 40,
        height = 2,
        bg="chartreuse3",
        fg="black",
        font="Verdana 10 bold",
        anchor='c'
    )
    swriter.pack()
    swriter.place(x=160, y=390)


    sduration = tk.Label(
        text='Song duration: ' + song_duration_m + ':' + song_duration_s if song_info[6] != 'Song duration: Unknown' else 'Song duration: Unknown',
        width= 40,
        height = 2,
        bg="chartreuse3",
        fg="black",
        font="Verdana 10 bold",
        anchor='c'
    )
    sduration.pack()
    sduration.place(x=160, y=445)

    slink = tk.Label(
        text='YouTube search link',
        width= 20,
        height = 4,
        bg="chartreuse3",
        fg="blue",
        font="Verdana 12 bold",
        anchor='c',
        cursor="hand2"
    )
    slink.pack()
    slink.place(x=228, y=500)
    slink.bind("<Button-1>", lambda e: youtube(song_link))

    slyrics = tk.Label(
        text=song_lyrics,
        width= 50,
        height = 70,
        bg="chartreuse3",
        fg="black",
        font="Verdana 8 italic",
        anchor='n'
    )
    slyrics.pack()
    slyrics.place(x=640, y=20)

    window2.configure(background='chartreuse3')
    window2.mainloop()
    exit()

window1()

