import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import parametros as p
from backend.logica_vinicio import Inicial
from frontend.resumen import Resumen
from frontend.ranking import Ranking
from frontend.ventana_inicial import VentanaInicial
from frontend.ventana_principal import VentanaPrincipal


def hook(type_error, traceback):
    print(type_error)
    print(traceback)

if __name__ == '__main__':
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)

    ventana_inicio = VentanaInicial()
    logica_inicio = Inicial()
    ventana_inicio.senal_revisar_nombre.connect(logica_inicio.comparar_codigo)
    logica_inicio.senal_resultado_nombre.connect(ventana_inicio.recibir_nombre)

    ventana_principal = VentanaPrincipal()
    ventana_inicio.senal_abrir_ventana_principal.connect(
        ventana_principal.senal_abrir_ventana_principal
        )

    ventana_ranking = Ranking()
    ventana_inicio.senal_abrir_ranking.connect(ventana_ranking.senal_abrir_ranking)
    ventana_ranking.senal_volver_inicio.connect(ventana_inicio.senal_volver_inicio)

    ventana_resumen = Resumen()
    ventana_resumen.senal_volver_inicio.connect(ventana_inicio.senal_volver_inicio)
    

    ventana_inicio.show()
    app.exec()

