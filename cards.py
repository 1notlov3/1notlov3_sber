from pathlib import Path
import subprocess
from tkinter import *
import os
from customtkinter import *
import sys
import pyodbc
with open('login.txt', 'r') as f:
    clean_log = str(f.read())
print(clean_log)
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Sber\Бд.accdb')
cursor = conn.cursor()
cursor.execute(f"SELECT Балланс_карты FROM Балланс WHERE Логин = '{clean_log}'")
result = cursor.fetchall()
for row in result:
    clean_bal0 = [str(item).strip() for item in row]
clean_bal="".join(clean_bal0)
OUTPUT_PATH = Path(os.path.dirname(__file__))
ASSETS_PATH = OUTPUT_PATH / Path("assets/cards")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def go_to_home():
    window.destroy()
    subprocess.Popen(['python', 'home.py'])
def go_to_history():
    window.destroy()
    subprocess.Popen(['python', 'history.py'])
def go_to_payments():
    window.destroy()
    subprocess.Popen(['python', 'payments.py'])
def go_to_sberpay():
    window.destroy()
    subprocess.Popen(['python', 'sberpay.py'])

window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("sber")
window.iconbitmap("sber.ico")
# Устанавливаем положение главного окна по центру экрана
window.geometry(f"300x645+{int((screen_width-300)/2)}+{int((screen_height-645)/2)}")
window.configure(bg = "#121212")


canvas = Canvas(
    window,
    bg = "#121212",
    height = 645,
    width = 300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg = "#121212",
    activebackground= "#121212",
    command=lambda: go_to_payments(),
    relief="flat"
)
button_1.place(
    x=9.0,
    y=281.0,
    width=146.42483520507812,
    height=99.65034484863281
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    bg = "#121212",
    activebackground= "#121212",
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=162.14697265625,
    y=281.0,
    width=128.84068298339844,
    height=99.65034484863281
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    bg = "#121212",
    activebackground= "#121212",
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=9.0,
    y=386.944091796875,
    width=146.85296630859375,
    height=44.055938720703125
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    bg = "#121212",
    activebackground= "#121212",
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=162.14697265625,
    y=386.944091796875,
    width=128.16258239746094,
    height=44.055938720703125
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    150.0,
    631.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    148.0,
    17.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    150.0,
    131.0,
    image=image_image_3
)

bal = Label(

    anchor="nw",
    text=clean_bal,
    font=("OpenSansRoman SemiBold", 21 * -1),
    bg="#121212",
    fg="white"
)
bal.pack(pady=220)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    bg = "#121212",
    activebackground= "#121212",
    command=lambda: go_to_history(),
    relief="flat"
)
button_5.place(
    x=13.0,
    y=454.0,
    width=274.0,
    height=30.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    bg = "#121212",
    activebackground= "#121212",
    command=lambda: go_to_home(),
    relief="flat"
)
button_6.place(
    x=13.0,
    y=35.0,
    width=19.20001220703125,
    height=19.20001220703125
)
window.resizable(False, False)
window.mainloop()
