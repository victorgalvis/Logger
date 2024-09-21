# Patrón Singleton 

Caso:
En una empresa de tecnología que gestiona una plataforma crítica para clientes, se ha decidido implementar un sistema de monitoreo que registre todos los eventos importantes de la aplicación, tales como errores, advertencias y otros logs del sistema. Este sistema debe garantizar que todos los eventos sean registrados de forma consistente y centralizada en un archivo o base de datos. Para evitar que múltiples componentes del sistema accedan de forma simultánea y creen registros duplicados o en desorden

# Logger 
Implementación en Python: 

Se crea la clase Logger tiene una única responsabilidad, que es gestionar el registro de eventos.
1. Atributo estático __instancia:
Este atributo se utiliza para almacenar la única instancia de Logger.

2. Constructor __init__: 
El constructor es privado porque solo debe ejecutarse una vez para evitar la creación de múltiples instancias. Si ya existe una instancia (__instancia no es None), lanza una excepción para prevenir la creación de otra.

3. Método estático obtener_instancia:
Este método es responsable de crear o devolver la única instancia de Logger. Si aún no ha sido creada, la instancia se inicializa y se asigna a __instancia. Si ya existe, simplemente devuelve esa instancia.

4. Método registrar_evento:
Permite agregar eventos al registro (lista de mensajes).

5. Método mostrar_log:
Muestra todos los eventos que se han registrado hasta el momento, recorriendo la lista log y mostrando los mensajes en consola.

