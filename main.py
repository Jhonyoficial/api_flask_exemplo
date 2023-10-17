import mysql.connector
from flask import make_response
from flask import Flask, request

mydb = mysql.connector.connect(
    host='localhost',
    user='root1',
    password='123',
    database='PycoderBr',
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/carros', methods=['GET'])
def getCars():
    my_cursor = mydb.cursor()

    my_cursor.execute('SELECT * FROM carros')
    my_carros = my_cursor.fetchall()

    carros_object = list()
    for carro in my_carros:
        carros_object.append(
            {
                'id': carro[0],
                'marca': carro[1],
                'modelo': carro[2],
                'ano': carro[3]
            }
        )

    return make_response(carros_object)


@app.route('/carros', methods=['POST'])
def postCarro():
    entrada_carro = request.get_json()
    my_cursor = mydb.cursor()
    sql = (f"insert into carros(marca, modelo, ano) "
           f"values ('{entrada_carro['marca']}', '{entrada_carro['modelo']}', {entrada_carro['ano']})")

    my_cursor.execute(sql)
    mydb.commit()

    return make_response(entrada_carro)


@app.route('/carros', methods=['PUT'])
def putCarro():
    carro_front = request.get_json()
    my_cursor = mydb.cursor()

    sql = (f"UPDATE carros set marca = '{carro_front['marca']}', modelo = '{carro_front['modelo']}', ano = {carro_front['ano']}"
           f" WHERE id = {carro_front['id']}")
    my_cursor.execute(sql)
    mydb.commit()
    my_cursor.close()

    return make_response(carro_front)


@app.route('/carros/<id>', methods=['DELETE'])
def deleteCarro(id):
    my_cursor = mydb.cursor()
    my_cursor.execute(f"DELETE FROM carros where id = {id}")
    mydb.commit()
    my_cursor.close()

    return 'sucesso'


app.run()
