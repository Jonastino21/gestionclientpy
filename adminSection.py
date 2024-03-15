import mysql.connector
import hashlib
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, filedialog
import io

def createDatabase():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS threel")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def createTable():
    try:
        mytable = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="threel"
        )
        mycursor = mytable.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS Prix_m² (Prix_m² INT(11))")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Pourcentage_1er_payement (Pourcentage_1er_payement INT(11))")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Tranche_de_payement (Tranche_de_payement INT(11))")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Liste_employers (Id_employer INT AUTO_INCREMENT PRIMARY KEY, Nom varchar(100), Prénoms varchar(100),Date_de_naissance varchar(50), Sexe varchar(10),  Cin varchar(30), Téléphone varchar(30), Photo BLOB, Adresse_émail varchar(50), Mot_de_passe varchar(50))")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

createDatabase()
createTable()

def hash_password(password):
    # Convertir le mot de passe en bytes (la fonction de hachage hashlib nécessite des données de type bytes)
    password_bytes = password.encode('utf-8')

    # Créer un objet de hachage SHA-256
    sha256_hash = hashlib.sha256()

    # Mettre à jour le hachage avec les données du mot de passe
    sha256_hash.update(password_bytes)

    # Obtenir le hachage en hexadécimal
    hashed_password = sha256_hash.hexdigest()

    return hashed_password

password = "mon_mot_de_passe"
hashed_password = hash_password(password)
print("Mot de passe haché:", hashed_password)

def charger_photo(self):
    filepath = filedialog.askopenfilename(title="Sélectionner une photo", filetypes=[('png files','.png'),('all files','.*')])
    if filepath:
        # Ouvrir l'image avec PIL
        self.photo_path = filepath
        with Image.open(self.photo_path) as img:
            img = img.resize((50, 50))
        
        
        # photo_tk = ImageTk.PhotoImage(image_pil)
        # # Afficher l'image dans un Label
        # photo.configure(image=photo_tk)
        # photo.image = photo_tk  
        
