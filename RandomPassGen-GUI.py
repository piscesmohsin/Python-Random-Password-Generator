#importing Libraries

from tkinter import *
import random, string
import pyperclip



###initialize window

root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("SECURE PASSWORD GENERATOR")
root.configure(bg='black')

f1=Frame(root,bg='BLACK')
f1.pack(expand=True)
f2=Frame(root,bg='Black')

#heading
###select password length
pass_label = Label(f2, text = 'Password Length:', font = 'arial 10 bold',bg='black',fg='WHITE',pady=10).pack(anchor='center')

pass_len = IntVar()
length = Spinbox(f2, from_ = 16, to_ = 64 , textvariable = pass_len , width = 20).pack(anchor='center')



#####define function

pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
    Gen_pass=Label(f2, text = 'Generated Password:', font = 'arial 10 bold',bg='black',fg='WHITE',pady=5).pack(anchor='center')
    Entry(f2 , textvariable = pass_str, width=25).pack()
    btn=Button(f2, text = 'COPY TO CLIPBOARD', borderwidth= 0,command = Copy_password,width=15,bg='WHITE',fg='BLACK').pack(pady=10)
# btn.place(relx=0.5, rely=0.5, anchor=CENTER)



###button

Button(f2, text = "GENERATE" , command = Generator, width=15,borderwidth= 0,bg='WHITE',fg='BLACK' ).pack(pady= 10)




########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())


f2.pack(anchor=CENTER)
f3=Frame(root,bg='BLACK')
f3.pack(expand=True)
# loop to run program
root.mainloop()
