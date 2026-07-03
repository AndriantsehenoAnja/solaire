import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from models.Materielle import Materielle
from models.Panneau import Panneau


class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Insertion")
        self.root.geometry("800x600")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        self.tab_materielle = ttk.Frame(self.notebook)
        self.tab_panneau = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_materielle, text="Matérielles")
        self.notebook.add(self.tab_panneau, text="Panneaux")

        self.setup_materielle_tab()
        self.setup_panneau_tab()

    def setup_materielle_tab(self):
        root = self.tab_materielle
        
        # ===== ID =====
        tk.Label(root, text="ID").pack()
        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        # ===== DATE DEBUT =====
        tk.Label(root, text="Début (HH:MM:SS)").pack()
        self.debut_entry = tk.Entry(root)
        self.debut_entry.pack()

        # ===== DATE FIN =====
        tk.Label(root, text=" Fin (HH:MM:SS)").pack()
        self.fin_entry = tk.Entry(root)
        self.fin_entry.pack()

        # ===== MATERIELLE =====
        tk.Label(root, text="Matérielle").pack()

        self.materielle = ttk.Entry(root)
        self.materielle.pack()

        #===== consomation =====
        tk.Label(root, text="Consomation").pack()
        self.consomation = ttk.Entry(root)
        self.consomation.pack()
                
        # ===== BUTTON =====
        tk.Button(root, text="Insérer Matérielle", command=self.insert).pack(pady=10)
        tk.Button(root, text="voir résultats", command=self.resultat).pack(pady=5)
        # =========================
        # 📊 TABLEAU UTILISATIONS
        # =========================
        self.table = ttk.Treeview(root, columns=("id", "materielle", "debut", "fin","consomation"), show="headings")

        self.table.heading("id", text="ID")
        self.table.heading("materielle", text="Matérielle")
        self.table.heading("debut", text="Début")
        self.table.heading("fin", text="Fin")
        self.table.heading("consomation", text="Consomation")

        self.table.pack(fill="both", expand=True, pady=20)
        self.load_Materielle()
        
    def setup_panneau_tab(self):
        root = self.tab_panneau
        
        # ===== ID =====
        tk.Label(root, text="ID").pack()
        self.panneau_id_entry = tk.Entry(root)
        self.panneau_id_entry.pack()

        # ===== NAME =====
        tk.Label(root, text="Nom du Panneau").pack()
        self.panneau_name = tk.Entry(root)
        self.panneau_name.pack()

        # ===== CONSOMATION =====
        tk.Label(root, text="Consommation").pack()
        self.panneau_consomation = ttk.Entry(root)
        self.panneau_consomation.pack()
        
        # ===== COEF =====
        tk.Label(root, text="Coefficient").pack()
        self.panneau_coef = ttk.Entry(root)
        self.panneau_coef.pack()
        
        # ===== PRIX =====
        tk.Label(root, text="Prix").pack()
        self.panneau_prix = ttk.Entry(root)
        self.panneau_prix.pack()
                
        # ===== BUTTON =====
        tk.Button(root, text="Insérer Panneau", command=self.insert_panneau).pack(pady=10)
        
        # =========================
        # 📊 TABLEAU PANNEAUX
        # =========================
        self.panneau_table = ttk.Treeview(root, columns=("id", "name", "consomation", "coef", "prix"), show="headings")

        self.panneau_table.heading("id", text="ID")
        self.panneau_table.heading("name", text="Nom")
        self.panneau_table.heading("consomation", text="Consommation")
        self.panneau_table.heading("coef", text="Coefficient")
        self.panneau_table.heading("prix", text="Prix")

        self.panneau_table.pack(fill="both", expand=True, pady=20)
        self.load_Panneau()

    def load_Panneau(self):
        panneau_list = Panneau.findAll()
        self.panneau_table.delete(*self.panneau_table.get_children())

        for p in panneau_list:
            self.panneau_table.insert("", "end", values=(
                p.id,
                p.name,
                p.consomation,
                p.coef,
                p.prix
            ))

    def insert_panneau(self):
        try:
            p = Panneau(
                id=int(self.panneau_id_entry.get()),
                name=self.panneau_name.get(),
                consomation=float(self.panneau_consomation.get()),
                coef=float(self.panneau_coef.get()),
                prix=float(self.panneau_prix.get())
            )

            if Panneau.insert_Panneau(p):
                messagebox.showinfo("Succès", "Insertion réussie")
                self.clear_panneau()
                self.load_Panneau()

            else:
                messagebox.showerror("Erreur", "Insertion échouée")

        except Exception as e:
            messagebox.showerror("Erreur", str(e))
            
    def clear_panneau(self):
        self.panneau_id_entry.delete(0, tk.END)
        self.panneau_name.delete(0, tk.END)
        self.panneau_consomation.delete(0, tk.END)
        self.panneau_coef.delete(0, tk.END)
        self.panneau_prix.delete(0, tk.END)

    # ===== RESULTATS =====
    def resultat(self):
        from services.CalculPanneaux import CalculPanneaux
        from services.CalculBatterie import CalculBatterie
        from models.Panneau import Panneau

        batterie_conso = round( CalculBatterie.calcul()+(CalculBatterie.calcul()*0.5),4)
        pinck = round( CalculPanneaux.getpinck())
        puissance_tsyniasa = CalculPanneaux.calculWavendre()
        # volaVarotra = CalculPanneaux.calculeVolaM()
        jourOvrable = CalculPanneaux.calculWavendrealea(35,190)
        jourFermer = CalculPanneaux.calculWavendrealea(40,210)

        msg = f"ETU:004370\n\npick: {pinck} W\npuissance restant :{puissance_tsyniasa}W\nJour Ouvrable :{jourOvrable} ariary\nWeekend :{jourFermer} ariary\n"

        panneaux_list = Panneau.findAll()
        # for p in panneaux_list:
        #     # On calcule la puissance via findMax avec la consommation du panneau
        #     puissance_requise = CalculPanneaux.findMax(p.coef)
        #     nombre_prix = CalculPanneaux.getnombreprix(p.id, puissance_requise)

        #     msg += f"- {p.name} (puissance totale: {round((puissance_requise),2)} W,\n Prix U: {p.prix}, \nConso: {p.consomation}W) \n=> Coût Total : {round(nombre_prix, 2)} Ar\n\n"

        messagebox.showinfo("Résultats", msg)
    # ===== CHARGER MATERIEL =====
    def load_Materielle(self):
        materielle_list = Materielle.findAll()
        self.table.delete(*self.table.get_children())

        for m in materielle_list:
            self.table.insert("", "end", values=(
                m.id,
                m.name,
                m.debutH,
                m.finH,
                m.consomation
            ))

    # ===== INSERT =====
    def insert(self):
        try:
            
            u = Materielle(
                id=int(self.id_entry.get()),
                name=self.materielle.get(),
                debutH=self.debut_entry.get(),
                finH=self.fin_entry.get(),
                consomation=self.consomation.get()
            )

            if Materielle.insert_Materielle(u):
                messagebox.showinfo("Succès", "Insertion réussie")
                self.clear()
                self.load_Materielle()   # 🔥 refresh table

            else:
                messagebox.showerror("Erreur", "Insertion échouée")

        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    # ===== RESET =====
    def clear(self):
        self.id_entry.delete(0, tk.END)
        self.debut_entry.delete(0, tk.END)
        self.fin_entry.delete(0, tk.END)