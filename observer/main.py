class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        print(f"\nSubject: Cambiando estado a '{state}'")
        self._state = state
        self.notify()

class ConcreteObserver:
    def __init__(self, name):
        self.name = name

    def update(self, state):
        print(f"Observer {self.name}: Reaccionó al nuevo estado ({state})")

if __name__ == "__main__":
    print("Demostración de Observer:")
    sujeto = Subject()
    
    obs1 = ConcreteObserver("Uno")
    obs2 = ConcreteObserver("Dos")

    sujeto.attach(obs1)
    sujeto.attach(obs2)

    sujeto.set_state("ACTIVO")
    sujeto.set_state("INACTIVO")
