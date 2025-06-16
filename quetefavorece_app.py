import streamlit as st
import os

st.set_page_config(page_title="¿Qué te favorece?", page_icon="👗")
st.title("👋 ¡Bienvenida a -Qué te favorece-!")

# Iniciar sección de bienvenida
if "inicio" not in st.session_state:
    st.session_state.inicio = False
if "nombre_archivo" not in st.session_state:
    st.session_state.nombre_archivo = ""
if "contador" not in st.session_state:
    st.session_state.contador = 0
if "respuestas" not in st.session_state:
    st.session_state.respuestas = []

# Paso 1: Bienvenida
if not st.session_state.inicio:
    nombre = st.text_input("¿Cómo es tu nombre?:")
    dni = st.text_input("Ingrese su número de DNI sin puntos ni espacios:")
    if nombre and dni:
        nombre_archivo = f"{dni}.txt"
        with open(nombre_archivo, "x") as f:
            f.write(f"Hola {nombre}. Estos son algunos comentarios acerca de tus respuestas: ")
        st.session_state.nombre_archivo = nombre_archivo
        st.session_state.inicio = True
        st.success("¡Hola " + nombre + "! Te habla Chuda, tu amiga personal. Aquí vas a poder encontrar la mejor opción de outfit para que te sientas cómoda y segura. A continuación te haremos preguntas para conocerte más y darte la opción que más te favorece.")
        st.experimental_rerun()

# Paso 2: Preguntas
elif st.session_state.inicio:
    nombre_archivo = st.session_state.nombre_archivo

    # Pregunta 1
    altura = st.radio("¿Cuál es tu estatura?", ["A) Menos de 1,58 m", "B) Entre 1,58 m y 1,68 m", "C) Más de 1,68 m"])
    if st.button("Confirmar altura"):
        if "A" in altura:
            comentario = "\n1. Tu altura es baja, ¿Sos mayor de edad? Pareces de 12."
        elif "B" in altura:
            comentario = "\n1. No sos bajo, sos promedio... pero meh."
        elif "C" in altura:
            comentario = "\n1. Sos muy alta, pareces una jirafa."
        with open(nombre_archivo, "a") as f:
            f.write(comentario)
        st.session_state.respuestas.append("altura")
        st.experimental_rerun()

    elif "altura" in st.session_state.respuestas:
        # Pregunta 2
        peso = st.radio("¿Cuál es tu peso aproximado?", ["A) Menos de 50 kg", "B) Entre 50 y 70 kg", "C) Más de 70 kg"])
        if st.button("Confirmar peso"):
            if "A" in peso:
                comentario = "\n2. Un poquito más de comida no te haría nada mal."
            elif "B" in peso:
                comentario = "\n2. Tu peso es normalito..."
            elif "C" in peso:
                comentario = "\n2. Sos media grandota."
            with open(nombre_archivo, "a") as f:
                f.write(comentario)
            st.session_state.respuestas.append("peso")
            st.experimental_rerun()

    elif "peso" in st.session_state.respuestas:
        # Pregunta 3
        cuerpo = st.radio("¿Qué forma se parece más a tu tipo de cuerpo?", [
            "A) Hombros más anchos que caderas",
            "B) Cintura marcada, hombros y caderas proporcionales",
            "C) Medidas similares, pocas curvas",
            "D) Cadera más anchas que hombros"])
        if st.button("Confirmar cuerpo"):
            if "A" in cuerpo:
                comentario = "\n3. El cuerpo triángulo invertido, tu tipo de cuerpo, no es tan femenino."
                st.session_state.contador += 50
            elif "B" in cuerpo:
                comentario = "\n3. El cuerpo reloj de arena, tu tipo de cuerpo, es el estereotipo ideal, ¿lo conseguiste de manera natural? "
                st.session_state.contador += 200
            elif "C" in cuerpo:
                comentario = "\n3. Al cuerpo rectángulo, tu tipo de cuerpo, le falta un poquito de forma."
                st.session_state.contador += 100
            elif "D" in cuerpo:
                comentario = "\n3. Al cuerpo pera, tu tipo de cuerpo, le sobra cadera para tus hombritos."
                st.session_state.contador += 150
            with open(nombre_archivo, "a") as f:
                f.write(comentario)
            st.session_state.respuestas.append("cuerpo")
            st.experimental_rerun()

    elif "cuerpo" in st.session_state.respuestas:
        # Pregunta 4
        piel = st.radio("¿Cuál es tu tono de piel?", ["A) Piel clara", "B) Piel intermedia", "C) Piel morena/oscura"])
        if st.button("Confirmar piel"):
            if "A" in piel:
                comentario = "\n4. Sos muy blanca, pareces un fantasma."
            elif "B" in piel:
                comentario = "\n4. Ni muy clara ni muy oscura, color promedio."
            elif "C" in piel:
                comentario = "\n4. Tu tono es raro, como sucio."
            with open(nombre_archivo, "a") as f:
                f.write(comentario)
            st.session_state.respuestas.append("piel")
            st.experimental_rerun()

    elif "piel" in st.session_state.respuestas:
        st.success(f"Tu puntaje total es: {st.session_state.contador}")

        st.markdown("---")
        st.markdown("### Recomendación final de Chuda 🐼")
        if st.session_state.contador == 200:
            archivo_reco = "cuerpo_reloj.txt"
        elif st.session_state.contador == 150:
            archivo_reco = "cuerpo_pera.txt"
        elif st.session_state.contador == 100:
            archivo_reco = "cuerpo_rectangulo.txt"
        elif st.session_state.contador == 50:
            archivo_reco = "cuerpo_triángulo.txt"
        else:
            archivo_reco = None

        if archivo_reco and os.path.exists(archivo_reco):
            with open(archivo_reco, "r", encoding="utf-8") as f:
                st.text(f.read())
        else:
            st.error("No se encontró una recomendación adecuada. Revisá tus respuestas.")

        with open(nombre_archivo, "r", encoding="latin-1") as f:
            st.markdown("---")
            st.markdown("### Archivo con comentarios:")
            st.text(f.read())

