from flask import render_template, request, redirect, url_for
from app import app, db
from models import PEDIDOS
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastroPedido', methods=['POST','GET'])
def cadastroPedido():
    if request.method == "POST":
        origem = request.form.get("origem")
        destino = request.form.get("destino")
        data_ida = request.form.get("dataIda")
        horario_ida = request.form.get("horarioIda")
        data_retorno = request.form.get("dataRetorno")
        horario_retorno = request.form.get("horarioRetorno")
        tipo_veiculo = request.form.get("tipoVeiculo")
        guia = (request.form.get("guiaSim")) or (request.form.get("guiaNao"))
        data = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        status = 1
        id_agencia = 1

        pedido = PEDIDOS(id_agencia = id_agencia, origem=origem, destino=destino, data_ida=data_ida, horario_ida=horario_ida, data_retorno=data_retorno, \
                          horario_retorno=horario_retorno, tipo_veiculo=tipo_veiculo, guia=guia, data = data, hora = hora, status = status)
        db.session.add(pedido)
        db.session.commit()
        return redirect(url_for("index")) 

if __name__ == "__main__":
    app.run(debug=True)
