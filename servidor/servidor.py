from flask import Flask, request, jsonify

# Instanciamos Flask y creamos nuestra app web
app = Flask(__name__) 

# Especificamos el endpoint donde recibiremos las solicitudes POST
@app.route('/convertir', methods=['POST']) 

# Función que obtiene el número y lo convierte
def convertir():
    try:
        # Obtener el número enviado en formato JSON
        data = request.get_json()
        numero_decimal = data.get('numero', None)

        # Verificamos si numero_decimal está vacío o no es un entero:
        if numero_decimal is None or not isinstance(numero_decimal, int):
            # En este caso se devuelve código HTTP 400, solicitud inválida
            return jsonify({"error": "Se requiere un número decimal válido."}), 400

        if numero_decimal < 0: # Si el número es negativo, manejamos el signo de la siguiente manera:
            binario = '-' + bin(numero_decimal)[3:]
            octal = '-' + oct(numero_decimal)[3:]
            hexadecimal = '-' + hex(numero_decimal)[3:].upper()
        else:
            binario = bin(numero_decimal)[2:]
            octal = oct(numero_decimal)[2:]
            hexadecimal = hex(numero_decimal)[2:].upper()

        # Retornar las conversiones en formato JSON
        return jsonify({
            "binario": binario,
            "octal": octal,
            "hexadecimal": hexadecimal
        })
    # Manejamos excepciones con except. Devolvemos el mensaje del error
    # y código HTTP 500, error interno del servidor
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# Cuando se ejecuta el script direectamente, inicia el servidor web.
if __name__ == '__main__':
    # 0.0.0.0 para que el servidor Flask escuche todas las interfaces de red
    app.run(host='0.0.0.0', port=8000)
