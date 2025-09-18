from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/mision")
def mision():
    return render_template('mision.html')

@app.route("/vision")
def vision():
    return render_template('vision.html')


@app.route('/recibir_mensaje', methods=['POST'])
def recibir_mensaje():
    datos = request.json
    mensaje = datos['mensaje']
    print("Mensaje recibido:", mensaje)
    return "Flask recibió: " + mensaje


@app.route('/obtener_datos')
def obtener_datos():
    datos = {'nombre': 'Juan', 'edad': 30}
    return jsonify(datos)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


