
import os

class Sokoban:
    """ Juego del Sokoban en terminal
    """
    def __init__(self) -> None:
        # Definir elementos del juego
        # Útil si se quieren cambiar la asignación de los elementos
        self.elementos = {
            "personaje": 0,
            "caja": 1,
            "pared": 2,
            "meta": 3,
            "camino": 4,
            "caja_meta": 5,
            "personaje_meta": 6
        }

        # Definir el mapa
        self.mapa_inicial = [
            [2, 2, 2, 2, 2, 2, 2],
            [2, 4, 3, 1, 4, 4, 2],
            [2, 4, 4, 0, 4, 4, 2],
            [2, 4, 3, 1, 4, 4, 2],
            [2, 2, 2, 2, 2, 2, 2],
        ]

        self.mapa = [fila.copy() for fila in self.mapa_inicial]

        # Buscar automáticamente la posición del personaje
        self.personaje_fila = 0
        self.personaje_columna = 0

        # Guardar las posiciones de las cajas y las metas
        self.cajas = []
        self.metas = []

        self.buscarElementos()

    def buscarElementos(self) -> None:
        # Buscar automáticamente el personaje, las cajas y las metas
        self.cajas = []
        self.metas = []

        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[fila])):
                casilla = self.mapa[fila][columna]

                if casilla == self.elementos["personaje"]:
                    self.personaje_fila = fila
                    self.personaje_columna = columna

                elif casilla == self.elementos["caja"]:
                    self.cajas.append((fila, columna))

                elif casilla == self.elementos["meta"]:
                    self.metas.append((fila, columna))

                elif casilla == self.elementos["caja_meta"]:
                    self.cajas.append((fila, columna))
                    self.metas.append((fila, columna))

                elif casilla == self.elementos["personaje_meta"]:
                    self.personaje_fila = fila
                    self.personaje_columna = columna
                    self.metas.append((fila, columna))

    def imprmirMapa(self) -> None:
        # Toma cada fila del mapa y la imprime
        for fila in self.mapa:
            print(fila)

    def mover(self, cambio_fila: int, cambio_columna: int) -> None:
        # Calcula la casilla a la que se quiere mover el personaje
        nueva_fila = self.personaje_fila + cambio_fila
        nueva_columna = self.personaje_columna + cambio_columna

        # Comprueba que la posición esté dentro del mapa
        if nueva_fila < 0 or nueva_fila >= len(self.mapa):
            return
        if nueva_columna < 0 or nueva_columna >= len(self.mapa[nueva_fila]):
            return

        casilla_actual = self.mapa[self.personaje_fila][self.personaje_columna]
        casilla_nueva = self.mapa[nueva_fila][nueva_columna]

        # Si hay una pared, el personaje no se puede mover
        if casilla_nueva == self.elementos["pared"]:
            return

        # Si hay una caja, revisa qué hay detrás para saber si se puede empujar
        if casilla_nueva == self.elementos["caja"] or casilla_nueva == self.elementos["caja_meta"]:
            fila_caja = nueva_fila + cambio_fila
            columna_caja = nueva_columna + cambio_columna

            # Comprueba que la caja no salga del mapa
            if fila_caja < 0 or fila_caja >= len(self.mapa):
                return
            if columna_caja < 0 or columna_caja >= len(self.mapa[fila_caja]):
                return

            casilla_detras = self.mapa[fila_caja][columna_caja]

            # La caja no se puede empujar contra una pared ni contra otra caja
            if casilla_detras == self.elementos["pared"]:
                return
            if casilla_detras == self.elementos["caja"] or casilla_detras == self.elementos["caja_meta"]:
                return
            if casilla_detras == self.elementos["personaje"] or casilla_detras == self.elementos["personaje_meta"]:
                return

            # Mueve la caja y revisa si queda encima de una meta
            if casilla_detras == self.elementos["meta"]:
                self.mapa[fila_caja][columna_caja] = self.elementos["caja_meta"]
            else:
                self.mapa[fila_caja][columna_caja] = self.elementos["caja"]

        # Deja libre la casilla donde estaba el personaje
        if casilla_actual == self.elementos["personaje_meta"]:
            self.mapa[self.personaje_fila][self.personaje_columna] = self.elementos["meta"]
        else:
            self.mapa[self.personaje_fila][self.personaje_columna] = self.elementos["camino"]

        # Coloca al personaje en la nueva casilla
        if casilla_nueva == self.elementos["meta"] or casilla_nueva == self.elementos["caja_meta"]:
            self.mapa[nueva_fila][nueva_columna] = self.elementos["personaje_meta"]
        else:
            self.mapa[nueva_fila][nueva_columna] = self.elementos["personaje"]

        # Actualiza la posición del personaje
        self.personaje_fila = nueva_fila
        self.personaje_columna = nueva_columna

        # Actualiza las posiciones de las cajas y las metas
        self.buscarElementos()

    def derecha(self) -> None:
        # Mueve el personaje hacia la derecha
        self.mover(0, 1)

    def izquierda(self) -> None:
        # Mueve el personaje hacia la izquierda
        self.mover(0, -1)

    def arriba(self) -> None:
        # Mueve el personaje hacia arriba
        self.mover(-1, 0)

    def abajo(self) -> None:
        # Mueve el personaje hacia abajo
        self.mover(1, 0)

    def reiniciar(self) -> None:
        # Vuelve a colocar el mapa en su estado inicial
        self.mapa = [fila.copy() for fila in self.mapa_inicial]

        # Busca automáticamente las posiciones iniciales
        self.buscarElementos()

    def nivelTerminado(self) -> bool:
        # Revisa si ya no quedan cajas fuera de las metas
        for fila in self.mapa:
            if self.elementos["caja"] in fila:
                return False

        # Si hay al menos una caja sobre una meta, se completó el nivel
        for fila in self.mapa:
            if self.elementos["caja_meta"] in fila:
                return True

        return False

    def jugar(self) -> None:
        """
        a - Izquierda
        d - Derecha
        w - Arriba
        s - Abajo
        r - Reiniciar
        q - Salir
        """
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            self.imprmirMapa()

            if self.nivelTerminado():
                print("¡Nivel completado!")
                break

            movimiento = input("Movimiento: ").lower()

            if movimiento == "d":
                self.derecha()
            elif movimiento == "a":
                self.izquierda()
            elif movimiento == "w":
                self.arriba()
            elif movimiento == "s":
                self.abajo()
            elif movimiento == "r":
                self.reiniciar()
            elif movimiento == "q":
                break


soko = Sokoban()
soko.jugar()
