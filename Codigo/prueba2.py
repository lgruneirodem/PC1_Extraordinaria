import os
from pytube import YouTube

# Carpeta base donde se guardarán las descargas
base_folder = "Descargas_Recetas"

# Crear la carpeta base si no existe
if not os.path.exists(base_folder):
    os.makedirs(base_folder)

# Lista de URL de videos de recetas de YouTube
urls = [
    "https://youtu.be/STN35aO6ISY"
    # Agrega aquí más URLs de videos de recetas
]

# Recorrer las URLs y descargar los videos
for url in urls:
    try:
        yt = YouTube(url)
        video_title = yt.title

        # Crear una carpeta para el tipo de receta si no existe
        recipe_folder = os.path.join(base_folder, yt.author)
        if not os.path.exists(recipe_folder):
            os.makedirs(recipe_folder)

        # Descargar el video en la carpeta correspondiente
        video_file = yt.streams.first().download(output_path=recipe_folder)

        print(f"Se ha descargado el video '{video_title}' en la carpeta '{recipe_folder}'.")

    except Exception as e:
        print(f"No se pudo descargar el video de la URL '{url}'. Error: {str(e)}")