class Modal:
    def __init__(self,parent,title):
        self.parent = parent
        global e_nom
        global e_prenoms
        global e_date_naissance
        global e_sexe
        global e_cin
        global e_telephone
        global e_adresse_email
        global e_mot_de_passe
        global photo

        # Créer une nouvelle fenêtre modale
        self.modal = Toplevel(parent)
        self.modal.title(title)
        self.modal.resizable(False,False)
        self.modal.geometry('500x400')
      

        nom = Label(self.modal, text='Nom')
        nom.place(x=60, y=50)
        prenoms = Label(self.modal, text='Prénoms')
        prenoms.place(x=300,y=50)
        date_naissance = Label(self.modal, text='Date de naissance')
        date_naissance.place(x=60, y=120)
        sexe = Label(self.modal, text='Sexe')
        sexe.place(x=300,y=120)
        telephone = Label(self.modal, text='Téléphone ')
        telephone.place(x=60, y=190)
        photo = Label(self.modal)
        photo.place(x=150, y=330)
        btn_charger_photo = Button(self.modal, text="Photo", command=charger_photo)
        btn_charger_photo.place(x=60, y=340)
        adresse_email = Label(self.modal, text='Adresse émail')
        adresse_email.place(x=60,y=260)
        mot_de_passe = Label(self.modal, text='Mot de passe')
        mot_de_passe.place(x=300,y=260)
        cin = Label(self.modal, text='Cin')
        cin.place(x=300,y=190)

        #Entry
        e_nom = Entry(self.modal,width=20)
        e_nom.place(x=60, y=80,height=30)
        e_prenoms = Entry(self.modal,width=20)
        e_prenoms.place(x=300,y=80,height=30)
        e_date_naissance = Entry(self.modal,width=20)
        e_date_naissance.place(x=60, y=150,height=30)
        e_sexe = ttk.Combobox(self.modal, width=19)
        e_sexe['background']='white'
        e_sexe["values"]=("Homme","Femme")
        e_sexe.current(0)
        e_sexe.place(x=300,y=150,height=30)
        e_telephone = Entry(self.modal,width=20)
        e_telephone.place(x=60, y=220,height=30)
        e_adresse_email = Entry(self.modal,width=20)
        e_adresse_email.place(x=60, y=290,height=30)

        def update_entry():
            global hidden
            self.hidden = not self.hidden
            if self.hidden:
                e_mot_de_passe['show'] = '.'
                btn['image'] = hide
            else:
                e_mot_de_passe['show'] = ''
                btn['image'] = view

        self.hidden = True

        e_mot_de_passe = Entry(self.modal,width=20,show='.')
        e_mot_de_passe.place(x=300,y=290,height=30)
        e_cin = Entry(self.modal,width=20)
        e_cin.place(x=300, y=220,height=30)

        

        hide = ImageTk.PhotoImage(Image.open('hide.png').resize((20,20)))
        view = ImageTk.PhotoImage(Image.open('view.png').resize((20,20)))

        btn = Button(self.modal ,image=hide, bg='white',activebackground='white',bd=0,command=update_entry, borderwidth=0, highlightthickness=0)
        btn.place(x=440,y=293)
       

        # Ajouter un bouton "Fermer"
        Button(self.modal, text="Fermer", command=self.close_modal).place(x=350,y=348)
        Button(self.modal, text="Valider",background='#13c8f1',activebackground='#13c8f1', command=self.ajouter_employer).place(x=250,y=348)


        # Rendre la fenêtre modale modale
        self.modal.transient(parent)
        self.modal.grab_set()
        parent.wait_window(self.modal)

    def close_modal(self):
        self.modal.destroy()
 
    def ajouter_employer(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="threel"
        )
        nom = e_nom.get()
        prenoms = e_prenoms.get()
        date_naissance = e_date_naissance.get()
        sexe = e_sexe.get()
        cin = e_cin.get()
        telephone = e_telephone.get()
        adresse_email = e_adresse_email.get()
        mot_de_passe = e_mot_de_passe.get()
        try:
            with Image.open(self.photo_path, 'rb') as img:
                
                with io.BytesIO() as output:
                    img.save(output, format="PNG")
                    photo = output.getvalue()
        except AttributeError:
            messagebox.showerror("Erreur", "Veuillez sélectionner une photo.")
            return
        if not all([nom, prenoms, date_naissance, sexe, cin, telephone,photo, adresse_email, mot_de_passe]):
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
            return

        req = "INSERT INTO Liste_employers (Nom, Prénoms, Date_de_naissance, Sexe, Cin, Téléphone, Photo, Adresse_émail, Mot_de_passe) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor = conn.cursor()
        cursor.execute(req, (nom, prenoms, date_naissance, sexe, cin, telephone, photo, adresse_email, mot_de_passe))
        conn.commit()
        self.rein()
        messagebox.showinfo("Succès", "Employé ajouté avec succès.")
        conn.close()
    def rein(self):
        e_nom.delete(0, END)
        e_prenoms.delete(0, END)
        e_date_naissance.delete(0, END)
        e_sexe.delete(0, END)
        e_cin.delete(0, END)
        e_telephone.delete(0, END)
        e_adresse_email.delete(0, END)
        e_mot_de_passe.delete(0, END)


class ModalButton:
    def __init__(self,parent,title,bouton):
        self.parent = parent
        global e_valeur
        self.modal = Toplevel(parent)
        self.modal.title(title)
        self.modal.resizable(False,False)
        self.modal.geometry('400x100')

        e_valeur = Entry(self.modal,width=20)
        e_valeur.place(x=120, y=20,height=30)

        Button(self.modal, text="Valider",background='#13c8f1',activebackground='#13c8f1', command=bouton ).place(x=165,y=60)

        self.modal.transient(parent)
        self.modal.grab_set()
        parent.wait_window(self.modal)
        

    def close_modal(self):
        self.modal.destroy()


def ajouter_prix():
    conn=mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="threel"
    )
    cursors = conn.cursor()
    cursors.execute("SELECT Prix_m² FROM Prix_m²")
    results = cursors.fetchone()
    if conn.is_connected():
        e_valeur.get()
        cursors = conn.cursor()
        cursors.execute("SELECT Prix_m² FROM Prix_m²")
        results = cursors.fetchone()
        if results:
            valeur = results[0]
            e_prixmc.delete(0, "end")
            e_prixmc.insert(0, valeur)
            messagebox.showwarning("Avertissement", "Une valeur existe déjà dans la base de données. Veuillez d'abord supprimer cette valeur avant d'en ajouter une nouvelle.")
            e_valeur.delete(0, "end")
        else:
            req="INSERT INTO Prix_m² (Prix_m²)VALUES(%s)"
            cursor=conn.cursor()
            cursor.execute(req,(e_valeur.get(),))
            cursors.execute("SELECT Prix_m² FROM Prix_m²")
            results = cursors.fetchone()
            if results:
                valeur = results[0]
                e_prixmc.delete(0, "end")
                e_prixmc.insert(0, valeur)
            conn.commit()
            messagebox.showinfo("Succès", "La valeur a été ajoutée avec succès.")

            conn.close()
            e_valeur.delete(0, "end")
    else:
        print("Erreur lors d'insertion")

