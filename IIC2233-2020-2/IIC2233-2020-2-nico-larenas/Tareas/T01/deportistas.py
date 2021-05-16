import cargar_datos
import parametros as par
import random

class Deportistas:
    def __init__(self, vel, res, flex, mor, lesionado, precio):
        self.__velocidad = vel
        self.__resistencia = res
        self.__flexibilidad = flex
        self.__moral = mor
        self.lesionado = lesionado
        self.precio = precio

    @property
    def velocidad(self):
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self, final_vel):
        if final_vel > par.VELOCIDAD_MAX:
            self.__velocidad = par.VELOCIDAD_MAX
        elif final_vel < par.VELOCIDAD_MIN:
            self.__velocidad = par.VELOCIDAD_MIN
        else:
            self.__velocidad = final_vel
    
    @property
    def resistencia(self):
        return self.__resistencia
    
    @resistencia.setter
    def resistencia(self, final_res):
        if final_res > par.RESISTENCIA_MAX:
            self.__resistencia = par.RESISTENCIA_MAX
        elif final_res < par.RESISTENCIA_MIN:
            self.__resistencia = par.RESISTENCIA_MIN
        else:
            self.__resistencia = final_res
    
    @property
    def flexibilidad(self):
        return self.__flexibilidad
    
    @flexibilidad.setter
    def flexibilidad(self, final_flex):
        if final_flex > par.FLEXIBILIDAD_MAX:
            self.__flexibilidad = par.FLEXIBILIDAD_MAX
        elif final_flex < par.FLEXIBILIDAD_MIN:
            self.__flexibilidad = par.FLEXIBILIDAD_MIN
        else:
            self.__flexibilidad = final_flex

    @property
    def moral(self):
        return self.__moral
        
    @moral.setter
    def moral(self, final_moral):
        if final_moral > par.MORAL_MAX:
            self.__moral = par.MORAL_MAX
        elif final_moral < par.MORAL_MIN:
            self.__moral = par.MORAL_MIN
        else:
            self.__moral = final_moral


    def entrenar(self, atributo):
        if atributo == "Velocidad":
            self.velocidad += par.PUNTOS_ENTRENAMIENTO
            return self.velocidad
        elif atributo == "Resistencia":
            self.resistencia += par.PUNTOS_ENTRENAMIENTO
            return self.resistencia
        elif atributo == "Flexibilidad":
            self.flexibilidad+= par.PUNTOS_ENTRENAMIENTO
            return self.flexibilidad
        elif atributo == "Moral":
            self.moral += par.PUNTOS_ENTRENAMIENTO
            return self.moral
            

    def lesionarse(self, riesgo):
        prob = random.uniform(0,1)
        if prob < riesgo:
            self.lesionado = True
