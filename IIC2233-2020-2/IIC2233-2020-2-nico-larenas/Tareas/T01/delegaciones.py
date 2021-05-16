from abc import ABC, abstractmethod
import parametros as par
import random
from deportistas import Deportistas


class Delegaciones(ABC):
    def __init__(self, entrenador, equipo, medallas, moral_eq, dinero):
        self.entrenador = entrenador
        self.equipo = equipo
        self.__medallas = medallas
        self.__moral_eq = moral_eq
        self.dinero = dinero
        self.__exc_resp = random.uniform(0,1)
        self.__imp_dep = random.uniform(0,1)
        self.__imp_med = random.uniform(0,1)

    @property
    def moral_eq(self):
        return self.__moral_eq
    
    @moral_eq.setter
    def moral_eq(self, moral_fin):
        if moral_fin > par.MORALT_MAX:
            self.__moral_eq = par.MORALT_MAX
        elif moral_fin < par.MORALT_MIN:
            self.__moral_eq = par.MORALT_MIN
    
    @property
    def exc_resp(self):
        return self.__exc_resp
    
    @exc_resp.setter
    def exc_resp(self, final_e_r):
        if final_e_r > par.FORTALEZA:
            self.__exc_resp = par.FORTALEZA
            print("Este atributo tiene su valor máximo")
        elif final_e_r < par.DEBILIDAD:
            self.__exc_resp = par.DEBILIDAD
            print("Este atributo tiene su valor mínimo")
        else:
            self.__exc_resp = final_e_r

    @property
    def imp_dep(self):
        return self.__imp_dep
    
    @imp_dep.setter
    def imp_dep(self, final_i_d):
        if final_i_d > par.FORTALEZA:
            self.__imp_dep = par.FORTALEZA
            print("Este atributo tiene su valor máximo")
        elif final_i_d < par.DEBILIDAD:
            self.__imp_dep = par.DEBILIDAD
            print("Este atributo tiene su valor mínimo")
        else:
            self.__imp_dep = final_i_d

    @property
    def imp_med(self):
        return self.__imp_med
    
    @imp_med.setter
    def imp_med(self, final_i_m):
        if final_i_m > par.FORTALEZA:
            self.__imp_med = par.FORTALEZA
            print("Este atributo tiene su valor máximo")
        elif final_i_m < par.DEBILIDAD:
            self.__imp_med = par.DEBILIDAD
            print("Este atributo tiene su valor mínimo")
        else:
            self.__imp_med = final_i_m

    def fichar_deportistas(self, fichajes):
        if self.moral_eq > par.MORAL_EQ:
            print("Estos son los posibles fichajes:")
            for m in fichajes.keys():
                print(fichajes[m]["nombre"]+" "+fichajes[m]["precio"])
            print("¿Qué jugador desea fichar?")
            fichar = str(input("Ingrese el nombre exacto del juagor"))
            if fichajes[fichar]["precio"] < self.dinero:
                self.dinero -= fichajes[fichar]["precio"]
                self.equipo.append(fichajes[fichar]["nombre"])
            elif fichajes[fichar]["precio"] > self.dinero:
                print("no tiene dinero suficiente")

    def entrenar_deportistas(self, dep):
        if self.dinero >= par.COSTO_ENVIO:
            self.dinero = self.dinero - par.COSTO_ENVIO
            dep.moral += par.MORAL_ENVIO
            

    def sanar_lesiones(self,dep):
        if self.dinero >= par.COSTO_RECUPERACION:
            self.dinero = self.dinero - par.COSTO_RECUPERACION
        prob_rec = (min(par.SAN_MAX,max(par.SAN_MIN,
                   (dep.moral*(self.imp_med+self.exc_resp)/par.DIV))))
        prob_rec = round(prob_rec,1)
        prob = random.uniform(0,1)
        if prob < prob_rec:
            dep.lesionado = False
        return dep.lesionado
    
    def comprar_tecnologia(self):
        if self.dinero >= par.COSTO_TECNOLOGIA:
            self.dinero = self.dinero - par.COSTO_TECNOLOGIA
            self.imp_dep += (self.__imp_dep*par.AUM_IMPLEMENTOS_DEP)
            self.imp_med += (self.__imp_med*par.AUM_IMPLEMENTOS_MED)
        return self.imp_dep, self.imp_med
        
    @abstractmethod
    def habilidad_especial(self):
        if self.dinero >= par.COSTO_HABILIDAD:
            self.dinero = self.dinero - par.COSTO_HABILIDAD


class IEEEsparta(Delegaciones):
    # La fórmula de entrenamiento deportivo se pondera por 1.7.
    # La moral del deportista disminuye el doble de lo normal cuando pierde una competencia.
    hab_esp = 1
    def habilidad_especial(self, hab_esp):
        super().habilidad_especial()
        if hab_esp == 1:
            # subir moral al max.
            # moral.dep = par.MAX_
            pass
        

class DCCrotona(Delegaciones):
    # : La delegación de DCCrotona es una de las delegaciones más populares de la competencia, 
    # es por esto que cada vez que un deportista de este equipo gana una medalla la moral del
    # deportista aumenta el doble que en condiciones normales.
    hab_esp = 1
    def habilidad_especial(self, hab_esp):
        super().habilidad_especial()
        if hab_esp == 1:
            # 
            pass
    # Cada vez que un jugador se lesiona, la delegación debe pagar el doble para poder sanar a sus
    # deportistas
    pass
