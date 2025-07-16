# main.py

# Importamos las funciones que hicimos en utils.py
from utils import procesar_emails, mostrar_usuarios

if __name__ == "_main_":
    # Lista original con correos (algunos buenos, otros malos)
    datos = ["  ALICE@MAIL.COM", "bob@gmail.com", "invalid_email", " charlie@live.com "]

    # Llamamos a la función para procesar los correos
    correos_validos = procesar_emails(datos)

    # Mostramos los usuarios de los correos que sí eran válidos
    mostrar_usuarios(correos_validos)

    # Imprimimos la lista de correos válidos
    print("Correos válidos:", correos_validos)      
  
                 