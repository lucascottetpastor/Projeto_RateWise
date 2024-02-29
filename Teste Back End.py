import requests
import time
from flask import Flask, request, jsonify

cache = {}
app = Flask(__name__)

def get_cotacao_moeda(moeda):
    if moeda in cache and time.time() - cache[moeda]['timestamp'] < 3600:
        print("Cotação de", moeda, "obtida do cache")
        return cache[moeda]['valor']
    else:
        response = requests.get("https://economia.awesomeapi.com.br/last/BRL-USD,EUR-USD,BTC-USD,ETH-USD")

        if response.status_code == 200:
            data = response.json()
            valor = float(data[moeda + "USD"]["bid"])
            cache[moeda] = {'valor': valor, 'timestamp': time.time()}
            
            print("Cotação de", moeda, "obtida da API e armazenada em cache")
            return valor

        else:
            print("Erro ao acessar a API:", response.status_code)
            return None



@app.route('/', methods=['GET'])
def converter_moeda():
    moeda_origem = request.args.get('from')
    moeda_destino = request.args.get('to')
    quantidade = float(request.args.get('amount'))

    if moeda_origem is None or moeda_destino is None or quantidade is None:
        return jsonify({'error': 'Parâmetros inválidos'})

    if moeda_origem == 'USD' :
        if moeda_destino in ['BRL', 'EUR', 'BTC', 'ETH']:
            valor_origem = 1 / get_cotacao_moeda(moeda_destino)
            return jsonify({
                'from': moeda_origem,
                'to': moeda_destino,
                'amount': quantidade,
                'converted_amount': valor_origem * quantidade,
                'unic': valor_origem
            })
        else:
            print('sem moeda destino')
    elif moeda_origem in ['BRL', 'EUR', 'BTC', 'ETH']:
        if moeda_destino in ['BRL', 'EUR', 'BTC', 'ETH']:
            valor_origem = get_cotacao_moeda(moeda_origem)
            valor_destino = get_cotacao_moeda(moeda_destino)
            valorFinal = valor_origem/valor_destino
            print(valor_origem, valor_destino, valorFinal)
            return jsonify({
                'from': moeda_origem,
                'to': moeda_destino,
                'amount': quantidade,
                'converted_amount': f'{valorFinal * quantidade:.8f}',
                'unic': f'{valorFinal:.8f}'
            })
        elif moeda_destino == 'USD':
            valor_origem = get_cotacao_moeda(moeda_origem)
            return jsonify({
                'from': moeda_origem,
                'to': moeda_destino,
                'amount': quantidade,
                'converted_amount': valor_origem * quantidade,
                'unic': valor_origem
            })


if __name__ == '__main__':
    app.run(debug=True)