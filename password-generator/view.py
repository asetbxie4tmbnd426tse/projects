import tkinter as tk
from tkinter.constants import END
import passwordGenerator as pg

root = tk.Tk()
root.title("password generator")
root.geometry("800x400")

def generate_password():
    lengh = password_lengh_tb.get(1.0, END)
    pass

password_lengh_lable = tk.Label(root, text="please specify the lengh of the password without '.' or ',':")
password_lengh_lable.grid(column=0, row=0)

password_lengh_tb = tk.Text(root, height=1, width = 10, bg = "white")
password_lengh_tb.grid(column=1, row=0)

password_tb = tk.Text(root, height=4, width = 40, bg = "white")
password_tb.grid(column=0, row=2, columnspan=2)

password_generator_button = tk.Button(root, text="Generate password", command=generate_password)
password_generator_button.grid(column=0, row=1, columnspan=2)

apper_lable = tk.Label(root, text="Include uppercase:")
apper_lable.grid(column=3, row=0)

lower_lable = tk.Label(root, text="Include lowercase:")
lower_lable.grid(column=3, row=1)

num_lable = tk.Label(root, text="Include numbers:")
num_lable.grid(column=5, row=0)

symb_lable = tk.Label(root, text="Include symbols:")
symb_lable.grid(column=5, row=1)

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

password_generator_button = tk.Button(root, text="Save")
password_generator_button.grid(column=0, row=6, columnspan=2)

root.mainloop()