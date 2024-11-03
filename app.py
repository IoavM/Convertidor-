import streamlit as st
import ffmpeg
import gdown
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

st.title("Conversor de MKV a MP3 desde Google Drive")
google_drive_link = st.text_input("Pega el enlace de Google Drive del archivo .mkv")

if google_drive_link:
    st.write("Descargando archivo desde Google Drive...")
    try:
        # Convertir el enlace de Google Drive a formato de descarga directa
        file_id = google_drive_link.split('/')[-2]
        download_url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(download_url, "input.mkv", quiet=False)

        output_path = "output.mp3"
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
    except Exception as e:
        st.error("Error al descargar el archivo.")
        st.write(e)