def ajouter_pourcentage():
    conn=mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="threel"
    )
    cursors = conn.cursor()
    cursors.execute("SELECT Pourcentage_1er_payement FROM Pourcentage_1er_payement")
    results = cursors.fetchone()
    if conn.is_connected():
        e = e_valeur.get()
        e_int = int(e)
        if e_int > 100:
            messagebox.showwarning("Erreur","le pourcentage doit inférieur ou égal à 100")
        else:
            cursors = conn.cursor()
            cursors.execute("SELECT Pourcentage_1er_payement FROM Pourcentage_1er_payement")
            results = cursors.fetchone()
            if results:
                valeur = results[0]
                e_ppayment.delete(0, "end")
                e_ppayment.insert(0, valeur)
                messagebox.showwarning("Avertissement", "Une valeur existe déjà dans la base de données. Veuillez d'abord supprimer cette valeur avant d'en ajouter une nouvelle.")
                e_valeur.delete(0, "end")
            else:
                req="INSERT INTO Pourcentage_1er_payement (Pourcentage_1er_payement)VALUES(%s)"
                cursor=conn.cursor()
                cursor.execute(req,(e_valeur.get(),))
                cursors.execute("SELECT Pourcentage_1er_payement FROM Pourcentage_1er_payement")
                results = cursors.fetchone()
                if results:
                    valeur = results[0]
                    e_ppayment.delete(0, "end")
                    e_ppayment.insert(0, valeur)
            conn.commit()
            messagebox.showinfo("Succès", "La valeur a été ajoutée avec succès.")

            conn.close()
            e_valeur.delete(0, "end")
    else:
        print("Erreur lors d'insertion")

def ajouter_tranche():
    conn=mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="threel"
    )
    cursors = conn.cursor()
    cursors.execute("SELECT Tranche_de_payement FROM Tranche_de_payement")
    results = cursors.fetchone()
    if conn.is_connected():
        e = e_valeur.get()
        e_int = int(e)
        if e_int>12:
            messagebox.showwarning("Erreur","le tranche doit inférieur ou égal à 12")
        else:
            cursors = conn.cursor()
            cursors.execute("SELECT Tranche_de_payement FROM Tranche_de_payement")
            results = cursors.fetchone()
            if results:
                valeur = results[0]
                e_tranche.delete(0, "end")
                e_tranche.insert(0, valeur)
                messagebox.showwarning("Avertissement", "Une valeur existe déjà dans la base de données. Veuillez d'abord supprimer cette valeur avant d'en ajouter une nouvelle.")
                e_valeur.delete(0, "end")
            else:
                req="INSERT INTO Tranche_de_payement (Tranche_de_payement)VALUES(%s)"
                cursor=conn.cursor()
                cursor.execute(req,(e_valeur.get(),))
                cursors.execute("SELECT Tranche_de_payement FROM Tranche_de_payement")
                results = cursors.fetchone()
                if results:
                    valeur = results[0]
                    e_tranche.delete(0, "end")
                    e_tranche.insert(0, valeur)
                conn.commit()
                messagebox.showinfo("Succès", "La valeur a été ajoutée avec succès.")

            conn.close()
            e_valeur.delete(0, "end")
    else:
        print("Erreur lors d'insertion")
def supprimer_valeur():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="threel"
    )
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT Prix_m² FROM Prix_m²")
        results = cursor.fetchone()

        if results is None:
            messagebox.showwarning("Erreur","Il n'y a aucun élément")
        else:
            cursor.execute("DELETE Prix_m² FROM Prix_m²")
            e_prixmc.delete(0, "end")
            messagebox.showinfo("Succès", "La valeur a été supprimer avec succès.")
        conn.commit()

        conn.close()
