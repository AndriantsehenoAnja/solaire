from datetime import datetime, timedelta,time
from utils.db_connection import DBConnection
from models.PeriodeJ import PeriodeJ
class Panneau:
    def __init__(self, id, name, consomation, coef, prix):
        self.id = id
        self.name = name
        self.consomation = consomation
        self.coef = coef
        self.prix = prix
    def __str__(self):
        return f"Panneau(id={self.id}, name='{self.name}', consomation={self.consomation}, coef={self.coef}, prix={self.prix})"
    @staticmethod
    def insert_Panneau(panneau):
        conn = DBConnection.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

            query = """
            INSERT INTO Panneaux (id, name, consomation, coef, prix)
            VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(query, (
                panneau.id,
                panneau.name,
                panneau.consomation,
                panneau.coef,
                panneau.prix
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
        panneaux = []

        if conn is None:
            return panneaux
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, consomation, coef, prix FROM Panneaux")
    
            rows = cursor.fetchall()
    
            for row in rows:
                panneau = Panneau(id=row[0], name=row[1], consomation=row[2], coef=row[3], prix=row[4])
                panneaux.append(panneau)
    
            return panneaux

        except Exception as e:
            print("Erreur lors de la récupération des panneaux :", e)
            return []

        finally:
            conn.close()
    def getById(id):
        conn = DBConnection.connect()

        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, consomation, coef, prix FROM Panneaux WHERE id = %s",
                (id,)
            )

            row = cursor.fetchone()

            if row:
                return Panneau(id=row[0], name=row[1], consomation=row[2], coef=row[3], prix=row[4])

        except Exception as e:
            print("Erreur lors du getById :", e)
            return None