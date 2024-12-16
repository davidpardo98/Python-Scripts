import os
from PyPDF2 import PdfMerger

def unir_pdfs_por_subcarpeta(carpeta_raiz):
    try:
        # Recorrer la carpeta raíz y sus subcarpetas
        for carpeta_actual, _, archivos in os.walk(carpeta_raiz):
            # Crear un objeto escritor de PDFs
            escritor = PdfMerger()
            archivos_pdf = [archivo for archivo in archivos if archivo.lower().endswith('.pdf')]
            
            if archivos_pdf:
                print(f"\nProcesando la carpeta: {carpeta_actual}")
                
                # Añadir los PDFs de la carpeta actual
                for archivo in archivos_pdf:
                    ruta_pdf = os.path.join(carpeta_actual, archivo)
                    print(f"Añadiendo: {ruta_pdf}")
                    escritor.append(ruta_pdf)
                
                # Crear el nombre del archivo unificado
                nombre_carpeta = os.path.basename(carpeta_actual)
                archivo_salida = os.path.join(carpeta_actual, f"{nombre_carpeta}_unificado.pdf")
                
                # Guardar el archivo unificado
                with open(archivo_salida, 'wb') as salida:
                    escritor.write(salida)
                print(f"PDFs unificados en: {archivo_salida}")
            else:
                print(f"No se encontraron PDFs en la carpeta: {carpeta_actual}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Solicitar la carpeta raíz
carpeta_raiz = input("Ingresa la ruta de la carpeta raíz: ")
unir_pdfs_por_subcarpeta(carpeta_raiz)
