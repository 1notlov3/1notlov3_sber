from pathlib import Path
import subprocess
from tkinter import *
import os
from customtkinter import *
import sys
import pyodbc
with open('my_file.txt', 'r') as f:
    telephone = str(f.read())
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Sber\Бд.accdb')
cursor = conn.cursor()
cursor.execute(f"SELECT Логин FROM Пользователи WHERE Телефон = '{telephone}'")
result = cursor.fetchall()
for row in result:
    clean_name = [str(item).strip() for item in row]
clean_log="".join(clean_name)


                
OUTPUT_PATH = Path(os.path.dirname(__file__))
ASSETS_PATH = OUTPUT_PATH / Path("assets/home")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def go_to_home():
    window.destroy()
    subprocess.Popen(['python', 'home.py'])
def go_to_payments():
    window.destroy()
    subprocess.Popen(['python', 'payments.py'])
def go_to_exchange():
    window.destroy()
    subprocess.Popen(['python', 'exchange.py'])
def go_to_history():
    window.destroy()
    subprocess.Popen(['python', 'history.py'])
def open_cards():
    window.destroy()
    with open('login.txt', 'w') as f:
            f.write((clean_log))
    subprocess.Popen(['python', 'cards.py'])
def open_count():
    window.destroy()
    subprocess.Popen(['python', 'count.py'])
    with open('login.txt', 'w') as f:
            f.write((clean_log))
def go_to_sberpay():
    window.destroy()
    subprocess.Popen(['python', 'sberpay.py'])




window = Tk()
window.title("sber")
window.iconbitmap("sber.ico")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Устанавливаем положение главного окна по центру экрана
window.geometry(f"300x645+{int((screen_width-300)/2)}+{int((screen_height-645)/2)}")
window.configure(bg = "#000000")
window.configure(bg = "#000000")

canvas = Canvas(
    window,
    bg = "#000000",
    height = 645,
    width = 300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    150.0,
    119.0,
    image=image_image_1
)



canvas.create_rectangle(
    0.0,
    577.0,
    300.0,
    617.0,
    fill="#1E1E1E",
    outline="")

canvas.create_text(
    12.67431640625,
    83.0,
    anchor="nw",
    text=clean_log+",",
    fill="#FFFFFF",
    font=("OpenSansRoman Bold", 19 * -1)
)

canvas.create_text(
    12.67431640625,
    116.92138671875,
    anchor="nw",
    text="Экосиситема еще ближе",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Label(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    relief="flat"
)
button_1.place(
    x=12.002197265625,
    y=581.0,
    width=39.20703125,
    height=34.603759765625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_payments(),
    relief="flat"
)
button_2.place(
    x=70.41259765625,
    y=581.0,
    width=40.807373046875,
    height=34.603759765625
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    relief="flat"
)
button_3.place(
    x=130.423095703125,
    y=583.720703125,
    width=39.20703125,
    height=33.60595703125
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_exchange(),
    relief="flat"
)
button_4.place(
    x=177.0,
    y=581.0,
    width=54.0,
    height=34.342041015625
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_history(),
    relief="flat"
)
button_5.place(
    x=248.044189453125,
    y=581.0,
    width=39.20703125,
    height=34.603759765625
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    150.0,
    630,
    image=image_image_2
)


image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    30.0,
    48.188232421875,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    154.6444091796875,
    49.099853515625,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#3A4D40",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=62.993408203125,
    y=35.0,
    width=173.302001953125,
    height=26.19970703125
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    275.27734375,
    48.356689453125,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    149.0,
    17.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = Button(
    window,
    bg='#000000',
    activebackground='#000000',
    highlightthickness=0,
    bd=0,
    image=image_image_6,
    command= lambda: open_count(),

)
image_6.place(x=18,y=
    300.0)


image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = Button(
    window,

    
    bg='#000000',
    activebackground='#000000',
    highlightthickness=0,
    bd=0,
    image=image_image_7,
    command=lambda: open_cards()
)
image_7.place(x=18,y=
    170.0)
image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    74.0,
    491.0,
    image=image_image_8
)

canvas.create_text(
    83.0,
    205.0,
    anchor="nw",
    text="2000Р",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 20 * -1)
)

canvas.create_text(
    81.199951171875,
    464.416748046875,
    anchor="nw",
    text="50",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 20 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    216.0,
    491.0,
    image=image_image_9
)
window.resizable(False, False)
window.mainloop()
