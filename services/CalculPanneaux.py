from models.Materielle import Materielle
from services.CalculBatterie import CalculBatterie
from datetime import datetime, timedelta,time
from models.Panneau import Panneau
from models.Jours import Jours
import math
class CalculPanneaux:
    def getnombreprix(idpanneaux, puissance):
        panneau = Panneau.getById(idpanneaux)
        return math.ceil((float(puissance)/float(panneau.consomation))) * float(panneau.prix)
    def findMax(panneaux):
        div = float(panneaux)/100
        bateriele = CalculBatterie.calcul()
        
        max1 = 0.0
        max2 = 0.0
        
        materielles1 = Materielle.getByIdperiode(1)
        materielles2 = Materielle.getByIdperiode(2)
        
        debut1 = time(6,0,0)
        fin1 = time(17,0,0)
        
        debut2 = time(17,0,0)
        fin2 = time(19,0,0)
        
        current = datetime.combine(datetime.today(), debut1)
        end = datetime.combine(datetime.today(), fin1)

        while current < end:
            t = current.time()  # revenir en time

            stock = 0.0
            for materielle1 in materielles1:
                if materielle1.debutH <= t < materielle1.finH:
                    stock += float(materielle1.consomation)

            max1 = max(max1, stock)

            current += timedelta(minutes=1)
        
        current = datetime.combine(datetime.today(), debut2)
        end = datetime.combine(datetime.today(), fin2)

        while current < end:
            t = current.time()

            stock = 0.0
            for materielle2 in materielles2:
                if materielle2.debutH <= t < materielle2.finH:
                    stock += float(materielle2.consomation)

            max2 = max(max2, stock)

            current += timedelta(minutes=1)

        max1 += ((bateriele*1.5)/12)
        max2 += ((bateriele*1.5)/12)
        
        # max(max1,max2)*
        return max((max1/div),(max2/(div*0.5)))

    def getpinck():
        # bateriele = CalculBatterie.calcul()
        
        max1 = 0.0
        max2 = 0.0
        # max3 = 0.0
        materielles1 = Materielle.getByIdperiode(1)
        materielles2 = Materielle.getByIdperiode(2)
        # materielles3 = Materielle.getByIdperiode(3)
        
        debut1 = time(6,0,0)
        fin1 = time(17,0,0)
        
        debut2 = time(17,0,0)
        fin2 = time(19,0,0)
        
        # debut3 = time(19,0,0)
        # fin3 = time(6,0,0)
        
        current = datetime.combine(datetime.today(), debut1)
        end = datetime.combine(datetime.today(), fin1)

        while current < end:
            t = current.time()  # revenir en time

            stock = 0.0
            for materielle1 in materielles1:
                if materielle1.debutH <= t < materielle1.finH:
                    stock += float(materielle1.consomation)

            max1 = max(max1, stock)

            current += timedelta(minutes=1)
        
        current = datetime.combine(datetime.today(), debut2)
        end = datetime.combine(datetime.today(), fin2)

        while current < end:
            t = current.time()

            stock = 0.0
            for materielle2 in materielles2:
                if materielle2.debutH <= t < materielle2.finH:
                    stock += float(materielle2.consomation)

            max2 = max(max2, stock)

            current += timedelta(minutes=1)

        # current = datetime.combine(datetime.today(), debut3)
        # end = datetime.combine(datetime.today()+timedelta(days=1), fin3)

        # while current < end:
        #     t = current.time()

        #     stock = 0.0
        #     for materielle3 in materielles3:
        #         if materielle3.debutH <= materielle3.finH:
        #             if materielle3.debutH <= t < materielle3.finH:
        #                 stock += float(materielle3.consomation)
        #         else:
        #             if t >= materielle3.debutH or t <= materielle3.finH:
        #                 stock += float(materielle3.consomation)

        #     max3 = max(max3,stock)
            

            # current += timedelta(minutes=1)

        # max1 +=  (bateriele/13)
        # max2 +=  (bateriele/13)
		
        return max(max1, max2*2)

    def calculWavendrealea(pourcetagepoint,prix):
        maxW = CalculPanneaux.getpinck()
        pui1 = 0.0 #sans pointe
        pui2 = 0.0 #avec pointe
        materielles1 = Materielle.getByIdperiode(1)
        materielles2 = Materielle.getByIdperiode(2)
        
        debut1 = time(6,0,0)
        fin1 = time(12,0,0)
        debut11 = time(14,0,0)
        fin11 = time(17,0,0)
        
        debut2 = time(17,0,0)
        fin2 = time(19,0,0)
        
        debut3 = time(12,0,0)
        fin3 = time(14,0,0)
        
        current = datetime.combine(datetime.today(), debut1)
        end = datetime.combine(datetime.today(), fin1)

        while current < end:
            t = current.time()  # revenir en time

            stock = 0.0
            for materielle1 in materielles1:
                if materielle1.debutH <= t < materielle1.finH:
                    stock += float(materielle1.consomation)

            pui1 += float(maxW-stock)

            current += timedelta(hours=1)

        current = datetime.combine(datetime.today(), debut11)
        end = datetime.combine(datetime.today(), fin11)

        while current < end:
            t = current.time()  # revenir en time

            stock = 0.0
            for materielle1 in materielles1:
                if materielle1.debutH <= t < materielle1.finH:
                    stock += float(materielle1.consomation)

            pui1 += float(maxW-stock)

            current += timedelta(hours=1)
        
        
        
        current = datetime.combine(datetime.today(), debut2)
        end = datetime.combine(datetime.today(), fin2)

        while current < end:
            t = current.time()  # revenir en time

            stock = 0.0
            for materielle2 in materielles2:
                if materielle2.debutH <= t < materielle2.finH:
                    stock += float(materielle2.consomation)

            pui2+= float((maxW/2)-stock)

            current += timedelta(hours=1)

        current = datetime.combine(datetime.today(), debut3)
        end = datetime.combine(datetime.today(), fin3)

        while current < end:
            t = current.time()  # revenir en time

            stock = 0.0
            for materielle1 in materielles1:
                if materielle1.debutH <= t < materielle1.finH:
                    stock += float(materielle1.consomation)

            pui2+= float((maxW)-stock)

            current += timedelta(hours=1)
        
        return (pui1*prix+pui2*(prix+(pourcetagepoint*prix/100)))
    
    def calculWavendre():
        maxW = CalculPanneaux.getpinck()
        pui1 = 0.0
        pui2 = 0.0
        materielles1 = Materielle.getByIdperiode(1)
        materielles2 = Materielle.getByIdperiode(2)
        
        debut1 = time(6,0,0)
        fin1 = time(17,0,0)
        
        debut2 = time(17,0,0)
        fin2 = time(19,0,0)
        
        current = datetime.combine(datetime.today(), debut1)
        end = datetime.combine(datetime.today(), fin1)

        while current < end:
            t = current.time()  # revenir en time

            stock = 0.0
            for materielle1 in materielles1:
                if materielle1.debutH <= t < materielle1.finH:
                    stock += float(materielle1.consomation)

            pui1 += float(maxW-stock)

            current += timedelta(hours=1)
        
        current = datetime.combine(datetime.today(), debut2)
        end = datetime.combine(datetime.today(), fin2)

        while current < end:
            t = current.time()  # revenir en time

            stock = 0.0
            for materielle2 in materielles2:
                if materielle2.debutH <= t < materielle2.finH:
                    stock += float(materielle2.consomation)

            pui2+= float((maxW*0.5)-stock)

            current += timedelta(hours=1)
        return pui1+pui2
    def calculeVolaM(): 
        watt = CalculPanneaux.calculWavendre() 
        jours = Jours.findAll()
        resultat = []
        for jour in jours:
            resultat.append(float(jour.prixU)*watt)
        return resultat
            
        