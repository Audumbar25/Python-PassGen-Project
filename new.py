from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_char = string.punctuation
    
    all_chars = small_alphabets + capital_alphabets + numbers + special_char
    pass_length = int(length_box.get())
    
    if choice.get() == 1:
        passwordfield.delete(0, END)
        password = ''.join(random.sample(small_alphabets, pass_length))
        passwordfield.insert(0, password)
        
    elif choice.get() == 2:
        passwordfield.delete(0, END)
        password = ''.join(random.sample(small_alphabets + capital_alphabets, pass_length))
        passwordfield.insert(0, password)
    
    elif choice.get() == 3:
        passwordfield.delete(0, END)
        password = ''.join(random.sample(all_chars, pass_length))
        passwordfield.insert(0, password)
        
def copy():  
    copied_pass = passwordfield.get()
    pyperclip.copy(copied_pass)

root = Tk()
root.config(bg='gray20')
root.title("Password Generator")

Font=('Arial', 13, 'bold')

passwordlabel = Label(root, text='Password Generator', font=('Times New Roman', 20, 'bold'), bg='gray20', fg='white')
passwordlabel.grid(pady=15)

choice = IntVar()

weakradiobutton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font, bg='gray20', fg='white')
weakradiobutton.grid(pady=10)

mediumradiobutton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font, bg='gray20', fg='white')
mediumradiobutton.grid(pady=10)

strongradiobutton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font, bg='gray20', fg='white')
strongradiobutton.grid(pady=10)

plengthlabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
plengthlabel.grid(pady=2)

length_box = Spinbox(root, from_=5, to_=20, width=6, font=Font)
length_box.grid(pady=15)

generatebutton = Button(root, text='Generate', font=Font, command=generator)
generatebutton.grid(pady=10)

passwordfield = Entry(root, width=25, font=Font)
passwordfield.grid()

copybutton = Button(root, text='Copy', font=Font, command=copy)
copybutton.grid(pady=15)

root.mainloop()
