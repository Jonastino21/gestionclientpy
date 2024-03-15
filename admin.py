from tkinter import * 
from PIL import Image, ImageTk
import webbrowser
from tkinter import ttk



login = Tk()
login.title("Admin Connexion")
login.geometry("1000x640")
login.resizable(False, False)






canvas = Canvas(login, width=1000, height=640, background='#1b7e7e')
canvas.place(x=0,y=0)

#Landing
img2_path = "logo.png"
original_image2 = Image.open(img2_path)
new_width2 = 60 
new_height2 = 60  
resized_image2 = original_image2.resize((new_width2, new_height2))

logo = ImageTk.PhotoImage(resized_image2)
label1 = Label(login, text="sary", image=logo)
label1.place(x=360,y=50)
titre = Label(login, text="Three L", font=("Arial",39), background='#1b7e7e')
titre.place(x=445,y=55)

login_label = Label(login, text="Se connecter", font=("arial", 24), background='#1b7e7e')
login_label.place(x=400,y=150)

e_username = Entry(login,width=35,relief="raised", bg='lavender')
e_username.place(x=360,y=220,height=40)
username = Label(login, text="Adresse émail", background='#1b7e7e')
username.place(x=360,y=262)

def update_entry():
    global hidden
    hidden = not hidden
    if hidden:
        e_password['show'] = '.'
        btn['image'] = hide
    else:
        e_password['show'] = ''
        btn['image'] = view
    

e_password = Entry(login,width=35,relief="raised",show='.', background='lavender')
e_password.place(x=360, y=320,height=40)
password = Label(login, text="Mot de passe", background='#1b7e7e')
password.place(x=360,y=362)


hidden = True

hide = ImageTk.PhotoImage(Image.open('hide.png').resize((30,30)))
view = ImageTk.PhotoImage(Image.open('view.png').resize((30,30)))

btn = Button(login ,image=hide, bg='lavender',bd=0,command=update_entry,activebackground='lavender', borderwidth=0, highlightthickness=0)
btn.place(x=610,y=323)


def open_link():
    webbrowser.open("#")

# Créer un label avec le style "link" pour simuler un lien hypertexte
style = ttk.Style()
style.configure("link.TLabel", foreground="blue", cursor="hand2")

label = ttk.Label(login, text="Mot de passe oublié", style="link.TLabel", background='#1b7e7e')
label.place(x=445, y=400)

# Associer la fonction open_link au clic sur le label
label.bind("<Button-1>", lambda e: open_link())

connexion_bouton = Button(login,text="Connexion",background='#39a0c0',command="exit")
connexion_bouton.place(x=460, y=430)




def open_link2():
    webbrowser.open("#")

# Créer un label avec le style "link" pour simuler un lien hypertexte
style2 = ttk.Style()
style2.configure("link2.TLabel", foreground="blue", cursor="hand2")

label2 = ttk.Label(login, text="S'inscrire", style="link2.TLabel", background='#1b7e7e')
label2.place(x=478, y=550)

# Associer la fonction open_link au clic sur le label
label2.bind("<Button-1>", lambda e: open_link2())
















login.mainloop() 