def supprimer_valeur_pourcentage():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="threel"
    )
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT Pourcentage_1er_payement FROM Pourcentage_1er_payement")
        results = cursor.fetchone()

        if results is None:
            messagebox.showwarning("Erreur","Il n'y a aucun élément")
        else:
            cursor.execute("DELETE Pourcentage_1er_payement FROM Pourcentage_1er_payement")
            e_ppayment.delete(0, "end")
            messagebox.showinfo("Succès", "La valeur a été supprimer avec succès.")
        conn.commit()

        conn.close()
def supprimer_valeur_tranche():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="threel"
    )
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT Tranche_de_payement FROM Tranche_de_payement")
        results = cursor.fetchone()

        if results is None:
            messagebox.showwarning("Erreur","Il n'y a aucun élément")
        else:
            cursor.execute("DELETE Tranche_de_payement FROM Tranche_de_payement")
            e_tranche.delete(0, "end")
            messagebox.showinfo("Succès", "La valeur a été supprimer avec succès.")
        conn.commit()

        conn.close()

def show_modal():
    Modal(admin,'Ajouter un employer')
def show_modal_edit():
    Modal(admin,"Modifier l'information de l'employé")
def show_modal_add_price():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="threel"
    )
    cursors = conn.cursor()
    cursors.execute("SELECT Prix_m² FROM Prix_m²")
    results = cursors.fetchone()
    if results:
            messagebox.showwarning("Avertissement", "Une valeur existe déjà dans la base de données. Veuillez d'abord supprimer cette valeur avant d'en ajouter une nouvelle.")
    else:
        ModalButton(admin,"Ajouter le prix en m²",ajouter_prix)
    conn.close()
    
def show_modal_add_first_price_percent():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="threel"
    )
    cursors = conn.cursor()
    cursors.execute("SELECT Pourcentage_1er_payement FROM Pourcentage_1er_payement")
    results = cursors.fetchone()
    if results:
            messagebox.showwarning("Avertissement", "Une valeur existe déjà dans la base de données. Veuillez d'abord supprimer cette valeur avant d'en ajouter une nouvelle.")
    else:
        ModalButton(admin,"Ajouter le pourcentage du 1er payments",ajouter_pourcentage)
    conn.close()
    
def show_modal_tranche_payement():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="threel"
    )
    cursors = conn.cursor()
    cursors.execute("SELECT Tranche_de_payement FROM Tranche_de_payement")
    results = cursors.fetchone()
    if results:
            messagebox.showwarning("Avertissement", "Une valeur existe déjà dans la base de données. Veuillez d'abord supprimer cette valeur avant d'en ajouter une nouvelle.")
    else:
        ModalButton(admin,"Ajouter le tranche de payments",ajouter_tranche)
    conn.close()

