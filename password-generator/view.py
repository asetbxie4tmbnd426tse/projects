
from tkinter import messagebox, filedialog
from tkinter.constants import END
import tkinter as tk
import passwordGenerator as pg
import saveAsJSON as saj
import os


width = 400
hight = 250
root = tk.Tk()
root.title("password generator")
root.geometry(f"{width}x{hight}")


def error_pop_up(message: str):
    messagebox.showerror("error",message)

def generate_password():
    try:
        new_password = pg.generate_password(lengh=int(password_lengh_tb.get(1.0, END)), apper=apper.get(), lower=lower.get(), nums=nums.get(), symb=symb.get())
        password_tb.delete(1.0,"end")
        password_tb.insert(1.0, new_password)
    except:
        error_pop_up("make sure the lengh is a number. It should not include '.' or ',' and you checked at least one of the options to the right.")

def open_file_dialog() -> str:
    return filedialog.askopenfilename()

def save(username: str, password: str, email: str, app_name: str, notes: str = None):
    cont = pg.to_dictionarey(app_name=app_name,username=username, password=password, email=email, notes=notes)
    file_path = open_file_dialog()
    saj.add(file_path=file_path, cont=cont)

def open_save_window():
    save_window = tk.Toplevel()
    save_window.title("Save")
    
    username_lable = tk.Label(save_window, text="username:")
    username_lable.grid(column=0, row=3)

    username_tb = tk.Text(save_window, height=1, width = 20, bg = "white")
    username_tb.grid(column=1,row=3,)

    email_lable = tk.Label(save_window, text="email:")
    email_lable.grid(column=0, row=4)

    email_tb = tk.Text(save_window, height=1, width = 20, bg = "white")
    email_tb.grid(column=1,row=4)

    app_name_lable = tk.Label(save_window, text="application name:")
    app_name_lable.grid(column=0, row=5)

    app_name_tb = tk.Text(save_window, height=1, width = 20, bg = "white")
    app_name_tb.grid(column=1,row=5)
    
    notes_lable = tk.Label(save_window, text="notes:")
    notes_lable.grid(column=0, row=6)

    notes_tb = tk.Text(save_window, height=5, width = 20, bg = "white")
    notes_tb.grid(column=1,row=6)

    new_file_button = tk.Button(save_window, text="New file")
    new_file_button.grid(column=0, row=7, columnspan=2)

    save_button = tk.Button(save_window, text="Save", command= lambda: save(
        app_name=app_name_tb.get(1.0, END),
        username=username_tb.get(1.0, END),
        password=password_tb.get(1.0, END),
        email=email_tb.get(1.0, END),
        notes=notes_tb.get(1.0, END)
        ))
    save_button.grid(column=1, row=7, columnspan=2)

#---------------pasword generating gui part------------------------

password_lengh_lable = tk.Label(root, text="please specify the lengh of the password without '.' or ',':")
password_lengh_lable.grid(column=0, row=0)

password_lengh_tb = tk.Text(root, height=1, width = 10, bg = "white")
password_lengh_tb.grid(column=1, row=0)

password_generator_button = tk.Button(root, text="Generate password", command=generate_password)
password_generator_button.grid(column=0, row=6, columnspan=2)

password_tb = tk.Text(root, height=4, width = 40, bg = "white")
password_tb.grid(column=0, row=7, columnspan=2)

apper = tk.BooleanVar()
lower = tk.BooleanVar()
nums = tk.BooleanVar()
symb = tk.BooleanVar()

apper_cb = tk.Checkbutton(root, text="Include uppercase", variable=apper)
apper_cb.grid(column=0, row=2)

lower_cb = tk.Checkbutton(root, text="Include lowercase", variable=lower)
lower_cb.grid(column=0, row=3)

nums_cb = tk.Checkbutton(root, text="Include numbers", variable=nums)
nums_cb.grid(column=0, row=4)

symb_cb = tk.Checkbutton(root, text="Include symbols", variable=symb)
symb_cb.grid(column=0, row=5)

#-----------save file gui part-------------------------------------

save_button = tk.Button(root, text="Save", command=open_save_window)
save_button.grid(column=0, row=8, columnspan=2)

#-----------------------------------------------------------------

root.mainloop()