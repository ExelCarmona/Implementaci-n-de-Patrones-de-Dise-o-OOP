class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Crea la instancia si no existe
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection_string = "Conexión a BD activada"
        return cls._instance

if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print("Demostración de Singleton:")
    print("Misma instancia DB1 y DB2?:", db1 is db2)
    print("Estado interno (DB1):", db1.connection_string)
