import subprocess
from pathlib import Path
from customtkinter import *
from tkinter import *
import os
import pyodbc
from tkinter import messagebox

# Получаем путь к папке, где находится база данных
folder_path = os.path.dirname(os.path.abspath(__file__))

# Подключаемся к базе данных
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Sber\Бд.accdb')
cursor = conn.cursor()


def check():
    telephone = entry_1.get()
    password = entry_2.get()
    cursor.execute(f"SELECT * FROM Пользователи WHERE Телефон = '{telephone}' And Пароль = '{password}'")
    result = cursor.fetchone()
    print(result)
    if result:
        window.destroy()
        with open('my_file.txt', 'w') as f:
            f.write((telephone))
        subprocess.Popen(['python', 'home.py'])
    else:
        messagebox.showerror("Ошибка", "Неправильный логин или пароль", icon="error", type="ok", parent=window)
       

OUTPUT_PATH = Path(os.path.dirname(__file__))
ASSETS_PATH = OUTPUT_PATH / Path("assets/login")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def go_to_home():
    window.destroy()
    subprocess.Popen(['python', 'home.py'])
    
window = Tk()
window.title("sber")
window.iconbitmap("sber.ico")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Устанавливаем положение главного окна по центру экрана
window.geometry(f"300x645+{int((screen_width-300)/2)}+{int((screen_height-645)/2)}")
window.configure(bg = "#000000")
print(folder_path)

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

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    149.0,
    17.0,
    image=image_image_2
)

canvas.create_text(
    68.0,
    247.0,
    anchor="nw",
    text="Здравствуйте,",
    fill="#FFFFFF",
    font=("OpenSansRoman Bold", 24 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    150.0,
    192.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    151.0,
    630.0,
    image=image_image_4
)

entry_1 = CTkEntry(
    window,
    fg_color="#1E1E1E",
    text_color= "white",
    corner_radius=10,
    border_color="#1E1E1E",
    placeholder_text="Введите номер телефона",
    width=220,
    height=40
)
entry_1.place(
    x=43.0,
    y=323.0,
    
)


entry_2 = CTkEntry(
    window,
    fg_color="#1E1E1E",
    corner_radius=10,
    border_color="#1E1E1E",
    text_color= "white",
    placeholder_text="Введите пароль",
    width=220,
    height=40
)
entry_2.place(
    x=43.0,
    y=398.0,
   
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg="#000000",
    activebackground="#000000",
    command=lambda: check(),
    relief="flat"
)
button_1.place(
    x=85.0,
    y=485.0,
    width=130.0,
    height=39.0
)
window.resizable(False, False)
window.mainloop()
