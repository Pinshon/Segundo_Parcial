def validar_email(email):
    """
    Valida si un correo electrónico contiene el símbolo '@'.
    :param email: Cadena de texto que representa un correo electrónico.
    :return: True si es válido, False en caso contrario.
    """
    return "@" in email

def limpiar_email(email):
    """
    Limpia un correo electrónico eliminando espacios y convirtiéndolo a minúsculas.
    :param email: Cadena de texto que representa un correo electrónico.
    :return: Correo electrónico limpio.
    """
    return email.lower().strip()

def extraer_username(email):
    """
    Extrae el nombre de usuario de un correo electrónico (la parte antes del '@').
    :param email: Cadena de texto que representa un correo electrónico.
    :return: Nombre de usuario.
    """
    return email.split("@")[0]