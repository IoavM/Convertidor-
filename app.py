import streamlit as st
import ffmpeg
import os

def convertir_mkv_a_mp3(input_file, output_path):
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_path, format='mp3', acodec='libmp3lame')
            .run(overwrite_output=True)
        )
        return True
    except ffmpeg.Error as e:
        st.error("Ocurrió un error durante la conversión.")
        st.write(e)
        return False

# Interfaz de usuario con Streamlit
st.title("Conversor de MKV a MP3")
uploaded_file = st.file_uploader("Sube un archivo .mkv", type="mkv")

if uploaded_file is not None:
    output_path = "output.mp3"
    with open("input.mkv", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("Convirtiendo archivo...")
    if convertir_mkv_a_mp3("input.mkv", output_path):
        with open(output_path, "rb") as f:
            st.download_button(
                label="Descargar archivo MP3",
                data=f,
                file_name="archivo_convertido.mp3",
                mime="audio/mp3"
            )
        os.remove("input.mkv")
        os.remove(output_path)
    else:
        st.error("La conversión falló.")
