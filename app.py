from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/recibir_mensaje', methods=['POST'])
def recibir_mensaje():
    datos = request.json
    mensaje = datos['mensaje']
    print("Mensaje recibido:", mensaje)
    return "Flask recibió: " + mensaje

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


