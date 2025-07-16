# Paso 1: pedir al usuario que escriba su correo
correo_original = [" ALICE@MAIL.COM", "bob@gmail.com", "invalid_email", " charlie@live.com "]

# Paso 2: limpiar el correo
def limpiar_email(correos):
    # Elimina espacios y convierte a minúsculas cada correo
    return [correo.strip().lower() for correo in correos]

correo_limpio = limpiar_email(correo_original)

# Definir la función para validar el correo
def validar_email(email):
    # Validación básica: debe contener @ y al menos un punto después del @
    if "@" not in email:
        return False

    # Verificar que haya texto antes y después del @
    partes = email.split('@')
    if len(partes) != 2 or not partes[0] or not partes[1]:
        return False
    
    # Verificar que el dominio tenga al menos un punto
    if '.' not in partes[1]:
        return False
    
    # Verificar que haya texto después del último punto
    dominio_partes = partes[1].split('.')
    if not dominio_partes[-1]:
        return False
    
    return True
# Definir la función para obtener el nombre de usuario
def obtener_usuario(email):
    # Extrae la parte antes del '@'
    return email.split('@')[0]

# Paso 3: validar todos los correos
print("Validación de correos:")
correo_limpio
for i, email in enumerate(correo_limpio):
    if validar_email(email):
        print(f" El correo '{email}' es válido.")
    
        # Paso 4: extraer el nombre de usuario
        usuario = obtener_usuario(email)
        print(f"   Nombre de usuario: {usuario}")
    else:
        print(f" El correo '{email}' no es válido. Formato incorrecto.")

# Crear listas de correos válidos e inválidos
correos_validos = [email for email in correo_limpio if validar_email(email)]
correos_invalidos = [email for email in correo_limpio if not validar_email(email)]

print("\nResumen:")
print(f"Total de correos: {len(correo_limpio)}")
print(f"Correos válidos ({len(correos_validos)}):")
for email in correos_validos:
    print(f"  - {email}")
print(f"Correos inválidos ({len(correos_invalidos)}):")
for email in correos_invalidos:
    print(f"  - {email}")