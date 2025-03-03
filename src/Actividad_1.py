import json
import requests
import sys


class Actividad_1():
    def __init__(self):
        self.ruta_static="src/pad/static/"
        sys.stdout.reconfigure(encoding= "utf-8")

    def leer_api(self,url):
        response = requests.get(url)
        return response.json()

def escribir_json(self,nombre_archivo="",datos=None): # " " ´´ """ """
    if nombre_archivo=="":
        nombre_archivo="datos.json"
    if datos is None:
        datos= "No hay datos"
    ruta_json = "{}json/{}".format(self.ruta_static,nombre_archivo)
    try:
        with open(ruta_json, "w",encoding= "utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print("Error:",e)

    return True # booleano true (1) false (0)


# vamos a crear una instacia
ingestion = Actividad_1()
datos_json = ingestion.leer_api("https://bandsintown.com/")
print("datos json:",datos_json)

if ingestion.escribir_json(nombre_archivo="entrega_actividad_1.json",datos=datos_json):
    print("se crea el archivo json.")



