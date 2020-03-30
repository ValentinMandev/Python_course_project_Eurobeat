import tkinter as tk
import search_for_song
import webbrowser
import os
import datetime as dt
import time


class Element:
    def __init__(self, name, text, width, height, bg, fg, font, x, y):
        self.name = name
        self.text = text
        self.width = width
        self.height = height
        self.bg = bg
        self.fg = fg
        self.font = font
        self.x = x
        self.y = y

    def label(self, wraplength, anchor):
        name = tk.Label(
            text=f"{self.text}",
            width=self.width,
            height=self.height,
            bg=f"{self.bg}",
            fg=f"{self.fg}",
            font=f"{self.font}",
            wraplength=wraplength,
            anchor=f'{anchor}'
        )
        name.pack()
        name.place(x=self.x, y=self.y)

    def button(self, func):
        name = tk.Button(
            text=self.text,
            width=self.width,
            height=self.height,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
        )
        name.place(x=self.x, y=self.y)
        name.bind('<Button-1>', func)


# дата и час
def date_and_time():
    def clock_update():
        time1 = time.strftime('%H:%M:%S')
        clock.config(text=time1)
        clock.after(200, clock_update)

    def date_update():
        date1 = f'{dt.datetime.now():%d %b %Y (%a)}'
        date.config(text=date1)
        date.after(1000, date_update)

    date = tk.Label(fg="black", bg="chartreuse3", font=("Verdana 7 bold"))
    clock = tk.Label(fg="black", bg="chartreuse3", font=("Verdana 7 bold"))
    date.place(x=10, y=25)
    clock.place(x=10, y=10)
    clock_update()
    date_update()

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

    def select_random_song(_):
        rand0 = search_for_song.random_items()[3]
        random0 = Element('random0',
                         f"Random song: {rand0}",
                         80, 2,
                         "red", "midnight blue", "Verdana 12 bold italic",
                         65, 320)
        random0.button(select_random_song)
        find_songs(rand0)

    def select_random_artist(_):
        rand1 = search_for_song.random_items()[0]
        random1 = Element('random1',
                         f"Random artist: {rand1}",
                         80, 2,
                         "red", "midnight blue", "Verdana 12 bold italic",
                         65, 400)
        random1.button(select_random_artist)
        find_songs(rand1)

    def select_random_year(_):
        rand2 = search_for_song.random_items()[1]
        random2 = Element('random2',
                         f"Random year: {rand2}",
                         80, 2,
                         "red", "midnight blue", "Verdana 12 bold italic",
                         65, 480)
        random2.button(select_random_year)
        find_songs(rand2)

    def select_random_label(_):
        rand3 = search_for_song.random_items()[2]
        random3 = Element('random3',
                         f"Random label: {rand3}",
                         80, 2,
                         "red", "midnight blue", "Verdana 12 bold italic",
                         65, 560)
        random3.button(select_random_label)
        find_songs(rand3)

    def upddb(_):
        os.system('python update_songs_database.py')
        updms = tk.Message(window1,
            text='Database updated successfully. Please restart the application, so changes could take effect and you have the most up-to-date eurobeat information. :)',
            font='verdana 13 bold')
        updms.pack()
        updms.place(x=400, y=300)

    def close():
        exit()

    window1 = tk.Tk()
    window1.winfo_toplevel().title('Eurobeat song guide')
    window1.geometry('1024x768')
    window1.resizable(False, False)

    # Логото на програмата:
    label1 = Element('label1',
                     'EURO',
                     10, 2,
                     "chartreuse3", "midnight blue", "Verdana 45 bold italic",
                     90, 1)
    label1.label(300, "e")

    label2 = Element('label2',
                     'BEAT',
                     10, 2,
                     "chartreuse3", "red", "Verdana 45 bold italic",
                     513, 1)
    label2.label(300, "w")

    label3 = Element('label3',
                     'song guide',
                     20, 1,
                     "chartreuse3", "midnight blue", "Verdana 24 bold italic",
                     480, 105)
    label3.label(300, "w")

    # Текста над полето за търсене
    search_label = Element('search_label',
                      'Search for a song, artist, year or label',
                      40, 1,
                      "chartreuse3", "black", "Verdana 10 bold",
                      320, 175)
    search_label.label(300, "c")

    # Поле за търсене:
    entry = tk.Entry(fg="black", bg="white", width=50)
    entry.place(x=325, y=210)
    entry.bind('<Return>', search)

    # бутон 'Search'
    search = Element('search',
                      "Search",
                      6, 1,
                      "dodger blue", "black", "Verdana 8 bold italic",
                      635, 207)
    search.button(click)

    # бутона за ъпдейт на базата данни
    update = Element('update',
                      "Update database",
                      14, 4,
                      "LemonChiffon2", "black", "Verdana 12 bold italic",
                      85, 660)
    update.button(upddb)

    # текста с информация относно ъпдейта
    updinfo = Element('updinfo',
                      "<= Database update takes about 2-3 minutes, so please be patient. You don't need to do it too often.",
                      65, 4,
                      "chartreuse3", "black", "Verdana 13 bold underline",
                      250, 660)
    updinfo.label(600, "c")

    # контакти
    contacts = Element('contacts',
                      "Contacts:\nValentin Mandev\nemail: valentin.vkm@gmail.com\nNet IT course project",
                      30, 4,
                      "chartreuse3", "black", "Verdana 10 bold",
                      740, 50)
    contacts.label(300, "c")

    # random
    random_song = Element('random_song',
                      "Random song",
                      80, 2,
                      "midnight blue", "red", "Verdana 12 bold italic",
                      65, 320)
    random_song.button(select_random_song)

    random_artist = Element('random_artist',
                      "Random artist",
                      80, 2,
                      "midnight blue", "red", "Verdana 12 bold italic",
                      65, 400)
    random_artist.button(select_random_artist)

    random_year = Element('random_year',
                      "Random year",
                      80, 2,
                      "midnight blue", "red", "Verdana 12 bold italic",
                      65, 480)
    random_year.button(select_random_year)

    random_label = Element('random_label',
                      "Random label",
                      80, 2,
                      "midnight blue", "red", "Verdana 12 bold italic",
                      65, 560)
    random_label.button(select_random_label)

    # Дата и час:
    date_and_time()

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
    label1 = Element('label1',
                      'EURO',
                      8, 2,
                      "chartreuse3", "midnight blue", "Verdana 45 bold italic",
                      10, 1)
    label1.label(300, "e")

    label2 = Element('label2',
                      'BEAT',
                      8, 2,
                      "chartreuse3", "red", "Verdana 45 bold italic",
                      353, 1)
    label2.label(300, "w")

    label3 = Element('label3',
                      'song guide',
                      20, 1,
                      "chartreuse3", "midnight blue", "Verdana 24 bold italic",
                      320, 108)
    label3.label(300, "w")

    # бутон за връщане към основния екран
    back_button = Element('back_button',
                      "Back to search screen",
                      32, 2,
                      "LemonChiffon2", "black", "Verdana 14 bold italic",
                      125, 650)
    back_button.button(back)

    song_info = search_for_song.print_song_info()

    song_name = str(song_info[0])
    song_year = str(song_info[1])
    song_label = str(song_info[2])
    song_producer = str(song_info[3])
    song_writer = str(song_info[4])
    song_link = str(song_info[5])
    song_duration_m = str(song_info[6].split(':')[2]) if song_info[6] != 'Song duration: Unknown' else ''
    song_duration_s = str(song_info[6].split(':')[3]) if song_info[6] != 'Song duration: Unknown' else ''
    song_duration = 'Song duration: ' + song_duration_m + ':' + song_duration_s if song_info[6] != 'Song duration: Unknown' else 'Song duration: Unknown'
    song_lyrics = str(song_info[7])

    sname = Element('sname',
                      song_name,
                      40, 2,
                      "chartreuse3", "black", "Verdana 13 bold underline",
                      100, 160)
    sname.label(400, "c")

    syear = Element('syear',
                      song_year,
                      20, 2,
                      "chartreuse3", "black", "Verdana 10 bold",
                      250, 225)
    syear.label(300, "c")

    slabel = Element('slabel',
                      song_label,
                      30, 2,
                      "chartreuse3", "black", "Verdana 10 bold",
                      200, 280)
    slabel.label(300, "c")

    sproducer = Element('sproducer',
                      song_producer,
                      40, 2,
                      "chartreuse3", "black", "Verdana 10 bold",
                      160, 335)
    sproducer.label(300, "c")

    swriter = Element('swriter',
                      song_writer,
                      40, 2,
                      "chartreuse3", "black", "Verdana 10 bold",
                      160, 390)
    swriter.label(300, "c")

    sduration = Element('sduration',
                      song_duration,
                      40, 2,
                      "chartreuse3", "black", "Verdana 10 bold",
                      160, 445)
    sduration.label(300, "c")

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

    slyrics = Element('slyrics',
                      song_lyrics,
                      50, 70,
                      "chartreuse3", "black", "Verdana 8 italic",
                      640, 20)
    slyrics.label(300, "n")

    # Дата и час:
    date_and_time()

    window2.configure(background='chartreuse3')
    window2.mainloop()
    exit()


window1()

