from datetime import datetime, timedelta,time
from utils.db_connection import DBConnection
from models.PeriodeJ import PeriodeJ
class Jours:
    def __init__(self, id, prixU):
        self.id = id
        self.prixU = prixU
    
    def findAll():
        conn= DBConnection.connect()
        jours = []

        if conn is None:
            return jours
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, prixU FROM Jours")
    
            rows = cursor.fetchall()
    
            for row in rows:
                jour = Jours(
                    id=row[0],
                    prixU=row[1]
                )
                jours.append(jour)

        except Exception as e:
            print("Erreur lors du findAll :", e)
        finally:
            conn.close()
    
        return jours
