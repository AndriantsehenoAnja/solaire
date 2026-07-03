import pymssql

class DBConnection:
    
    @staticmethod
    def connect():
        try:
            connection = pymssql.connect(
                server='localhost:1433',
                user='SA',
                password='Sqlserver?123',
                database='solaire'
            )
            return connection
        except Exception as e:
            print("Error connecting to the database:", e)
            return None

if __name__ == "__main__":
    conn = DBConnection.connect()
    if conn:
        print("Connection successful!")
        conn.close()
    else:
        print("Connection failed.")