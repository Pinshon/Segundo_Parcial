# utils.py

# Verifica si un correo tiene "@" (muy básico pero útil para este caso)
def es_email_valido(email):
    return "@" in email

# Limpia el correo: lo pone en minúsculas y le quita espacios
def limpiar_email(email):
    return email.lower().strip()

# Extrae el nombre de usuario del correo (todo lo que está antes del "@")
def obtener_usuario(email):
    return email.split("@")[0]

# Esta función procesa una lista de correos: valida, limpia y los guarda si son correctos
def procesar_emails(lista_emails):
    emails_validos = []

    for email in lista_emails:
        try:
            if es_email_valido(email):
                limpio = limpiar_email(email)
                emails_validos.append(limpio)
            else:
                print("Correo inválido:", email)
        except Exception as e:
            print("Error procesando:", email, "-", str(e))
    
    return emails_validos

# Aquí mostramos solo los nombres de usuario de los correos válidos
def mostrar_usuarios(lista_emails_limpios):
    for email in lista_emails_limpios:
        usuario = obtener_usuario(email)
        print("Nombre de usuario:", usuario)