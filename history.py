from pathlib import Path
from tkinter import *
import os
import subprocess

OUTPUT_PATH = Path(os.path.dirname(__file__))
ASSETS_PATH = OUTPUT_PATH / Path("assets/history")

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


window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("sber")
window.iconbitmap("sber.ico")
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

canvas.create_rectangle(
    0.0,
    148.0,
    300.0,
    238.0,
    fill="#000000",
    outline="")

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
    bg = "#000000",
    activebackground= "#000000",
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=12.0,
    y=150.0,
    width=85.55126953125,
    height=85.55126953125
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    bg = "#000000",
    activebackground= "#000000",
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=109.0,
    y=150.0,
    width=85.55126953125,
    height=85.55126953125
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    bg = "#000000",
    activebackground= "#000000",
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=207.0,
    y=150.0,
    width=85.55126953125,
    height=85.55126953125
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    148.0,
    106.0,
    image=image_image_2
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground= "#1E1E1E",
    command=lambda: go_to_home(),
    relief="flat"
)
button_4.place(
    x=12.002197265625,
    y=581.0,
    width=39.206787109375,
    height=34.603759765625
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground= "#1E1E1E",
    command=lambda: go_to_payments(),
    relief="flat"
)
button_5.place(
    x=70.41259765625,
    y=581.0,
    width=40.80712890625,
    height=34.603759765625
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground= "#1E1E1E",
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=130.4228515625,
    y=583.720703125,
    width=39.20703125,
    height=33.60595703125
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground= "#1E1E1E",
    command=lambda: go_to_exchange(),
    relief="flat"
)
button_7.place(
    x=177.0,
    y=581.0,
    width=54.0,
    height=34.342041015625
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Label(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground= "#1E1E1E",
    relief="flat"
)
button_8.place(
    x=248.0439453125,
    y=581.0,
    width=39.20703125,
    height=34.603759765625
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    150.0,
    630,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    30.0,
    48.188232421875,
    image=image_image_4
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    154.644287109375,
    49.099853515625,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#3B4E40",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=62.993408203125,
    y=35.0,
    width=170.3017578125,
    height=26.19970703125
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    275.27734375,
    48.356689453125,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    149.0,
    17.0,
    image=image_image_6
)

canvas.create_rectangle(
    6.0,
    263.0,
    293.0,
    323.0,
    fill="#1E1E1E",
    outline="")

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    22.0,
    291.125732421875,
    image=image_image_7
)

canvas.create_text(
    46.0,
    279.0,
    anchor="nw",
    text="8908 7931 0987 2222",
    fill="#FFFFFF",
    font=("OpenSansRoman Regular", 12 * -1)
)

canvas.create_text(
    248.3486328125,
    270.800048828125,
    anchor="nw",
    text="500 ₽",
    fill="#428D39",
    font=("OpenSansRoman SemiBold", 12 * -1)
)

canvas.create_text(
    46.3486328125,
    295.800048828125,
    anchor="nw",
    text="Входящий перевод\nСообщение: Привет мир!",
    fill="#898989",
    font=("OpenSansRoman Regular", 10 * -1)
)


canvas.create_rectangle(
    5.0,
    344.0,
    292.0,
    404.0,
    fill="#1E1E1E",
    outline="")

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    21.0,
    372.125732421875,
    image=image_image_8
)

canvas.create_text(
    46.0,
    356.0,
    anchor="nw",
    text="8888 1234 5678 9999",
    fill="#FFFFFF",
    font=("OpenSansRoman Regular", 12 * -1)
)

canvas.create_text(
    248.3486328125,
    355.800048828125,
    anchor="nw",
    text="100 ₽",
    fill="#428D39",
    font=("OpenSansRoman SemiBold", 12 * -1)
)

canvas.create_text(
    46.3486328125,
    375.800048828125,
    anchor="nw",
    text="Входящий перевод",
    fill="#898989",
    font=("OpenSansRoman Regular", 10 * -1)
)

canvas.create_rectangle(
    6.0,
    422.0,
    293.0,
    482.0,
    fill="#1E1E1E",
    outline="")

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    22.0,
    450.125732421875,
    image=image_image_9
)

canvas.create_text(
    47.0,
    434.0,
    anchor="nw",
    text="1234 56789 0000 0023",
    fill="#FFFFFF",
    font=("OpenSansRoman Regular", 12 * -1)
)

canvas.create_text(
    249.3486328125,
    433.800048828125,
    anchor="nw",
    text="900 ₽",
    fill="#428D39",
    font=("OpenSansRoman SemiBold", 12 * -1)
)

canvas.create_text(
    47.3486328125,
    453.800048828125,
    anchor="nw",
    text="Входящий перевод",
    fill="#898989",
    font=("OpenSansRoman Regular", 10 * -1)
)

canvas.create_rectangle(
    6.0,
    500.0,
    293.0,
    560.0,
    fill="#1E1E1E",
    outline="")

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    22.0,
    528.125732421875,
    image=image_image_10
)

canvas.create_text(
    47.0,
    512.0,
    anchor="nw",
    text="0321 1000 0904 8856",
    fill="#FFFFFF",
    font=("OpenSansRoman Regular", 12 * -1)
)

canvas.create_text(
    249.3486328125,
    511.800048828125,
    anchor="nw",
    text="500 ₽",
    fill="#428D39",
    font=("OpenSansRoman SemiBold", 12 * -1)
)

canvas.create_text(
    47.3486328125,
    531.800048828125,
    anchor="nw",
    text="Входящий перевод",
    fill="#898989",
    font=("OpenSansRoman Regular", 10 * -1)
)
window.resizable(False, False)
window.mainloop()
