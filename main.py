from utils import validar_email, limpiar_email, extraer_username

def procesar_emails(emails):
    """
    Procesa una lista de correos electrónicos: valida, limpia y extrae nombres de usuario.
    :param emails: Lista de correos electrónicos.
    :return: Lista de correos electrónicos válidos y limpios.
    """
    emails_limpios = []
    for email in emails:
        try:
            if validar_email(email):
                email_limpio = limpiar_email(email)
                emails_limpios.append(email_limpio)
            else:
                print(f"Correo inválido: {email}")
        except Exception as e:
            print(f"Error al procesar el correo {email}: {e}")
    return emails_limpios

def mostrar_usernames(emails):
    """
    Muestra los nombres de usuario de una lista de correos electrónicos.
    :param emails: Lista de correos electrónicos válidos.
    """
    for email in emails:
        username = extraer_username(email)
        print(f"Nombre de usuario: {username}")

if __name__ == "_main_":
    data = [" ALICE@MAIL.COM", "bob@gmail.com", "invalid_email", " charlie@live.com "]
    emails_validos = procesar_emails(data)
    mostrar_usernames(emails_validos)