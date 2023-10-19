class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        
    def imprimir(self):
        print(f"La nota de {self.nombre} es {self.nota}")
        
    def resultado(self):
        if self.nota >= 5:
            return "Aprobado"
        else:
            return "Desaprobado"
    
alumno1 = Alumno("Martin Navarro", 10)
alumno2 = Alumno("Valentina Rosales", 8)
alumno3 = Alumno("Martina Rizzotti", 6)
alumno4 = Alumno("Jose Perez", 4)

print(alumno1.imprimir())
print(alumno1.resultado())
print(alumno2.imprimir())
print(alumno2.resultado())
print(alumno3.imprimir())
print(alumno3.resultado())
print(alumno4.imprimir())
print(alumno4.resultado())