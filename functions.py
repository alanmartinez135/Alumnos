nombres = []
notas = []

def nuevo_alumno():
    n_nombre = str(input("Ingrese el nombre del alumno: "))
    nombres.append(n_nombre)
    n_nota = int(input("Ingresa la nota del alumno: "))
    notas.append(n_nota)
    print(nombres)
    print(notas)
    


def menu():
    print("Bienvenido, selecciona una opción")
    print("[1] Nuevo Alumno")
    print("[2] Buscar notas alumno y promedio")
    print("[3] Calcular promedio de notas de todos los alumnos")
    print("[4] Borrar alumno")
    print("[5] Actualizar notas alumno")
    print("[6] Listar notas y promedios finales de todos los alumnos")
    print("[7] Mostrar alumnos repitentes")
    print("[8] Mostrar alumnos aprobados")
    print("[9] Importar alumnos a txt")
    print("[10] Exportar alumnos de doc txt")
    opc = int(input("Ingresa una opción: "))
    if opc == 1:
        nuevo_alumno()

menu() 

