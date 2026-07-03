import tkinter as tk
from models.Materielle import Materielle
from models.PeriodeJ import PeriodeJ
from services.CalculBatterie import CalculBatterie
from view.App import App

class Main:
    def run(self):
        # for materielle in Materielle.findAll():
        #     print(materielle)

        for materielle in Materielle.getByIdperiode(1):
            print(materielle)
        for materielle in Materielle.getByIdperiode(2):
            print(materielle)
        print(CalculBatterie.calcul())
if __name__ == "__main__":
    main = Main()
    main.run()
    root = tk.Tk()
    app = App(root)
    root.mainloop()
