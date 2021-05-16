from estudiante import cargar_datos
from verificar import corregir_alumno, corregir_nota, inscripcion_valida


class GymPro(Exception): 
    def __init__(self, alumno):
        super().__init__("Wait a minute... Who are you?")
        self.profesor = alumno.nombre

    def evitar_sospechas(self):
        print("¡Cuidado, viene " +self.profesor+ "! Solo estaba haciendo mi último push...")
    

if __name__ == "__main__":
    datos = cargar_datos("alumnos.txt")
    nueva_base = dict()
    for alumno in datos.values():
        corregir_alumno(alumno)
        corregir_nota(alumno)
        nueva_base[alumno.n_alumno] = alumno
    for alumno in nueva_base.values():
        try:
            if alumno.carrera == "Profesor":
                raise GymPro

        except:  
            pass
