import deportes
import deportistas


class Campeonato:
    def __init__(self, dia, medallero):
        self.dia = dia
        self.medallero = medallero

    def competencias_dia(self, atleta_1, atleta_2, ciclista_1, ciclista_2,
                         gimnasta_1, gimnasta_2, nadador_1, nadador_2):
        # Atletismo
        res_a = deportes.Atletismo().calcular_ganador(atleta_1,atleta_2)
        # Ciclismo
        res_c = deportes.Ciclismo().calcular_ganador(ciclista_1,ciclista_2)
        # Gimnasia
        res_g = deportes.Gimnasia().calcular_ganador(gimnasta_1,gimnasta_2)
        # Natacion
        res_n = deportes.Natacion().calcular_ganador(nadador_1,nadador_2)

        ruta_resultados = "resultados.txt"
        with open(ruta_resultados, 'a') as puntajes:
            puntajes.write(res_a+"\n")
        ruta_resultados = "resultados.txt"
        with open(ruta_resultados, 'a') as puntajes:
            puntajes.write(res_c+"\n")
        ruta_resultados = "resultados.txt"
        with open(ruta_resultados, 'a') as puntajes:
            puntajes.write(res_g+"\n")
        ruta_resultados = "resultados.txt"
        with open(ruta_resultados, 'a') as puntajes:
            puntajes.write(res_n+"\n")


    def premiar(self):
        pass

    def calcular_moral(self):
        pass

    def estado_del_dep(self):
        pass
