import os

def funcion_bienvenida():
    print("¡Bienvenida a -Que te favorece-!")
    nombre = input("¿Cómo es tu nombre?: ")
    print(f"¡Hola {nombre}! Te habla Chuda, tu amiga personal. Aquí vas a poder encontrar la mejor opción de outfit para que te sientas cómoda y segura.\nA continuación te haremos preguntas para conocerte más y darte la opción que más te favorece.")
    dni_usuario = input("Ingrese numero de DNI sin puntos ni espacios: ")
    nombre_archivo = "textos/" + dni_usuario + ".txt"
    with open(f"{nombre_archivo}", "x") as archivo_respuesta:
        archivo_respuesta.write(f"Hola {nombre}. Estos son algunos comentarios acerca de tus respuestas: ")
    return nombre_archivo

def preguntas(nombre_archivo):
    contador = 0
    print("¿Cuál es tu estatura?")
    print("A) Menos de 1,58 m\nB) Entre 1,58 m y 1,68 m\nC) Más de 1,68 m")
    respuesta = input("Respuesta (A/B/C): ").upper()
    if respuesta == "A":
        with open(nombre_archivo, "a") as f: f.write("\n1. Tu altura es baja, ¿Sos mayor de edad? Pareces de 12.")
    elif respuesta == "B":
        with open(nombre_archivo, "a") as f: f.write("\n1. No sos bajo, sos promedio... pero meh.")
    elif respuesta == "C":
        with open(nombre_archivo, "a") as f: f.write("\n1. Sos muy alta, pareces una jirafa.")

    print("¿Cuál es tu peso aproximado?")
    print("A) Menos de 50 kg\nB) Entre 50 y 70 kg\nC) Más de 70 kg")
    respuesta = input("Respuesta (A/B/C): ").upper()
    if respuesta == "A":
        with open(nombre_archivo, "a") as f: f.write("\n2. Un poquito más de comida no te haría nada mal.")
    elif respuesta == "B":
        with open(nombre_archivo, "a") as f: f.write("\n2. Tu peso es normalito...")
    elif respuesta == "C":
        with open(nombre_archivo, "a") as f: f.write("\n2. Sos media grandota.")

    print("¿Qué forma se parece más a tu tipo de cuerpo?")
    print("A) Hombros más anchos que caderas\nB) Cintura marcada, hombros y caderas proporcionales\nC) Medidas similares, pocas curvas\nD) Cadera más anchas que hombros")
    respuesta = input("Respuesta (A/B/C/D): ").upper()
    if respuesta == "A":
        contador += 50
        with open(nombre_archivo, "a") as f: f.write("\n3. El cuerpo triángulo invertido, tu tipo de cuerpo, no es tan femenino.")
    elif respuesta == "B":
        contador += 200
        with open(nombre_archivo, "a") as f: f.write("\n3. El cuerpo reloj de arena, tu tipo de cuerpo, es el estereotipo ideal, ¿lo conseguiste de manera natural? ")
    elif respuesta == "C":
        contador += 100
        with open(nombre_archivo, "a") as f: f.write("\n3. Al cuerpo rectángulo, tu tipo de cuerpo, le falta un poquito de forma.")
    elif respuesta == "D":
        contador += 150
        with open(nombre_archivo, "a") as f: f.write("\n3. Al cuerpo pera, tu tipo de cuerpo, le sobra cadera para tus hombritos.")

    print("¿Cuál es tu tono de piel?")
    print("A) Piel clara\nB) Piel intermedia\nC) Piel morena/oscura")
    respuesta = input("Respuesta (A/B/C): ").upper()
    if respuesta == "A":
        with open(nombre_archivo, "a") as f: f.write("\n4. Sos muy blanca, pareces un fantasma.")
    elif respuesta == "B":
        with open(nombre_archivo, "a") as f: f.write("\n4. Ni muy clara ni muy oscura, color promedio.")
    elif respuesta == "C":
        with open(nombre_archivo, "a") as f: f.write("\n4. Tu tono es raro, como sucio.")

    return contador

def mostrar_recomendacion(contador):
    if contador == 200:
        archivo = "data_cuerpo/cuerpo_reloj.txt"
    elif contador == 50:
        archivo = "data_cuerpo/cuerpo_triángulo.txt"
    elif contador == 100:
        archivo = "data_cuerpo/cuerpo_rectangulo.txt"
    elif contador == 150:
        archivo = "data_cuerpo/cuerpo_pera.txt"
    else:
        print("Ocurrió un error.")
        return
    with open(archivo, "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    archivo_usuario = funcion_bienvenida()
    puntaje = preguntas(archivo_usuario)
    mostrar_recomendacion(puntaje)
