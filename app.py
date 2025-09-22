from flask import Flask, render_template, request, jsonify

import db

def creatab():
    db.create_table()
#        validacion = conex.execute('SELECT * FROM user WHERE name_email= ?', (hashed_user,)).fetchone()


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

@app.route("/vision", methods=['POST'])
def vision_post():
    if request.method == 'POST':
        skill = request.form['skill']
        desc = request.form['desc']
        conex = db.get_db_connection()
        validacion = conex.execute('SELECT * FROM user WHERE skill= ?', (skill,)).fetchone()
        conex.close()            
        if validacion:
            return  render_template('mision.html', alerta="El codigo de carrera ya existe")## puedo agregar un alert con codigo js
        else:
            conex = db.get_db_connection()
            conex.execute('INSERT INTO user (skill, description) VALUES (?,?)', (skill, desc))
            conex.commit()
            conex.close()
            return render_template('respuesta.html', alerta="Registro exitoso") # puedo agregar un alert con codigo js
    else:
        return f"No ha funcionado"


@app.route('/recibir_mensaje', methods=['POST'])
def recibir_mensaje():
    datos = request.json
    mensaje = datos['mensaje']
    print("Mensaje recibido:", mensaje)
    creatab()
    return "Flask recibió: " + mensaje


@app.route('/obtener_datos')
def obtener_datos():
    datos = {'nombre': 'Juan', 'edad': 30}
    return jsonify(datos)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


