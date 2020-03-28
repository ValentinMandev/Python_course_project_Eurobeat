import tkinter as tk
import search_for_song
import webbrowser
import os
import datetime as dt
import time


def window1():
    def find_songs(entry):
        search_field = str(entry)

        def choose(_):
            with open('chosen_song.txt', 'w') as songfile:
                print(var.get(), file=songfile)
                window1.destroy()

        var = tk.StringVar()

        song_list = tk.OptionMenu(window1, var, *search_for_song.show_info(search_field), command=choose)
        song_list.pack()
        song_list.place(x=325, y=255)
        var.set('Please select the song you are looking for from the list below:')


    def search(entry):
        search_field = entry.widget.get()
        find_songs(search_field)


    def click(_):
        search_field = entry.get()
        find_songs(search_field)


    def select_random_artist(_):
        rand1 = search_for_song.random_items()[0]
        update = tk.Button(
            text=f"Random artist: {rand1}",
            width=80,
            height=3,
            bg="red",
            fg="midnight blue",
            font='Verdana 12 bold italic',
        )
        update.place(x=65, y=320)
        update.bind('<Button-1>', select_random_artist)
        find_songs(rand1)


    def select_random_year(_):
        rand2 = search_for_song.random_items()[1]
        update = tk.Button(
            text=f"Random year: {rand2}",
            width=80,
            height=3,
            bg="midnight blue",
            fg="red",
            font='Verdana 12 bold italic',
        )
        update.place(x=65, y=420)
        update.bind('<Button-1>', select_random_year)
        find_songs(rand2)


    def select_random_label(_):
        rand3 = search_for_song.random_items()[2]
        update = tk.Button(
            text=f"Random label: {rand3}",
            width=80,
            height=3,
            bg="red",
            fg="midnight blue",
            font='Verdana 12 bold italic',
        )
        update.place(x=65, y=520)
        update.bind('<Button-1>', select_random_label)
        find_songs(rand3)


    def upddb(_):
        os.system('update_songs_database.py')
        updms = tk.Message(window1,
            text='Database updated successfully. Please restart the application, so changes could take effect and you have the most up-to-date eurobeat information. :)',
            font='verdana 13 bold')
        updms.pack()
        updms.place(x=400, y=300)


    def clock_update():
        time1 = time.strftime('%H:%M:%S')
        clock.config(text=time1)
        clock.after(200, clock_update)


    def date_update():
        date1 = f'{dt.datetime.now():%d %b %Y (%a)}'
        date.config(text=date1)
        date.after(1000, date_update)


    def close():
        exit()


    window1 = tk.Tk()
    window1.winfo_toplevel().title('Eurobeat song guide')
    window1.geometry('1024x768')
    window1.resizable(False, False)

    # Логото на програмата:
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
    label1.place(x=90, y=1)
    label2.place(x=513, y=1)
    label3.place(x=480, y=105)


    # Текста над полето за търсене
    search_label = tk.Label(
        text="Search for a song, artist, year or label",
        fg="black",
        bg="chartreuse3",
        width=40,
        height=1,
        font='Verdana 10 bold',
        anchor='c'
    )
    search_label.place(x=320, y=175)

    # Поле за търсене:
    entry = tk.Entry(fg="black", bg="white", width=50)
    entry.place(x=325, y=210)
    entry.bind('<Return>', search)

    # бутон 'Search'
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


    # бутона за ъпдейт на базата данни
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

    # текста с информация относно ъпдейта
    updinfo = tk.Label(
        text="<= Database update takes about 2-3 minutes, so please be patient. You don't need to do it too often.",
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

    # контакти
    contacts = tk.Label(
        text="Contacts:\nValentin Mandev\nemail: valentin.vkm@gmail.com\nNet IT course project",
        width= 30,
        height = 4,
        bg="chartreuse3",
        fg="black",
        font="Verdana 10 bold",
        anchor='c'
    )
    contacts.pack()
    contacts.place(x=740, y=50)

    # random
    random_artist = tk.Button(
        text=f"Random artist",
        width=80,
        height=3,
        bg="red",
        fg="midnight blue",
        font='Verdana 12 bold italic',
    )
    random_artist.place(x=65, y=320)
    random_artist.bind('<Button-1>', select_random_artist)

    random_year = tk.Button(
        text=f"Random year",
        width=80,
        height=3,
        bg="midnight blue",
        fg="red",
        font='Verdana 12 bold italic',
    )
    random_year.place(x=65, y=420)
    random_year.bind('<Button-1>', select_random_year)

    random_label = tk.Button(
        text=f"Random label",
        width=80,
        height=3,
        bg="red",
        fg="midnight blue",
        font='Verdana 12 bold italic',
    )
    random_label.place(x=65, y=520)
    random_label.bind('<Button-1>', select_random_label)


    # дата и час
    date = tk.Label(window1, fg="black", bg="chartreuse3", font=("Verdana 7 bold"))
    clock = tk.Label(window1, fg="black", bg="chartreuse3", font=("Verdana 7 bold"))
    date.place(x=10, y=25)
    clock.place(x=10, y=10)
    clock_update()
    date_update()

    # Background на екрана
    window1.configure(background='chartreuse3')

    # за затварянето на прозореца
    window1.protocol("WM_DELETE_WINDOW", close)
    window1.mainloop()
    window2()




def window2():

    def back(_):
        window2.destroy()
        window1()

    def youtube(url):
        webbrowser.open_new(url)

    window2 = tk.Tk()
    window2.winfo_toplevel().title('Eurobeat song guide')
    window2.geometry('1024x768')
    window2.resizable(False, False)


    # Логото на програмата:
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

    label1.place(x=10, y=1)
    label2.place(x=353, y=1)
    label3.place(x=320, y=108)




    # бутон за връщане към основния екран
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

