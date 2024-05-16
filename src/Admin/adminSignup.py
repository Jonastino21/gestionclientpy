from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, filedialog
import mysql.connector

def fenetre():{
    
}

def createTable():
    try:
        mytable = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="threel"
        )
        mycursor = mytable.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS AdminSignup (Id_admin INT AUTO_INCREMENT PRIMARY KEY, Nom varchar(100), Prénoms varchar(100),Date_de_naissance varchar(50), Sexe varchar(10), Téléphone varchar(30), Cin varchar(30), Photo BLOB, Adresse_émail varchar(50), Mot_de_passe varchar(50))")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

signup = Tk()
signup.title('Inscription en Admin')
signup.geometry('1000x640')
signup.resizable(False,False)

createTable()

canvas = Canvas(signup,width=1000, height=640, background='#1b7e7e')
canvas.place(x=0,y=0)

img2_path = "./icones/logo.png"
original_image2 = Image.open(img2_path)
new_width2 = 30 
new_height2 = 30  
resized_image2 = original_image2.resize((new_width2, new_height2))

logo = ImageTk.PhotoImage(resized_image2)
label1 = Label(signup, text="sary", image=logo)
label1.place(x=410,y=43)


#Label
formulaire = Label(signup,text='Formulaire', font='calibri 20 bold', background='#1b7e7e')
formulaire.place(x=450,y=40)

nom = Label(signup, text='Nom', background='#1b7e7e')
nom.place(x=210, y=100)
prenoms = Label(signup, text='Prénoms', background='#1b7e7e')
prenoms.place(x=530,y=100)
date_naissance = Label(signup, text='Date de naissance', background='#1b7e7e')
date_naissance.place(x=210, y=170)
sexe = Label(signup, text='Sexe', background='#1b7e7e')
sexe.place(x=530,y=170)
telephone = Label(signup, text='Téléphone ', background='#1b7e7e')
telephone.place(x=210, y=240)
photo = Label(signup, text='Photo', background='#1b7e7e')
photo.place(x=530, y=240)
adresse_email = Label(signup, text='Adresse émail', background='#1b7e7e')
adresse_email.place(x=210,y=310)
mot_de_passe = Label(signup, text='Mot de passe', background='#1b7e7e')
mot_de_passe.place(x=530,y=310)

#Entry
e_nom = Entry(signup,width=35)
e_nom.place(x=210, y=130,height=30)
e_prenoms = Entry(signup,width=35)
e_prenoms.place(x=530,y=130,height=30)
e_date_naissance = Entry(signup,width=35)
e_date_naissance.place(x=210, y=200,height=30)
e_sexe = Entry(signup,width=35)
e_sexe.place(x=530,y=200,height=30)
e_telephone = Entry(signup,width=35)
e_telephone.place(x=210, y=270,height=30)
e_photo = Entry(signup,width=35)
e_photo.place(x=530,y=270,height=30)
e_adresse_email = Entry(signup,width=35)
e_adresse_email.place(x=210, y=340,height=30)


def update_entry():
    global hidden
    hidden = not hidden
    if hidden:
        e_mot_de_passe['show'] = '.'
        btn['image'] = hide
    else:
        e_mot_de_passe['show'] = ''
        btn['image'] = view

e_mot_de_passe = Entry(signup,width=35,show='.')
e_mot_de_passe.place(x=530,y=340,height=30)

hidden = True

hide = ImageTk.PhotoImage(Image.open('./icones/hide.png').resize((20,20)))
view = ImageTk.PhotoImage(Image.open('./icones/view.png').resize((20,20)))

btn = Button(signup ,image=hide, bg='white',bd=0,command=update_entry,activebackground='white', borderwidth=0, highlightthickness=0)
btn.place(x=790,y=343)


identification = Button(signup, text="S'identifier",command=fenetre)
identification.place(x=465,y=400)



signup.mainloop()
