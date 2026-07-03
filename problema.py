asignaturas = {
'DSY1103': ['Fullstack', 'L4', 7, 42, 12],
'FPY1101': ['Programación', 'L6', 7, 21, 23],
'OCY1101': ['CyberSeguridad', 'online', 4, 31, 14],
'DSY1101': ['Cloud Computing', 'L3', 4, 31, 6],
'DSY1105': ['Aplicaciones Mobile', 'L9', 5, 15, 21],
'MDY3131': ['Base de Datos', 'L3', 5, 11, 12]
}

def iniciafuncion(nombre):
    print("Incicia la Función ", nombre)

def totalAlumnos(codigo):
    iniciafuncion("totalAlumnos") 
    if codigo in asignaturas:
        datos = asignaturas[codigo]
        
        print("El resultado de la sumatoria de alumnos es:",datos[3] + datos[4])

        return datos[3] + datos[4]
    
    return 0

def totalAsignaturas():
    
    iniciafuncion("totalAsignaturas") 
    return len(asignaturas) 

def asignaturasPorSala(sala):
    iniciafuncion("asignaturasPorSala") 
    resultado = []
    for codigo, datos in asignaturas.items():
        if datos[1].lower() == sala.lower():
            resultado.append(codigo) 
    return resultado

totalAlumnos("DSY1103")