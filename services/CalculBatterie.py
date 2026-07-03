from models.PeriodeJ import PeriodeJ
from models.Materielle import Materielle
from datetime import datetime, timedelta, time

class CalculBatterie:

    @staticmethod
    def calcul():
        puissance = 0.0

        periode = PeriodeJ.getById(3)
        if periode is None:
            print("Période Nuit introuvable.")
            return puissance
            
        materielles = Materielle.getByIdperiode(3)
        
        def time_to_hours(t):
            return t.hour + t.minute / 60.0 + t.second / 3600.0

        for materielle in materielles:
            h_start = time_to_hours(materielle.debutH)
            h_end = time_to_hours(materielle.finH)
            
            duree = h_end - h_start
            if duree < 0:
                duree += 24.0 
                
            puissance += duree * float(materielle.consomation)

        print("Puissance totale consommée (Nuit) :", puissance)
        return puissance

    @staticmethod
    def calculpanneau2(puissance):
        puissance = (puissance*0.3)/0.2
        return puissance