class Admin:
    def __init__(self,admin):
        global e_prixmc
        global e_tranche
        global e_ppayment
        
        canvas = Canvas( admin, width=1000, height=640, background='#043737')
        canvas.place(x=0,y=0)

        frame = Frame( admin,width=990,height=55, background='#3d8a8a')
        frame.place(x=5,y=10)
        self.mess = ImageTk.PhotoImage(Image.open('./icones/messager.png').resize((30,30)))
        self.btn_mess = Button(frame ,image= self.mess,bd=0,background='#3d8a8a',activebackground='#3d8a8a', borderwidth=0, highlightthickness=0)
        self.btn_mess.place(x=800,y=10)
        self.notif = ImageTk.PhotoImage(Image.open('./icones/cloche.png').resize((30,30)))
        self.btn_notif = Button(frame ,image= self.notif,bd=0,background='#3d8a8a',activebackground='#3d8a8a', borderwidth=0, highlightthickness=0)
        self.btn_notif.place(x=850,y=10)
        self.profil = ImageTk.PhotoImage(Image.open('./icones/avatar-homme.png').resize((50,50)))
        self.btn_profil = Button(frame ,image= self.profil,bd=0,background='#3d8a8a',activebackground='#3d8a8a', borderwidth=0, highlightthickness=0)
        self.btn_profil.place(x=920,y=2)

        self.greeting = Label(frame,text="Bienvenue ....",fg='white', font='calibri 20 bold',background='#3d8a8a')
        self.greeting.place(x=10,y=7)
        
        #leftside

        self.info = Label( admin, text='Info peintures',fg='white', font='calibri 18 bold',background='#043737')
        self.info.place(x=190,y=110)

        frame1 = Frame( admin,width=400, height=400)
        frame1.place(x=70, y=150)

        self.prixmc = Label(frame1, text="Prix en m²:", font='calibri 16 bold')
        self.prixmc.place(x=10,y=25)
        e_prixmc = Entry(frame1, width=7,font='calibri 16 bold')
        e_prixmc.place(x=115,y=25,height=35)
        self.devise = Label(frame1, text="MGA", font='calibri 13 bold')
        self.devise.place(x=210,y=28)
        self.ajouter1 = Label(frame1, text='Ajouter',activebackground='white')
        self.ajouter1.place(x=260,y=43)
        self.ajout1 = ImageTk.PhotoImage(Image.open('./icones/plus.png').resize((20,20)))
        self.btn_a1 = Button(frame1 ,image= self.ajout1,bd=0, borderwidth=0, highlightthickness=0,command=show_modal_add_price)
        self.btn_a1.place(x=275,y=25)
        self.sup1 = Label(frame1, text='Supprimer')
        self.sup1.place(x=320,y=43)
        self.supp = ImageTk.PhotoImage(Image.open('./icones/supprimer.png').resize((20,20)))
        self.btn_s1 = Button(frame1 ,image= self.supp,bd=0, borderwidth=0, highlightthickness=0,command=supprimer_valeur)
        self.btn_s1.place(x=345,y=25)
        
        self.tranche = Label(frame1, text="Tranche de \n payements", font='calibri 16 bold')
        self.tranche.place(x=10,y=145)
        e_tranche = Entry(frame1, width=5,font='calibri 16 bold')
        e_tranche.place(x=125,y=155,height=35)
        self.delai = Label(frame1, text="Mois", font='calibri 13 bold')
        self.delai.place(x=190,y=158)
        self.ajoute = Label(frame1, text='Ajouter',activebackground='white')
        self.ajoute.place(x=260,y=173)
        self.ajou = ImageTk.PhotoImage(Image.open('./icones/plus.png').resize((20,20)))
        self.bt = Button(frame1 ,image= self.ajou,bd=0, borderwidth=0, highlightthickness=0,command=show_modal_tranche_payement)
        self.bt.place(x=275,y=155)
        self.su = Label(frame1, text='Supprimer')
        self.su.place(x=320,y=173)
        self.suppp = ImageTk.PhotoImage(Image.open('./icones/supprimer.png').resize((20,20)))
        self.btn_s1 = Button(frame1 ,image= self.suppp,bd=0, borderwidth=0, highlightthickness=0,command=supprimer_valeur_tranche)
        self.btn_s1.place(x=345,y=155)

        self.ppayment = Label(frame1, text="Pourcentage \n 1er payement", font='calibri 16 bold')
        self.ppayment.place(x=3,y=75)
        e_ppayment = Entry(frame1, width=5,font='calibri 16 bold')
        e_ppayment.place(x=145,y=85,height=35)
        self.percent = Label(frame1, text="%", font='calibri 13 bold')
        self.percent.place(x=210,y=88)
        self.ajouter2 = Label(frame1, text='Ajouter',activebackground='white')
        self.ajouter2.place(x=260,y=103)
        self.ajout2 = ImageTk.PhotoImage(Image.open('./icones/plus.png').resize((20,20)))
        self.btn_a2 = Button(frame1 ,image= self.ajout2,bd=0, borderwidth=0, highlightthickness=0,command=show_modal_add_first_price_percent)
        self.btn_a2.place(x=275,y=85)
        self.sup2 = Label(frame1, text='Supprimer')
        self.sup2.place(x=320,y=103)
        self.supp1 = ImageTk.PhotoImage(Image.open('./icones/supprimer.png').resize((20,20)))
        self.btn_s2 = Button(frame1 ,image= self.supp1,bd=0, borderwidth=0, highlightthickness=0,command=supprimer_valeur_pourcentage)
        self.btn_s2.place(x=345,y=85)
        try:
            conns = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="threel"
            )
            cursorss = conns.cursor()
            cursorss.execute("SELECT Prix_m² FROM Prix_m² ")
            resultss = cursorss.fetchone()

            if resultss:
                valeur = resultss[0]
                e_prixmc.insert(0, valeur)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        try:
            conns = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="threel"
            )
            cursorss = conns.cursor()
            cursorss.execute("SELECT Pourcentage_1er_payement FROM Pourcentage_1er_payement")
            resultss = cursorss.fetchone()

            if resultss:
                valeur = resultss[0]
                e_ppayment.insert(0, valeur)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        try:
            conns = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="threel"
            )
            cursorss = conns.cursor()
            cursorss.execute("SELECT Tranche_de_payement FROM Tranche_de_payement ")
            resultss = cursorss.fetchone()

            if resultss:
                valeur = resultss[0]
                e_tranche.insert(0, valeur)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        #rightside

        self.employers = Label( admin, text='Liste employers',fg='white', font='calibri 18 bold',background='#043737')
        self.employers.place(x=640,y=110)

        frame2 = Frame( admin,width=400, height=400)
        frame2.place(x=530, y=150)
        result_f = Frame(frame2, bd=5, relief=GROOVE)
        result_f.place(x=3,y=5,width=389,height=390)

        scrol_x = Scrollbar(result_f,orient=HORIZONTAL)
        scrol_y = Scrollbar(result_f,orient=VERTICAL)
        self.tabl = ttk.Treeview(result_f,columns=('id','nom','prénoms','date','sexe','cin','téléphone','photo','adresse_mail','mot_de_passe'),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set )

        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)

        self.tabl.heading('id', text='Id employer')
        self.tabl.heading('nom', text='Nom')
        self.tabl.heading('prénoms', text='Prénoms')
        self.tabl.heading('date', text='Date de naissance')
        self.tabl.heading('sexe', text='Sexe')
        self.tabl.heading('cin', text='Cin')
        self.tabl.heading('téléphone', text='Téléphone')
        self.tabl.heading('photo', text='Photo')
        self.tabl.heading('adresse_mail', text='Adresse émail')
        self.tabl.heading('mot_de_passe', text='Mot de passe')


        self.tabl["show"]="headings"

        self.tabl.column('id', width=100)
        self.tabl.column('nom', width=150)
        self.tabl.column('prénoms', width=150)
        self.tabl.column('date', width=150)
        self.tabl.column('sexe', width=150)
        self.tabl.column('cin', width=150)
        self.tabl.column('téléphone', width=150)
        self.tabl.column('photo', width=150)
        self.tabl.column('adresse_mail', width=150)
        self.tabl.column('mot_de_passe', width=150)






        self.tabl.place(x=0,width=365,height=365)
        scrol_x.config(command=self.tabl.xview)
        scrol_y.config(command=self.tabl.yview)

        self.tabl.bind("<ButtonRelease-1")


        #boutonlabel

        self.ajouter = Label(admin, text='Ajouter',fg='white',background='#043737')
        self.ajouter.place(x=570,y=560)
        self.ajout = ImageTk.PhotoImage(Image.open('./icones/plus.png').resize((20,20)))
        self.btn_a = Button( admin ,image= self.ajout,bd=0,background='#043737',activebackground='#043737', borderwidth=0, highlightthickness=0,command=show_modal)
        self.btn_a.place(x=627,y=560)



        self.modifier = Label( admin, text='Modifier',fg='white',background='#043737')
        self.modifier.place(x=690,y=560)
        self.modif = ImageTk.PhotoImage(Image.open('./icones/stylo.png').resize((20,20)))
        self.btn_m = Button( admin ,image= self.modif,bd=0,background='#043737',activebackground='#043737', borderwidth=0, highlightthickness=0,command=show_modal_edit)
        self.btn_m.place(x=753,y=560)
        self.supprimer = Label( admin, text='Supprimer',fg='white',background='#043737', borderwidth=0, highlightthickness=0)
        self.supprimer.place(x=810,y=560)
        self.sup = ImageTk.PhotoImage(Image.open('./icones/supprimer.png').resize((20,20)))
        self.btn_s = Button( admin ,image= self.sup,bd=0,background='#043737',activebackground='#043737', borderwidth=0, highlightthickness=0)
        self.btn_s.place(x=885,y=560)

        self.btn_s = Button( admin ,text="Formulaire Client",bd=0,background='red',activebackground='#ffffff', highlightthickness=0)
        self.btn_s.place(x=70,y=560)

admin = Tk()
admin.title('Admin')
admin.geometry('1000x640')
admin.resizable(False,False)
obj = Admin(admin)

admin.mainloop()