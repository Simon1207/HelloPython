import requests
from colorama import Fore, Back, Style



params = {
    "api_key": "DEMO_KEY"
}
r = requests.get("https://api.nasa.gov/planetary/apod", params=params)

if r.status_code == 200:
    results = r.json()
    url = results["url"]
    # Si es una imagen guardar el archivo.
    if results["media_type"] == "image":
        with open("apod.jpg", "wb") as f:
            f.write(requests.get(url).content)
            print(Fore.GREEN,"Imagen recibida desde el satelite, se a guardado una imagen con el nombre apod.jpg")
    else:
        print(url)
else:
    print("No se pudo obtener la imagen.")