if __name__ == '_main__':


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '_main__':
    app.run(debug=True)


