import os
import shutil
import pandas as pd

# Ruta donde están las carpetas originales
ruta_origen = r"H:\_______radicar_febrero\ES"  

# Ruta donde se deben mover las carpetas
ruta_destino = r"H:\_______radicar_febrero\ES_N"

# Leer el archivo de Excel (asegurando que se lean como texto)
df = pd.read_excel(r"C:\Users\SISTEMAS\Desktop\rutas.xlsx", dtype=str)

# Recorrer el DataFrame y mover las carpetas
for index, row in df.iterrows():
    carpeta = str(row['CARPETA']).strip()  # Convertir a string y eliminar espacios extra
    destino = str(row['DESTINO']).strip()  # Convertir a string y eliminar espacios extra

    origen_carpeta = os.path.join(ruta_origen, carpeta)
    destino_carpeta = os.path.join(ruta_destino, destino)

    # Crear la carpeta de destino si no existe
    os.makedirs(destino_carpeta, exist_ok=True)

    # Mover la carpeta
    if os.path.exists(origen_carpeta):
        shutil.move(origen_carpeta, destino_carpeta)
        print(f"✅ Movida '{carpeta}' a '{destino_carpeta}'")
    else:
        print(f"⚠️ La carpeta '{carpeta}' no existe en '{ruta_origen}'")

print("🎯 Proceso completado.")