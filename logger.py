class Logger:
    __instancia = None

    def __init__(self):
        """Private constructor to avoid direct instantiation"""
        if Logger.__instancia is not None:
            raise Exception("Esta clase es Singleton. Usa obtener_instancia() para acceder.")
        print("Inicializando el Logger...")
        self.log = []


    @staticmethod
    def obtener_instancia():
        """Method to get the only instance of the class"""
        if Logger.__instancia is None:
            Logger.__instancia = Logger()
            print("Instancia única de Logger creada.")
        else:
            print("Instancia única ya existente.")
        return Logger.__instancia

    def registrar_evento(self, mensaje):
        """Method to log an event (simulated with a message)"""
        self.log.append(mensaje)
        print(f"Evento registrado: {mensaje}")


    def mostrar_log(self):
        """Method to display logged events"""
        print("Registro de eventos:")
        for evento in self.log:
            print(evento)


# Example of use...
if __name__ == "__main__":
    # We try to get the unique instance of the Logger
    logger1 = Logger.obtener_instancia()

    # Register some events
    logger1.registrar_evento("Error al conectar a la base de datos")
    logger1.registrar_evento("Conexión exitosa a la API")

    # Show logged events
    logger1.mostrar_log()

    # We try to have another instance to verify that it is the same
    logger2 = Logger.obtener_instancia()
    print("¿Son la misma instancia?", logger1 is logger2)

    # Display the logged events again to verify that it is the same instance
    logger2.mostrar_log()