from tkinter import *
from tkinter import ttk

class Index:
    def __init__(self,root):
        WIDTH = 420
        HEIGHT = 500
        fs = "10"


        canvas = Canvas(root, width=1000, height=640,background='#012a2f')
        canvas.pack()

        #Frame_formulaire
        frame = Frame(root, background='#2353cc',width=WIDTH, height=HEIGHT, bd=5,relief=GROOVE)
        frame.place(x=15,y=90)

        def calcul_mesure(*args):
            try:
                value1 = float(self.e_mesure_trano.get())
                value2 = float(self.s_tranche_payement.get())
                prix_m2 = 5000
                prixTotl = (value1*prix_m2)
                pr = 40
                pv = ((prixTotl*pr)/100)
                rs = (prixTotl-pv)
                pt = (rs/(value2-1))
                self.result_label.config(text=f"Prix Total : {prixTotl} Ar", background='red')
                self.result_label1.config(text=f"1er payements : {pv} Ar", background='black',fg='white')
                self.result_label2.config(text=f"Reste à payer : {rs} Ar")
            except ValueError:
                self.result_label.config(text="Prix Total :" ,background='red')
                self.result_label1.config(text="1er payements :", background='black', fg='white')
                self.result_label2.config(text="Reste à payer :")
                

        #  #Variables
        # self.nom = StringVar()
        # self.prenoms = StringVar()
        # self.date_naissance = StringVar()
        # self.sexe = StringVar()
        # self.cin = StringVar()
        # self.telephone = StringVar()
        # self.photo = StringVar()
        # self.id_employer = StringVar()
        # self.label_mesure_trano = StringVar()
        # self.label_tranche_payement = StringVar()
        


        #Label_formulaire
        self.nom = Label(frame, text="Nom: ",bg='#2353cc',font=("calibri",fs))
        self.prenoms = Label(frame, text="Prénoms: ", bg='#2353cc',font=("calibri",fs))
        self.date_naissance = Label(frame, text="Date de naissance: ", bg='#2353cc',font=("calibri",fs))
        self.sexe = Label(frame, text="Sexe: ", bg='#2353cc',font=("calibri",fs))
        self.cin = Label(frame, text="CIN: ", bg='#2353cc',font=("calibri",fs))
        self.adresse = Label(frame, text="Adrèsse: ", bg='#2353cc',font=("calibri",fs))
        self.telephone = Label(frame, text="Téléphone: ", bg='#2353cc',font=("calibri",fs))
        self.photo = Label(frame, text="Photo: ", bg='#2353cc',font=("calibri",fs))
        self.id_employer = Label(frame, text="Id employer: ", bg='#2353cc',font=("calibri",fs))
        self.mesure_trano = Label(frame, text="Mésure trano: ", bg='#2353cc',font=("calibri",fs))
        self.label_mesure_trano = Label(frame, text="m² ", bg='#2353cc',font=("calibri",12))
        self.tranche_payement = Label(frame, text="Tranche de payement: ", bg='#2353cc',font=("calibri",fs))
        self.label_tranche_payement = Label(frame, text="Mois ", bg='#2353cc',font=("calibri",12))

        self.nom.place(x=10, y=100)
        self.prenoms.place(x=200, y=100)
        self.date_naissance.place(x=10, y=150)
        self.sexe.place(x=200, y=150)
        self.cin.place(x=10, y=200)
        self.adresse.place(x=200, y=200)
        self.telephone.place(x=10, y=250)
        self.photo.place(x=200, y=250)
        self.id_employer.place(x=10, y=300)
        self.mesure_trano.place(x=10, y=350)
        self.tranche_payement.place(x=200, y=350)

        #Entry_formulaire/autre widgets
        self.e_nom = Entry(frame,textvariable=self.nom, width=17)
        self.e_prenoms = Entry(frame,textvariable=self.prenoms, width=15)
        self.c_date_naissance = Entry(frame,textvariable=self.date_naissance, width=8)
        self.l_sexe = ttk.Combobox(frame ,textvariable=self.sexe, width=14,state="readonly")
        self.l_sexe['background']='red'
        self.l_sexe["values"]=("Homme","Femme")
        self.l_sexe.current(0)
        self.e_cin = Entry(frame ,textvariable=self.cin, width=17)
        self.e_adresse = Entry(frame ,textvariable=self.adresse, width=15)
        self.e_telephone = Entry(frame ,textvariable=self.telephone, width=13)
        self.e_photo = Entry(frame ,textvariable=self.photo, width=15)
        self.e_employer = Entry(frame ,textvariable=self.id_employer, width=12)
        self.e_mesure_trano = Entry(frame, width=5)
        self.s_tranche_payement = Entry(frame , width=3)

        self.e_mesure_trano.bind("<KeyRelease>", calcul_mesure)
        self.s_tranche_payement.bind("<KeyRelease>", calcul_mesure)

        self.result_label = Label(frame, text="Prix Total :", background='red')
        self.result_label1 = Label(frame, text="1er payements :", background='black',fg='white')
        self.result_label2 = Label(frame, text="Reste à payer :")
        # self.result_label3 = Label(frame, text="Prix Total :")
        # self.result_label4 = Label(frame, text="Prix Total :")

        

        self.result_label.place(x=10,y=400)
        self.result_label1.place(x=10,y=430)
        self.result_label2.place(x=10,y=460)
        # self.result_label3.place(x=10,y=400)
        # self.result_label4.place(x=10,y=400)

        self.e_nom.place(x=50,y=100)
        self.e_prenoms.place(x=260,y=100)
        self.c_date_naissance.place(x=120,y=150)
        self.l_sexe.place(x=260,y=150)
        self.e_cin.place(x=50,y=200)
        self.e_adresse.place(x=260,y=200)
        self.e_telephone.place(x=80,y=250)
        self.e_photo.place(x=260,y=250)
        self.e_employer.place(x=90,y=300)
        self.e_mesure_trano.place(x=100,y=350)
        self.label_mesure_trano.place(x=150,y=350)
        self.s_tranche_payement.place(x=330,y=350)
        self.label_tranche_payement.place(x=370,y=350)

        #bouton


        Details_Frame = Frame(root, bd=3, relief=GROOVE, bg="#2353cc")
        Details_Frame.place(x=480,y=90, width=500,height=500)

        affiche_resultat = Label(Details_Frame, text="Rechercher par",font=("times new roman", 8),bd=5,relief=GROOVE,bg="gray")
        affiche_resultat.place(x=7,y=15)
        rech = ttk.Combobox(Details_Frame,background='red', font=("times new roman", 13),state="readonly")
        rech["values"]=("id","nom","id employer")
        rech.place(x=97, y=16, width=110, height=23)
        rech_txt = Entry(Details_Frame,font=("times new roman", 11),bd=2,relief=GROOVE)
        rech_txt.place(x=212,y=16,width=120,height=23)
        btn_rech = Button(Details_Frame,text="Rechercher",font=("times new roman", 8),bd=3,bg="gray",relief=GROOVE)
        btn_rech.place(x=337,y=16,width=70,height=23)
        btn_afftou = Button(Details_Frame,text="Afficher Tous",font=("times new roman", 8),bd=3,bg="gray",relief=GROOVE)
        btn_afftou.place(x=412,y=16,width=75,height=23)


        #Affichage

        result_frame = Frame(Details_Frame, bd=5, relief=GROOVE, bg="#2353cc")
        result_frame.place(x=3,y=50,width=487,height=400)

        scrol_x = Scrollbar(result_frame,orient=HORIZONTAL)
        scrol_y = Scrollbar(result_frame,orient=VERTICAL)
        self.tabl_resul = ttk.Treeview(result_frame, columns=('id','nom','prénoms','date','sexe','cin','adresse','téléphone','photo','id_e','mesure_trano','tranche','total','1er'),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set )

        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)

        self.tabl_resul.heading('id', text='Id')
        self.tabl_resul.heading('nom', text='Nom')
        self.tabl_resul.heading('prénoms', text='Prénoms')
        self.tabl_resul.heading('date', text='Date de naissance')
        self.tabl_resul.heading('sexe', text='Sexe')
        self.tabl_resul.heading('cin', text='Cin')
        self.tabl_resul.heading('adresse', text='Adresse')
        self.tabl_resul.heading('téléphone', text='Téléphone')
        self.tabl_resul.heading('photo', text='Photo')
        self.tabl_resul.heading('id_e', text='Id employer')
        self.tabl_resul.heading('mesure_trano', text='Mesure_Trano')
        self.tabl_resul.heading('tranche', text='Tranche de Payement')
        self.tabl_resul.heading('total', text='Prix total')
        self.tabl_resul.heading('1er', text='1er Versement')

        self.tabl_resul["show"]="headings"

        self.tabl_resul.column('id', width=50)
        self.tabl_resul.column('nom', width=150)
        self.tabl_resul.column('prénoms', width=150)
        self.tabl_resul.column('date', width=150)
        self.tabl_resul.column('sexe', width=150)
        self.tabl_resul.column('cin', width=150)
        self.tabl_resul.column('adresse', width=150)
        self.tabl_resul.column('téléphone', width=150)
        self.tabl_resul.column('photo', width=150)
        self.tabl_resul.column('id_e', width=150)
        self.tabl_resul.column('mesure_trano', width=150)
        self.tabl_resul.column('tranche', width=150)
        self.tabl_resul.column('total', width=150)
        self.tabl_resul.column('1er', width=150)





        self.tabl_resul.place(x=0,width=465,height=377)
        scrol_x.config(command=self.tabl_resul.xview)
        scrol_y.config(command=self.tabl_resul.yview)

        self.tabl_resul.bind("<ButtonRelease-1")

       
root=Tk()
root.title("Three L")
root.geometry("1000x640")
root.resizable(False, False)
obj = Index(root)
root.mainloop()