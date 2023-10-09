from flask import Flask
from bd import Carros

app = Flask(__name__)


@app.route('/carros')
def getCars():
    return Carros


app.run()
