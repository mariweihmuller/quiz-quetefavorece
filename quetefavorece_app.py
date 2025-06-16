import streamlit as st
import os

st.set_page_config(page_title="¿Qué te favorece?", page_icon="👗")
st.title("👋 ¡Bienvenida a -Qué te favorece-!")

# Inicializar variables de sesión
if "step" not in st.session_state:
    st.session_state.step = 0
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "dni" not in st.session_state:
    st.session_state.dni = ""
if "comentarios" not in st.session_state:
    st.session_state.comentarios = []
if "contador" not in st.session_state:
    st.session_state.contador = 0

# Paso 0: Bienvenida y registro
if st.session_state.step == 0:
    st.write("Por favor, ingresá tus datos para comenzar:")
    st.session_state.nombre = st.text_input("¿Cómo es tu nombre?:", st.session_state.nombre)
    st.session_state.dni    = st.text_input("Ingrese su número de DNI sin puntos ni espacios:", st.session_state.dni)
    if st.button("Iniciar quiz"):
        if st.session_state.nombre.strip() and st.session_state.dni.strip():
            st.session_state.step = 1
        else:
            st.error("Tenés que completar ambos campos para continuar.")

# Paso 1: Pregunta altura
elif st.session_state.step == 1:
    altura = st.radio("¿Cuál es tu estatura?", ["A) Menos de 1,58 m", "B) Entre 1,58 m y 1,68 m", "C) Más de 1,68 m"])
    if st.button("Confirmar altura"):
        if "A" in altura:
            st.session_state.comentarios.append("1. Tu altura es baja, ¿Sos mayor de edad? Pareces de 12.")
        elif "B" in altura:
            st.session_state.comentarios.append("1. No sos bajo, sos promedio... pero meh.")
        else:
            st.session_state.comentarios.append("1. Sos muy alta, pareces una jirafa.")
        st.session_state.step = 2

# Paso 2: Pregunta peso
elif st.session_state.step == 2:
    peso = st.radio("¿Cuál es tu peso aproximado?", ["A) Menos de 50 kg", "B) Entre 50 y 70 kg", "C) Más de 70 kg"])
    if st.button("Confirmar peso"):
        if "A" in peso:
            st.session_state.comentarios.append("2. Un poquito más de comida no te haría nada mal.")
        elif "B" in peso:
            st.session_state.comentarios.append("2. Tu peso es normalito...")
        else:
            st.session_state.comentarios.append("2. Sos media grandota.")
        st.session_state.step = 3

# Paso 3: Pregunta tipo de cuerpo
elif st.session_state.step == 3:
    cuerpo = st.radio("¿Qué forma se parece más a tu tipo de cuerpo?", [
        "A) Hombros más anchos que caderas",
        "B) Cintura marcada, hombros y caderas proporcionales",
        "C) Medidas similares, pocas curvas",
        "D) Cadera más anchas que hombros"
    ])
    if st.button("Confirmar cuerpo"):
        if "A" in cuerpo:
            st.session_state.comentarios.append("3. El cuerpo triángulo invertido, tu tipo de cuerpo, no es tan femenino.")
            st.session_state.contador += 50
        elif "B" in cuerpo:
            st.session_state.comentarios.append("3. El cuerpo reloj de arena, tu tipo de cuerpo, es el estereotipo ideal, ¿lo conseguiste de manera natural? ")
            st.session_state.contador += 200
        elif "C" in cuerpo:
            st.session_state.comentarios.append("3. Al cuerpo rectángulo, tu tipo de cuerpo, le falta un poquito de forma.")
            st.session_state.contador += 100
        else:
            st.session_state.comentarios.append("3. Al cuerpo pera, tu tipo de cuerpo, le sobra cadera para tus hombritos.")
            st.session_state.contador += 150
        st.session_state.step = 4

# Paso 4: Pregunta tono de piel
elif st.session_state.step == 4:
    piel = st.radio("¿Cuál es tu tono de piel?", ["A) Piel clara", "B) Piel intermedia", "C) Piel morena/oscura"])
    if st.button("Confirmar piel"):
        if "A" in piel:
            st.session_state.comentarios.append("4. Sos muy blanca, pareces un fantasma.")
        elif "B" in piel:
            st.session_state.comentarios.append("4. Ni muy clara ni muy oscura, color promedio.")
        else:
            st.session_state.comentarios.append("4. Tu tono es raro, como sucio.")
        st.session_state.step = 5

# Paso 5: Resultado final y archivo
elif st.session_state.step == 5:
    st.success(f"Tu puntaje total es: {st.session_state.contador}")
    st.markdown("---")
    st.markdown("### Recomendación final de Chuda 🐼")

    # Elegir archivo de recomendación
    rutas = {
        200: "cuerpo_reloj.txt",
        150: "cuerpo_pera.txt",
        100: "cuerpo_rectangulo.txt",
        50:  "cuerpo_triángulo.txt"
    }
    archivo_reco = rutas.get(st.session_state.contador)
    if archivo_reco and os.path.exists(archivo_reco):
        with open(archivo_reco, "r", encoding="utf-8") as f:
            st.text(f.read())
    else:
        st.error("No se encontró una recomendación adecuada. Revisá tus respuestas.")

    # Guardar el archivo de comentarios
    nombre_archivo = f"{st.session_state.dni}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"Hola {st.session_state.nombre}. Estos son algunos comentarios acerca de tus respuestas:\n")
        for c in st.session_state.comentarios:
            f.write(c + "\n")

    st.markdown("---")
    st.markdown("### Archivo con comentarios:")
    st.text("\n".join(st.session_state.comentarios))
