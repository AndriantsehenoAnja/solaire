from utils.db_connection import DBConnection
from datetime import datetime, timedelta,time
class PeriodeJ:
    def __init__(self, id, name, debutH, finH):
        self.id = id
        self.name = name
        self.debutH = debutH
        self.finH = finH
    def findAll():
        conn = DBConnection.connect()
        periodeJ = []

        if conn is None:
            return periodeJ
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, debutH,finH FROM PeriodeJ")
    
            rows = cursor.fetchall()
    
            for row in rows:
                period = PeriodeJ(
                    id=row[0],
                    name=row[1],
                    debutH=row[2],
                    finH=row[3]
                )
                periodeJ.append(period)
    
        except Exception as e:
            print("Erreur lors du findAll :", e)
        finally:
            conn.close()

        return periodeJ

    @staticmethod
    def getById(id):
        conn = DBConnection.connect()

        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, debutH, finH FROM PeriodeJ WHERE id = %s",
                (id,)
            )

            row = cursor.fetchone()

            if row:
                return PeriodeJ(
                    id=row[0],
                    name=row[1],
                    debutH=row[2],
                    finH=row[3]
                )

        except Exception as e:
            print("Erreur lors du getById :", e)

        finally:
            conn.close()

        return None