from flask import Flask

app = Flask(__name__)


@app.route('/carros')
def getCars():
    print('ola')


app.run()
