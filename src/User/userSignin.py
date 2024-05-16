from tkinter import * 
from PIL import Image, ImageTk
import webbrowser
from tkinter import ttk



login = Tk()
login.title("Se connecter à Three L")
login.geometry("1000x640")
login.resizable(False, False)

#right page
img_path = "./Images/img1.png"
original_image = Image.open(img_path)
new_width = 500 
new_height = 640  
resized_image = original_image.resize((new_width, new_height))

photo = ImageTk.PhotoImage(resized_image)
label = Label(login, text="sary", image=photo)
label.place(x=500,y=-1)
#---------------------------

#Left page
img2_path = "./icones/logo.png"
original_image2 = Image.open(img2_path)
new_width2 = 60 
new_height2 = 60  
resized_image2 = original_image2.resize((new_width2, new_height2))

logo = ImageTk.PhotoImage(resized_image2)
label1 = Label(login, text="sary", image=logo)
label1.place(x=100,y=50)
titre = Label(login, text="Three L", font=("Arial",39))
titre.place(x=170,y=55)

login_label = Label(login, text="Se connecter", font=("arial", 24))
login_label.place(x=100,y=150)

e_username = Entry(login,width=35,relief="raised", bg='lavender')
e_username.place(x=100,y=220,height=40)
username = Label(login, text="Adresse émail")
username.place(x=100,y=262)


e_password = Entry(login,width=35,relief="raised", bg='lavender',show='.')
e_password.place(x=100, y=320,height=40)
password = Label(login, text="Mot de passe")
password.place(x=100,y=362)

connexion_bouton = Button(login,text="Connexion",background='#39a0c0',command="exit")
connexion_bouton.place(x=200, y=430)

def update_entry():
    global hidden
    hidden = not hidden
    if hidden:
        e_password['show'] = '.'
        btn['image'] = hide
    else:
        e_password['show'] = ''
        btn['image'] = view

hidden = True

hide = ImageTk.PhotoImage(Image.open('./icones/hide.png').resize((30,30)))
view = ImageTk.PhotoImage(Image.open('./icones/view.png').resize((30,30)))

btn = Button(login ,image=hide, bg='lavender',bd=0,command=update_entry)
btn.place(x=350,y=323)

def open_link():
    webbrowser.open("#")


# Créer un label avec le style "link" pour simuler un lien hypertexte
style = ttk.Style()
style.configure("link.TLabel", foreground="blue", cursor="hand2")

label = ttk.Label(login, text="Mot de passe oublié", style="link.TLabel")
label.place(x=185, y=400)

# Associer la fonction open_link au clic sur le label
label.bind("<Button-1>", lambda e: open_link())

















login.mainloop() 
