# Python Design Patterns

Este repositorio contiene 5 proyectos funcionales que demuestran la implementación de 5 de los patrones de diseño orientados a objetos más comunes:

## Proyectos y Patrones Explicados

1. Singleton (Creacional)
   - Propósito: Garantiza que una clase tenga únicamente una instancia y proporciona un punto de acceso global a esta.
   - En el proyecto (`singleton/main.py`): Se implementa una clase `DatabaseConnection` que intercepta la creación de objetos sobrescribiendo el método mágico `__new__`. Si se intenta crear más de un objeto para la conexión, el patrón garantiza que siempre se devuelva la primera y única instancia en memoria.

2. Factory Method (Creacional)
   - Propósito: Define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase instanciar.
   - En el proyecto (`factory_method/main.py`): Tenemos una fábrica base `AnimalFactory` que delega la creación específica de animales a las fábricas concretas `DogFactory` y `CatFactory`. Esto evita introducir dependencias directas de las clases concretas de productos (`Dog` y `Cat`) en nuestra lógica de negocio superficial.

3. Observer (De comportamiento)
   - Propósito: Define una dependencia de uno-a-muchos entre objetos agrupados, de manera que cuando el objeto principal ("Sujeto") cambie su estado, notifica automáticamente a los objetos dependientes ("Observadores").
   - En el proyecto (`observer/main.py`): La clase `Subject` maneja una lista de suscripción. Cuando llamamos a `set_state()`, este invoca internamente al método `notify()`, el cual recorre su lista y avisa a todos los objetos `ConcreteObserver` instanciados y registrados para que reaccionen adecuadamente mediante su propio método `update()`.

4. Strategy (De comportamiento)
   - Propósito: Define y encapsula una familia de algoritmos en clases independientes y los hace intercambiables en tiempo de ejecución, de acuerdo con el contexto.
   - En el proyecto (`strategy/main.py`): Tenemos un contexto principal `ShoppingCart` (carrito de compras) que recibe en uno de sus atributos, de manera inyectada, una estrategia de pago abstracta (`PaymentStrategy`). Gracias a ello, podemos decidir e intercambiar dinámicamente si queremos procesar el pago mediante PayPal (`PayPalPayment`) o Tarjeta de Crédito (`CreditCardPayment`), sin modificar el proceso nativo del carrito en sí.

5. Decorator (Estructural)
   - Propósito: Permite añadir funcionalidad nueva a los objetos sin alterar su código base subyacente, "envolviéndolos" dentro de objetos especiales ("decoradores o wrappers").
   - En el proyecto (`decorator/main.py`): Se arranca con una interfaz simple `Coffee` y una implementación concreta `SimpleCoffee`. Después, se le proveen envolturas (`CoffeeDecorator`) que delegan la misma interfaz a un objeto envuelto. Adicionalmente, tenemos decoradores extra (`MilkDecorator` y `VanillaDecorator`) que toman instacias de código de café para agregar su propia lógica (ya sean nuevos componentes al string de la descripción o modificaciones del precio original). Estas modificaciones se apilan unas con otras dinámicamente sin usar herencia pesada.

## Cambios Recientes (Refactorización y Tipado Estricto)

Como parte del mantenimiento del código, se llevaron a cabo una serie de correcciones orientadas a mejorar la conformidad del proyecto con análisis estáticos estrictos (ej. tipeo de Pyright, Pylance, Pyre):

- Coherencia de métodos sobreescritos: A lo largo del código se arreglaron firmas que presentaban variables de retorno inconsistentes o en blanco, respetando a cabalidad lo impuesto por la interfaz base abstracta (métodos como `get_cost()`, `speak()`, etc.).
- Corrección explícita de `@abstractmethod` en Interfaces: Previamente se utilizaba la convención `pass` o `...` en cuerpos de métodos abstractos. Esta práctica derivaba en advertencias de tipeo como _“Missing Return Value”_ (ej. Si la firma promete `-> float`, un `pass` hace que la función devuelva implícitamente `None`). Como arreglo, se implementó el lanzamiento explícito de `raise NotImplementedError`. De este modo, los chequeadores tipo Pylance entienden que la ejecución de la función _se detiene_ en ese paso particular de la interfaz abstracta, y el _warning_ de tipos deja de insistir por el retorno flotante erróneo.

## Ejecución

Puedes entrar en cualquiera de las 5 carpetas y ejecutar el archivo `main.py` para ver el resultado respectivo en la consola. Un ejemplo:

## Reflexion de los patrones de diseño

Después de revisar esta página me di cuenta de que programar no es solo escribir código a lo loco para que algo funcione, sino que hay que ser ordenado y usar la lógica. Los patrones de diseño son como recetas o plantillas que ya inventaron expertos para resolver problemas que a todos nos pasan cuando creamos un programa, como cuando no sabes cómo organizar los objetos o cómo hacer que varias partes se comuniquen sin que sea un caos. Me pareció súper interesante que se dividan en grupos, como los creacionales o los de comportamiento, porque te ayudan a que el código sea más limpio y fácil de entender para otros. Al principio parece un poco difícil con nombres raros como Singleton o Observer, pero si los aprendemos ahora que estamos empezando, nos vamos a ahorrar un montón de errores y dolores de cabeza en el futuro. Siento que usar estos patrones es lo que diferencia a alguien que solo escribe líneas de un verdadero desarrollador que piensa en grande.

```bash
python decorator/main.py
```
