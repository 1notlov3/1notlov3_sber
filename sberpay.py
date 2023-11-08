from pathlib import Path
import subprocess
from tkinter import *
import os
from customtkinter import *
import pyodbc
from tkinter import messagebox

OUTPUT_PATH = Path(os.path.dirname(__file__))
ASSETS_PATH = OUTPUT_PATH / Path("assets/sberpay")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def go_to_pay():
    window.destroy()
    subprocess.Popen(['python', 'payments.py'])

def transfer_money():
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Sber\Бд.accdb')
    cursor = conn.cursor()
    phone_number=entry_3.get()
    amount=entry_1.get()
    # Connect to the database


    # Get the user's ID based on their phone number
    cursor.execute("SELECT id_пользователя FROM Пользователи WHERE Телефон = ?", phone_number)
    result = cursor.fetchone()

    if result:
        user_id = result[0]



        # Update the card balance
        cursor.execute("UPDATE Карты SET Балланс_карты = Балланс_карты + ? WHERE id_пользователя = ?", amount, user_id)
        conn.commit()


        messagebox.showinfo("Успешный перевод",(f"Успешно переведено {amount} рублей на номер {phone_number}"))
        go_to_pay()
    else:
        messagebox.showerror("Ошибка",(f"Пользователь с номером телефона {phone_number} не найден в базе"))

  

window = Tk()
window.title("sber")
window.iconbitmap("sber.ico")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

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
    104.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    151.0,
    17.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    150.0,
    124.5,
    image=entry_image_1
)
entry_1 = CTkEntry(
    window,
    fg_color="#05753B",
    bg_color="#05753B",
    text_color="light gray",
    font = ("Arial",24),
    border_width=0,
    width=300.0,
    height=43.0,
    justify="center"
)
entry_1.place(
    x=0.0,
    y=102.0,
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    135.5,
    178.0,
    image=entry_image_2
)
entry_2 = CTkEntry(
    window,
    fg_color="#23A463",
    bg_color="#23A463",
    text_color="light gray",
    width=237.0,
    height=42.0,
    border_width=0,
    placeholder_text="Сообщение получателю",
    placeholder_text_color="light gray",
    
    
)
entry_2.place(
    x=17.0,
    y=156.0,
    
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg="#078A48",
    activebackground="#078A48",
    command=lambda: go_to_pay(),
    relief="flat"
)
button_1.place(
    x=3.0,
    y=42.0,
    width=19.0,
    height=22.0
)

button_pay=CTkButton(
    window, 
    fg_color = "#078A48",
    hover_color= "#078A48",
    text = "Перевести",
    width=200,
    command = lambda: transfer_money()

)
button_pay.place(x=50,y = 500)

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
    281.0,
    170.0,
    image=image_image_4
)

canvas.create_text(
    125.0,
    75.0,
    anchor="nw",
    text="Сумма",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 15 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    278.0,
    52.0,
    image=image_image_5
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    149.5,
    55.0,
    image=entry_image_3
)
entry_3 = CTkEntry(
    window,
    fg_color="#23A463",
    bg_color="#23A463",
    text_color="light gray",
    width=161.0,
    height=22.0,
    border_width=0,
    placeholder_text="Номер телефона",
    placeholder_text_color="light gray",
    justify="center"
)
entry_3.place(
    x=69.0,
    y=43.0,
)
entry_1.focus_set()
image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    37.0,
    249.0,
    image=image_image_6
)

canvas.create_text(
    62.0,
    215.0,
    anchor="nw",
    text="Счёт списания",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 14 * -1)
)

canvas.create_text(
    231.0,
    241.0,
    anchor="nw",
    text="0 ₽",
    fill="#428D39",
    font=("OpenSansRoman SemiBold", 14 * -1)
)

canvas.create_text(
    55.25,
    250.25,
    anchor="nw",
    text="●●●● ",
    fill="#FFFFFF",
    font=("Roboto Regular", 10 * -1)
)

canvas.create_text(
    81.5,
    251.5,
    anchor="nw",
    text="0000",
    fill="#FFFFFF",
    font=("OpenSansRoman SemiBold", 10 * -1)
)


window.resizable(False, False)
window.mainloop()
