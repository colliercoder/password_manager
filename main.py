from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for letter in range(randint(8, 10))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]
    password_list += [choice(numbers) for number in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    entry = f"{website_input.get()}|{email_input.get()}|{password_input.get()}"

    if website_input.get() == "" or password_input.get() == "":
        messagebox.showwarning(title="Greetings PENDEJO", message="Do not leave fields blank")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(),message=f"These are the details entered: \n" \
                                                                  f"\nEmail: {email_input.get()}" \
                                                                  f"\nPassword: {password_input.get()}"
                                                                  f"\nIs it ok to save?")
        if is_ok:
            with open("passwords.txt","a") as data_file:
                data_file.write(f"{entry}\n")
                website_input.delete(0,END)
                password_input.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height= 200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row = 0,column=1)

#Labels

website = Label(text="Website:")
website.grid(row =1, column = 0)

email = Label(text="Email/Username:")
email.grid(row =2, column = 0)

password = Label(text="Password:")
password.grid(row =3, column = 0)

#Entrys
website_input = Entry(width=35)
website_input.grid(column=1,row=1,columnspan=2,sticky=EW)


email_input = Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2,sticky=EW)
email_input.insert(0,"dummyemail@dumbmail.com")


password_input = Entry(width=21)
password_input.grid(column=1,row=3,sticky=EW)

#Buttons



generate_password = Button(text="Generate Password", command=gen_pass)
generate_password.grid(row=3,column=2,sticky=EW)

add_password = Button(text="Add", command=save_password,width=36)
add_password.grid(row=4,column=1,columnspan=2,sticky=EW)









window.mainloop()