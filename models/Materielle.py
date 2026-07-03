from datetime import datetime, timedelta,time
from utils.db_connection import DBConnection
from models.PeriodeJ import PeriodeJ
class Materielle:
    def __init__(self, id, name,consomation, debutH, finH):
        self.id = id
        self.name = name
        self.debutH = debutH
        self.finH = finH
        self.consomation = consomation
    
    def __str__(self):
        return f"Materielle(id={self.id}, name='{self.name}', debutH={self.debutH}, finH={self.finH}, consomation={self.consomation})"
    @staticmethod
    def insert_Materielle(materielle):
        conn = DBConnection.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

            query = """
            INSERT INTO Materielle (id, name, debutH, finH, consomation)
            VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(query, (
                materielle.id,
                materielle.name,
                materielle.debutH,
                materielle.finH,
                materielle.consomation
            ))

            conn.commit()
            print("Insertion réussie !")
            return True

        except Exception as e:
            print("Erreur lors de l'insertion :", e)
            conn.rollback()
            return False

        finally:
            conn.close()
    @staticmethod
    def findAll():
        conn = DBConnection.connect()
        materiels = []

        if conn is None:
            return materiels
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name,debutH,finH,consomation FROM Materielle")
    
            rows = cursor.fetchall()
    
            for row in rows:
                materiel = Materielle(
                    id=row[0],
                    name=row[1],
                    debutH=row[2],
                    finH=row[3],
                    consomation=row[4]
                )
                materiels.append(materiel)
    
        except Exception as e:
            print("Erreur lors du findAll :", e)
        finally:
            conn.close()
    
        return materiels

    @staticmethod
    def getByIdperiode(idperiode):
        conn = DBConnection.connect()
        periode = PeriodeJ.getById(idperiode)
        if periode is None:
            return []
        materielles = Materielle.findAll()
        data = []
        
        def get_segments(d, f):
            if d < f:
                return [(d, f)]
            elif d > f:
                return [(d, time(23, 59, 59, 999999)), (time(0, 0), f)]
            else:
                # Si debut == fin, on considere pas que c'est l'anomalie ou 24h, 
                # on renvoie just l'intervalle d'un instant
                return [(d, f)]

        p_segs = get_segments(periode.debutH, periode.finH)

        for materielle in materielles:
            m_segs = get_segments(materielle.debutH, materielle.finH)
            overlap = False
            for ps, pe in p_segs:
                for ms, me in m_segs:
                    # Condition stricte d'intersection ou inclusion
                    # si max(debut) < min(fin), l'intervalle est valide
                    if max(ps, ms) < min(pe, me) or (ms == me and ps <= ms <= pe):
                        overlap = True
                        break
                if overlap:
                    break
            
            if overlap:
                data.append(materielle)
        
        return data
        