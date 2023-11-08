from pathlib import Path
import subprocess
from tkinter import *
import os

OUTPUT_PATH = Path(os.path.dirname(__file__))
ASSETS_PATH = OUTPUT_PATH / Path("assets/payments")

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
def go_to_sberpay():
    window.destroy()
    subprocess.Popen(['python', 'sberpay.py'])
def go_to_own():
    window.destroy()
    subprocess.Popen(['python', 'own.py'])


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
    104.0,
    image=image_image_1
)

canvas.create_text(
    20.0,
    117.0,
    anchor="nw",
    text="Переводы стали еще удобнее",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 12 * -1)
)

canvas.create_rectangle(
    0.0,
    577.0,
    300.0,
    617.0,
    fill="#1E1E1E",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_home(),
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
button_2 = Label(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
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
    command=lambda: print("button_3 clicked"),
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
    630.126953125,
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
image_6 = canvas.create_image(
    149.0,
    401.5,
    image=image_image_6
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_sberpay(),
    relief="flat"
)
button_6.place(
    x=40.0,
    y=308.0,
    width=170.833251953125,
    height=26.573974609375
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_own(),
    relief="flat"
)
button_7.place(
    x=35.0,
    y=425.0,
    width=171.0,
    height=26.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_sberpay(),
    relief="flat"
)
button_8.place(
    x=40.0,
    y=368.0,
    width=170.833251953125,
    height=23.245849609375
)

canvas.create_text(
    20.0,
    85.0,
    anchor="nw",
    text="Перевести",
    fill="#FFFFFF",
    font=("OpenSansRoman Bold", 19 * -1)
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    bg = "#000000",
    activebackground="#000000",
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=24.0,
    y=153.0,
    width=85.55126953125,
    height=85.55126953125
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    bg = "#000000",
    activebackground="#000000",
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=123.0,
    y=151.0,
    width=85.55126953125,
    height=85.55126953125
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_sberpay(),
    relief="flat"
)
button_11.place(
    x=35.0,
    y=479.0,
    width=117.652587890625,
    height=26.8701171875
)
window.resizable(False, False)
window.mainloop()
