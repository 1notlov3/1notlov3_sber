from pathlib import Path
import subprocess
from tkinter import *
import os
from customtkinter import *
import requests
from tkinter import messagebox
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
ASSETS_PATH = OUTPUT_PATH / Path("assets/exchange")

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
window.configure(bg = "#000000")
def exchange():
    amount = entry_2.get
    print(amount)
    
    messagebox.showinfo(icon="info",title = "Успешный обмен",message=("Вы успешно обменяли валюту"))

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
canvas.create_rectangle(
    0.0,
    265.0,
    300.0,
    317.0,
    fill="#121212",
    outline="")

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

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg = "#121212",
    activebackground="#121212",
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=24.0,
    y=152.0,
    width=85.55120849609375,
    height=85.55120849609375
)

canvas.create_rectangle(
    0.0,
    578.0,
    300.0,
    618.0,
    fill="#1E1E1E",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    148.0,
    106.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_home(),
    relief="flat"
)
button_2.place(
    x=12.002197265625,
    y=581.0,
    width=39.206974029541016,
    height=34.60382080078125
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_payments(),
    relief="flat"
)
button_3.place(
    x=70.41259765625,
    y=581.0,
    width=40.80725860595703,
    height=34.60382080078125
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=130.423095703125,
    y=583.720703125,
    width=39.20697021484375,
    height=33.60595703125
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Label(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    relief="flat"
)
button_5.place(
    x=177.0,
    y=581.0,
    width=54.0,
    height=34.34210205078125
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    bg = "#1E1E1E",
    activebackground="#1E1E1E",
    command=lambda: go_to_history(),
    relief="flat"
)
button_6.place(
    x=248.044189453125,
    y=581.0,
    width=39.20697021484375,
    height=34.60382080078125
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    150.0,
    631.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    30.000030517578125,
    48.18821334838867,
    image=image_image_4
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    154.6443328857422,
    49.09979820251465,
    image=entry_image_1
)
entry_1 = CTkEntry(
    window,
    fg_color="#3B4E40",
    bg_color="#3B4E40",
    text_color="white",
    border_width=0,
    width=170.30202865600586,
    height=22.199588775634766
)
entry_1.place(
    x=55.99331855773926,
    y=37.000003814697266,
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

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    150.0,
    393.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    37.0,
    299.0,
    image=image_image_8
)

canvas.create_text(
    15.0,
    270.0,
    anchor="nw",
    text="СЧЁТ СПИСАНИЯ",
    fill="gray65",
    font=("OpenSansRoman SemiBold", 7 * -1)
)

canvas.create_text(
    231.0,
    291.0,
    anchor="nw",
    text=clean_bal+"₽",
    fill="#428D39",
    font=("OpenSansRoman SemiBold", 12 * -1)
)

canvas.create_text(
    55.0,
    300.0,
    anchor="nw",
    text="●●●● ",
    fill="#FFFFFF",
    font=("Roboto Regular", 6 * -1)
)

canvas.create_text(
    73.0,
    302.0,
    anchor="nw",
    text="0000",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 6 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    74.0,
    364.5,
    image=entry_image_2
)
entry_2 = CTkEntry(
    window,
    fg_color="#1E1E1E",
    bg_color="#1E1E1E",
    text_color="white",
    border_width=0,
    width=58.0,
    height=21.0
    
)
entry_2.place(
    x=45.0,
    y=353.0,
)

def option_callback(choice):
    print("combobox dropdown clicked:", choice)

option = CTkOptionMenu(window, fg_color= "#1E1E1E", button_color="#1E1E1E", button_hover_color="#1E1E1E", values=["Доллары", "Евро","Юани"],
                                     command=option_callback)
option.set("Доллар")

option.place(x=11,y=420)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    bg = "#121212",
    activebackground="#121212",
    command=lambda: exchange(),
    relief="flat"
)
button_7.place(
    x=13.0,
    y=504.0,
    width=274.0,
    height=30.0
)
window.resizable(False, False)
window.mainloop()
