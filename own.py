from pathlib import Path
import subprocess
from tkinter import *
import os
from customtkinter import *


OUTPUT_PATH = Path(os.path.dirname(__file__))
ASSETS_PATH = OUTPUT_PATH / Path("assets/own")

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
    subprocess.Popen(['python', 'cards.py'])
def open_count():
    window.destroy()
    subprocess.Popen(['python', 'count.py'])
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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    150.0,
    17.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    33.0,
    300.0,
    63.0,
    fill="#1E1E1E",
    outline="")

canvas.create_text(
    80.0,
    38.0,
    anchor="nw",
    text="Между своими счетами",
    fill="#FFFFFF",
    font=("Arial BoldMT", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg="#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_payments(),
    relief="flat"
)
button_1.place(
    x=8.0,
    y=38.0,
    width=19.20001220703125,
    height=19.200000762939453
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    258.0,
    124.0,
    image=image_image_2
)

canvas.create_text(
    18.0,
    74.0,
    anchor="nw",
    text="Откуда",
    fill="#575757",
    font=("OpenSansRoman SemiBold", 9 * -1)
)

canvas.create_text(
    20.0,
    205.0,
    anchor="nw",
    text="Куда",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 9 * -1)
)

canvas.create_text(
    247.0,
    96.0,
    anchor="nw",
    text="0 ₽",
    fill="#428D39",
    font=("OpenSansRoman SemiBold", 12 * -1)
)

canvas.create_text(
    247.0,
    221.0,
    anchor="nw",
    text="0 ₽",
    fill="#428D39",
    font=("OpenSansRoman SemiBold", 12 * -1)
)

canvas.create_text(
    19.0,
    121.0,
    anchor="nw",
    text="●●●● ",
    fill="#575757",
    font=("Roboto Regular", 6 * -1)
)

canvas.create_text(
    35.25,
    122.25,
    anchor="nw",
    text="0000",
    fill="#575757",
    font=("OpenSansRoman SemiBold", 6 * -1)
)

canvas.create_text(
    21.0,
    248.0,
    anchor="nw",
    text="●●●● ",
    fill="#575757",
    font=("Roboto Regular", 6 * -1)
)

canvas.create_text(
    37.25,
    249.25,
    anchor="nw",
    text="0000",
    fill="#575757",
    font=("OpenSansRoman SemiBold", 6 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    150.0,
    176.0,
    image=image_image_3
)

canvas.create_text(
    18.0,
    94.0,
    anchor="nw",
    text="Карта",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 9 * -1)
)

canvas.create_text(
    21.0,
    223.0,
    anchor="nw",
    text="Накопительный счет",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 9 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    256.0,
    250.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    150.0,
    296.0,
    image=image_image_5
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    43.0,
    307.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#121212",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=11.0,
    y=298.0,
    width=64.0,
    height=16.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    150.0,
    631.0,
    image=image_image_6
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    bg="#121212",
    activebackground="#121212",
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=13.0,
    y=579.0,
    width=274.0,
    height=30.0
)
window.resizable(False, False)
window.mainloop()
