from estudiante import cargar_datos, cargar_datos_corto


def verificar_numero_alumno(alumno):
    if not alumno.n_alumno.isdigit() or alumno.n_alumno[:-1] != "J":
        raise ValueError("El numero de alumno es incorrecto")
    if alumno.n_alumno[2:4] != "63" and alumno.carrera == "Ingeniería":
        raise ValueError("El numero de alumno es incorrecto")
    if alumno.n_alumno[2:4] != "61" and alumno.carrera == "College":
        raise ValueError("El numero de alumno es incorrecto")
    if alumno.n_alumno[:2] != (str(alumno.generacion))[-2:]:
        raise ValueError("El numero de alumno es incorrecto")

def corregir_alumno(alumno):
    try:
        verificar_numero_alumno(alumno)
    except ValueError as error1:
        print(f"Error: {error1}")
        if alumno.n_alumno[:2] != (str(alumno.generacion))[-2:]:
            alumno.n_alumno = (str(alumno.generacion))[-2:] + alumno.n_alumno[2:]
        if alumno.n_alumno[2:4] != "61" and alumno.carrera == "College":
            alumno.n_alumno = alumno.n_alumno[:2]+"61"+alumno.n_alumno[4:]
        if alumno.n_alumno[2:4] != "61" and alumno.carrera == "Ingeniería":
            alumno.n_alumno = alumno.n_alumno[:2]+"63"+alumno.n_alumno[4:]
    finally:
        print(alumno.nombre+" está correctamente inscrite en el curso, todo en orden")


# ************
def verificar_inscripcion_alumno(n_alumno, base_de_datos): 
    if n_alumno in base_de_datos.keys():
        raise KeyError("El numero de alumno no se encuentra en la base de datos")


def inscripcion_valida(n_alumno, base_de_datos): 
    try:
        verificar_inscripcion_alumno(n_alumno,base_de_datos)
    except KeyError as error2:
        print(f"Error: {error2}")
        print("¡Alerta! ¡Puede ser Dr. Pinto intentando atraparte!")


# ************

def verificar_nota(nota):  # Levanta la excepción correspondiente
    if not isinstance(nota,float):
        raise TypeError("El numero de alumno es incorrecto")


def corregir_nota(alumno):  # Captura la excepción anterior
    try: 
        verificar_nota(alumno.promedio)
    except TypeError as error3:
        print(f"Error: {error3}")
        if not isinstance(alumno.promedio, int):
                alumno.promedio = float(alumno.promedio.replace(',','.'))
        #https://stackoverflow.com/questions/6633523/how-can-i-convert-a-string-with-dot-and-comma-into-a-float-in-python
        if isinstance(alumno.promedio, int):
            alumno.promedio = float(alumno.promedio)
        
    finally:
        print("Procediendo a hacer git hack sobre "+str(alumno.promedio))


if __name__ == "__main__":
    datos = cargar_datos_corto("alumnos.txt")  # Se cargan los datos
    for alumno in datos.values():
        if alumno.carrera != "Profesor":
            corregir_alumno(alumno)
            inscripcion_valida(alumno, datos)
            corregir_nota(alumno)
