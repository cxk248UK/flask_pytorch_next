from flask import Flask, render_template
from api import model

app = Flask(__name__)

app.register_blueprint(model.bp)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")
