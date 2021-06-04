import tkinter as tk
from tkinter.constants import END
import passwordGenerator as pg

root = tk.Tk()
root.title("password generator")
root.geometry("800x400")

def generate_password():
    try:
        new_password = pg.generate_password(lengh=int(password_lengh_tb.get(1.0, END)), apper=apper.get(), lower=lower.get(), nums=nums.get(), symb=symb.get())
        password_tb.delete(1.0,"end")
        password_tb.insert(1.0, new_password)
    except:
        pass

password_lengh_lable = tk.Label(root, text="please specify the lengh of the password without '.' or ',':")
password_lengh_lable.grid(column=0, row=0)

password_lengh_tb = tk.Text(root, height=1, width = 10, bg = "white")
password_lengh_tb.grid(column=1, row=0)

password_tb = tk.Text(root, height=4, width = 40, bg = "white")
password_tb.grid(column=0, row=2, columnspan=2)

password_generator_button = tk.Button(root, text="Generate password", command=generate_password)
password_generator_button.grid(column=0, row=1, columnspan=2)

apper = tk.BooleanVar()
lower = tk.BooleanVar()
nums = tk.BooleanVar()
symb = tk.BooleanVar()

apper_cb = tk.Checkbutton(root, text="Include uppercase", variable=apper)
apper_cb.grid(column=3, row=0)

lower_cb = tk.Checkbutton(root, text="Include lowercase", variable=lower)
lower_cb.grid(column=3, row=1)

nums_cb = tk.Checkbutton(root, text="Include numbers", variable=nums)
nums_cb.grid(column=5, row=0)

symb_cb = tk.Checkbutton(root, text="Include symbols", variable=symb)
symb_cb.grid(column=5, row=1)

username_lable = tk.Label(root, text="username:")
username_lable.grid(column=0, row=3)

username_tb = tk.Text(root, height=1, width = 20, bg = "white")
username_tb.grid(column=1,row=3,)

email_lable = tk.Label(root, text="email:")
email_lable.grid(column=0, row=4)

email_tb = tk.Text(root, height=1, width = 20, bg = "white")
email_tb.grid(column=1,row=4)

app_name_lable = tk.Label(root, text="application name:")
app_name_lable.grid(column=0, row=5)

app_name_tb = tk.Text(root, height=1, width = 20, bg = "white")
app_name_tb.grid(column=1,row=5)

#url_lable = tk.Label(root, text="url:")
#url_lable.grid(column=0, row=6)

save_button = tk.Button(root, text="Save")
save_button.grid(column=0, row=6, columnspan=2)

root.mainloop()