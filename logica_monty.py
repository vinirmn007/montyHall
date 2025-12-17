import random

class JuegoMontyHall:
    def __init__(self, num_puertas):
        self.num_puertas = num_puertas
        self.puerta_ganadora = random.randint(0, num_puertas - 1)
        self.eleccion_usuario = None
        self.puerta_alternativa = None
        self.puertas_abiertas = []

    def seleccionar_puerta_inicial(self, indice):
        self.eleccion_usuario = indice

    def obtener_puertas_para_abrir(self):
        opciones = list(range(self.num_puertas))
        
        if self.eleccion_usuario == self.puerta_ganadora:
            opciones.remove(self.eleccion_usuario)
            self.puerta_alternativa = random.choice(opciones)
        else:
            self.puerta_alternativa = self.puerta_ganadora
            
        self.puertas_abiertas = [
            p for p in range(self.num_puertas) 
            if p != self.eleccion_usuario and p != self.puerta_alternativa
        ]
        
        return self.puertas_abiertas, self.puerta_alternativa

    def verificar_victoria(self, eleccion_final):
        return eleccion_final == self.puerta_ganadora

    def obtener_ganadora(self):
        return self.puerta_ganadora