students_control = {}
key = True

#Sistema de adición de estudiantes
def student_add(dictionary, max_students):
    for attempt in range(max_students):
        id_tested = False
        while not id_tested:
            student_id = input("Coloque el ID del estudiante: ")
            if student_id in dictionary:
                print("Ese estudiante ya existe...")
            else:
                id_tested = True
        s_name = input("Coloque el nombre del estudiante: ")
        s_career = input("Coloque la carrera que cursa: ")
        dictionary[student_id] = {
            "name": s_name,
            "carreer": s_career,
            "courses": {}
        }
    return dictionary

# Agregado de cursos
def course_addition(student, max_courses):
    for attempt in range(max_courses):
        course_name = input("Coloque el nombre del curso: ")
        score_validation = False
        while not score_validation:
            course_score = int(input("Coloque el nombre del estudiante: "))
            if course_score < 0 or course_score > 100:
                print("Esa no es una nota válida")
            else:
                score_validation = True
        student["courses"][course_name] = {
            "score": course_score
        }
    return student


#Promedio y status
def status_avg_calc(dictionary, mod):
    div_end = 0
    total = 0
    for course_avg, score_avg in dictionary["courses"].items():
        div_end += 1
        total += score["score"]
        if score["score"] >= 61 and mod == 2:
            print(f"El curso {course_avg} fue aprobado con {score_avg["score"]} puntos\n")
        elif score["score"] < 61 and mod == 2:
            print(f"El curso {course_avg} NO fue aprobado, sacó {score_avg["score"]} puntos\n")
    if mod == 0:
        print(f"El promedio general es: {total/div_end}")


try:
    while key:
        print("------------Bienvenido al programa---------")
        ops = input("1.Agregar estudiante\n"
                    "2.Agregar curso con nota\n"
                    "3.Consultar estudiante\n"
                    "4. Calcular promedio de estudiante\n"
                    "5. Verificar si aprueba\n"
                    "6. Mostrar todos los estudiantes\n"
                    "7. Salir del programa\n\n"
                    "Escoja una opción: ")
        match ops:
            case "1":
                max_s = int(input("¿Cuántos estudiantes desea agregar?: "))
                student_add(students_control, max_s)
            case "2":
                id_searched = input("Coloque el ID que desea buscar: ")
                if id_searched in students_control:
                    max_c = int(input("¿Cuántos cursos desea agregar?: "))
                    course_addition(students_control[id_searched], max_c)
            case "3":
                display_searched = input("Coloque el ID del estudiante al que quiere consultar: ")
                if display_searched in students_control:
                    print(f"\nAlumno: {students_control[display_searched]["name"]}\n"
                          f"Carrera: {students_control[display_searched]["carreer"]}\n♦ Cursos: ♦")
                    for course, score in students_control[display_searched]["courses"].items():
                        print(f"♥ Curso: {course}|Nota: {score["score"]}\n")
            case "4":
                avg_searcher = input("Coloque el ID del estudiante: ")
                if avg_searcher in students_control:
                    status_avg_calc(students_control[avg_searcher], 0)
            case "5":
                pass
            case "6":
                pass
            case "7":
                key = False

except ValueError:
    print("Eso no es un número")
except Exception as e:
    print("Anomalía detectada: {}".format(e))
finally:
    print("♥ Gracias por usar el programa ♥")