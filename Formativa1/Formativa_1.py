def cargarEvaluacion(puntajeTotal, exigencia=60):
    resultados = []

    try:
        nombreArchivo = input("Ingrese el nombre del archivo de entrada: ")
        with open(nombreArchivo, 'r') as archivo:
            for linea in archivo:
                elementos = linea.strip().split(';')
                rut = elementos[0].strip()
                nombre = elementos[1].strip()
                puntajes = [int(elemento) for elemento in elementos[2:]]
                puntajeObtenido = sum(puntajes)
                # Calcular la nota en una escala de 1 a 7
                nota = (puntajeObtenido / puntajeTotal) * 6 + 1

                # Verificar si el alumno aprueba o reprueba
                aprobado = "Aprobado" if nota >= 4 else "Reprobado"

                resultado_alumno = {
                    "RUT": rut,
                    "Nombre": nombre,
                    "Puntaje Total Obtenido": puntajeObtenido,
                    "Nota": nota,
                    "Estado": aprobado
                }
                resultados.append(resultado_alumno)

    except FileNotFoundError:
        print(f"El archivo {nombreArchivo} no fue encontrado.")

    return resultados

puntajeTotal = int(input("Ingrese el puntaje total de la evaluación: "))
exigencia = input("Ingrese el porcentaje de exigencia: ")
resultados_evaluacion = cargarEvaluacion(puntajeTotal, exigencia)

for alumno in resultados_evaluacion:
    print("RUT:", alumno["RUT"])
    print("Nombre:", alumno["Nombre"])
    print("Puntaje Total Obtenido:", alumno["Puntaje Total Obtenido"])
    print("Nota:", alumno["Nota"])
    print("Estado:", alumno["Estado"])
    print()


