from abc import ABC, abstractmethod
import parametros as par
import deportistas


class Deporte(ABC):
    def __init__(self, implemento, riesgo):
        self.implemento = implemento
        self.riesgo = riesgo

    def validez_de_la_competencia(self, dep_1, dep_2):
        if not dep_1.lesionado and not dep_2.lesionado:
            pass
        
        elif dep_1.lesionado and dep_2.lesionado:             
            pass
    
    @abstractmethod
    def calcular_ganador(self):
        pass


class Atletismo(Deporte):
    def __init__(self):
        super().__init__(par.IMPLEMENTO_ATLETISMO, par.RIESGO_ATLETISMO)

    def calcular_ganador(self, dep_1, dep_2):
        p1 = max(par.PUNTAJE_MINIMO, par.VEL_ATL*dep_1.velocidad + par.RES_ATL
                 * dep_1.resistencia + par.MOR_ATL*dep_1.moral)
        p2 = max(par.PUNTAJE_MINIMO, par.VEL_ATL*dep_2.velocidad + par.RES_ATL
                 * dep_2.resistencia + par.MOR_ATL*dep_2.moral)
        if p1 > p2:
            ganador = p1
            perdedor = p2
        
        elif p2 > p1:
            ganador = p2
            perdedor = p1

        return ganador, perdedor


class Ciclismo(Deporte):
    def __init__(self):
        super().__init__(par.IMPLEMENTO_CICLISMO, par.RIESGO_CICLISMO)

    def calcular_ganador(self, dep_1, dep_2):
        p1 = max(par.PUNTAJE_MINIMO, par.VEL_CIC*dep_1.velocidad + par.RES_CIC
                 * dep_1.resistencia + par.FLEX_CIC*dep_1.flexibilidad)
        p2 = max(par.PUNTAJE_MINIMO, par.VEL_CIC*dep_2.velocidad + par.RES_CIC
                 * dep_2.resistencia + par.FLEX_CIC*dep_2.flexibilidad)
        if p1 > p2:
            ganador = p1
            perdedor = p2
        
        elif p2 > p1:
            ganador = p2
            perdedor = p1
            
        return ganador, perdedor


class Gimnasia(Deporte):
    def __init__(self):
        super().__init__(par.IMPLEMENTO_GIMNASIA, par.RIESGO_GIMNASIA)

    def calcular_ganador(self, dep_1, dep_2):
        p1 = max(par.PUNTAJE_MINIMO, par.VEL_GIM*dep_1.velocidad + par.RES_GIM
                 * dep_1.resistencia + par.MOR_GIM*dep_1.moral)
        p2 = max(par.PUNTAJE_MINIMO, par.VEL_GIM*dep_2.velocidad + par.RES_GIM
                 * dep_2.resistencia + par.MOR_GIM*dep_2.moral)
        if p1 > p2:
            ganador = p1
            perdedor = p2
        
        elif p2 > p1:
            ganador = p2
            perdedor = p1
            
        return ganador, perdedor


class Natacion(Deporte):
    def __init__(self):
        super().__init__(par.IMPLEMENTO_NATACION, par.RIESGO_NATACION)

    def calcular_ganador(self, dep_1, dep_2):
        p1 = max(par.PUNTAJE_MINIMO, par.VEL_NAT*dep_1.velocidad + par.RES_NAT
                 * dep_1.resistencia + par.FLEX_NAT*dep_1.flexibilidad)
        p2 = max(par.PUNTAJE_MINIMO, par.VEL_NAT*dep_2.velocidad + par.RES_NAT
                 * dep_2.resistencia + par.FLEX_NAT*dep_2.flexibilidad)
        if p1 > p2:
            ganador = p1
            perdedor = p2
        
        elif p2 > p1:
            ganador = p2
            perdedor = p1
            
        return ganador, perdedor


# # VER VALIDEZ COMPETENCIA
