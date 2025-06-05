import requests # Librería utilizada para realizar solicitudes HTTP (POST,GET,PUT,DELETE,etc)

# URL del servidor
# Usa el nombre del contenedor 'servidor' para la red interna de Docker
URL = "http://servidor:8000/convertir"  

def enviar_numero_decimal(numero):
    # Crear el cuerpo de la solicitud como JSON
    data = {"numero": numero}

    # Convierte data a formato json y realiza la solicitud POST al servidor, 
    response = requests.post(URL, json=data)

    # Verificar el estado de la respuesta
    # Si el código de respuesta es 200, o sea respuesta exitosa
    if response.status_code == 200: 
        # Mostrar las conversiones
        resultado = response.json()
        print(f"Binario: {resultado['binario']}")
        print(f"Octal: {resultado['octal']}")
        print(f"Hexadecimal: {resultado['hexadecimal']}\n")
    else:
        # Mostrar mensaje de error
        # Busca el campo 'error' en la respuesta, si no lo encuentra, muestra la segunda cadena.
        print(f"Error: {response.json().get('error', 'No se pudo procesar el número')}") 

if __name__ == "__main__":
    while True:
        numero = input("Ingresá un número decimal (o 'salir' para salir): ")
        # Si la entrada es igual a 'salir', rompe el bucle y termina el programa.
        if numero.lower() == "salir":
            break
        try:            
            # Intentamos convertir la string ingresada a tipo 'int'
            numero = int(numero)
            print(f"Número recibido: {numero}")
            # Ejecuta la función 'enviar_numero_decimal' y le pasa como argumento el numero
            enviar_numero_decimal(numero)
        # Manejamos los valores inválidos con 'except'
        except ValueError:
            print("⚠️ Entrada no válida. Por favor, ingresá un número decimal.")
