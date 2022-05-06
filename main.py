import random
from tkinter import *
import string
import pyperclip

# Créer la fontion de génération du password
def generator():
  lettres = string.ascii_letters
  chiffres = string.digits
  ponc = string.punctuation 
  mylist = lettres+chiffres+ponc
  pwd = "".join(random.choices(mylist, k=12))  
  enter_pwd.delete(0, END)
  enter_pwd.insert(0, pwd)
 

# Créer la fontion de copy du password
def copy():
  pyperclip.copy(enter_pwd.get())
  # enter_pwd.delete(0, END)

# Créer la fenetre
bg_color = '#1e1e1e'

window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.maxsize(width=720, height=480)
window.minsize(width=720, height=480)
window.iconbitmap("RedCoding.ico")
window.config(background = bg_color)

# Créer une frame pricipale
frame = Frame(window, bg = bg_color)

# Creation d'image
width = 300
height = 300
image = PhotoImage(file="pwd.png")
canvas = Canvas(frame, width = width, height = height, bg = bg_color, bd = 0, highlightthickness = 0 )
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row = 0, column=0, sticky=W)

# Créer une sous frame
r_frame = Frame(frame, bg = bg_color)
photo_btn = PhotoImage(file="copy.png")
# Créer une sous frame
r_r_frame = Frame(frame, bg = bg_color)

# créer un titre 
label_title = Label(r_frame, text="Mot de passe", font=("Helvetica", 20), bg = bg_color, fg='#aaa')
label_title.pack()

# créer un champ/entrée/input
enter_pwd = Entry(r_frame, font=("Helvetica", 20), bg = bg_color, fg='#aaa')
enter_pwd.pack()




# creer un bouton generate
generate_pwd_button = Button(r_frame, text="Générer", font=("Helvetica", 20), bg = bg_color, fg='#aaa', command = generator)
generate_pwd_button.pack(fill = X, pady=10)

# créer un bouton copier
copy_pwd_button = Button(window, image=photo_btn, bg ="#fff", command = copy)
copy_pwd_button.place(x=665, y=201)

# On place la sous frame à droite de la frame principale
r_frame.grid(row = 0, column=1,sticky=W)

# On place la sous frame à droite de la frame de droite
r_r_frame.grid(row = 0, column=2, sticky=W)

# Afficher la Frame
frame.pack(expand=YES)


window.mainloop()


