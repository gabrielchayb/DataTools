from flask import Flask, render_template, request, jsonify, json, redirect, make_response, send_file
import json
from sidemodules.databasehandler import send_data, get_data
import webbrowser
from datetime import datetime
app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')
    

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/cadastroempresas", methods=['GET', 'POST'])
def cadempresas():
    if request.method == 'GET':
         return render_template('cadastroempresas.html')
    else:
        registro = request.form.to_dict()
        now = datetime.now()
        now = now.strftime('%d-%m-%Y_%H:%M:%S')
        registro['timeregister'] = now
        print(registro)
        send_data(registro,'empresas')
        return redirect('home')

@app.route("/cadastroindicacoes", methods=['GET', 'POST'])
def cadindicacoes():
    if request.method == 'GET':
         return render_template('cadastroindicacoes.html')
    else:
        registro = request.form.to_dict()
        now = datetime.now()
        now = now.strftime('%d-%m-%Y_%H:%M:%S')
        registro['timeregister'] = now
        print(registro)
        send_data(registro,'indicadores')
        return redirect('home')

@app.route("/cadastrovendas", methods=['GET', 'POST'])
def cadvendas():
    if request.method == 'GET':
         return render_template('cadastrovendas.html')
    else:
        registro = request.form.to_dict()
        now = datetime.now()
        now = now.strftime('%d-%m-%Y_%H:%M:%S')
        registro['timeregister'] = now
        print(registro)
        send_data(registro,'vendas')
        return redirect('home')

@app.route("/verempresas")
def veremp():
    data = json.loads(get_data('empresas'))

    return render_template('verempresas.html', bananinha=data)

@app.route("/verindicacoes")
def verind():
    data = json.loads(get_data('indicadores'))

    return render_template('verindicacoes.html', bananinha=data)

@app.route("/vervendas")
def vervendas():
    data = json.loads(get_data('vendas'))

    return render_template('vervendas.html', bananinha=data)

if __name__== "__main__":
    app.run(debug=True)


