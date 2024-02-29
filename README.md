Desafio Técnico desenvolvedor backend Python, usando bibliotecas requests e flask.

## README:
 Este é um servidor Flask que fornece uma API para converter valores de uma moeda para outra (USD, BRL, EUR, BTC e ETH), usando as taxas de câmbio da API.<br/>
 Foi utilizado o USD como moeda de lastro, o valor foi pego da API: "https://economia.awesomeapi.com.br/"<br/>
 <br/>Aqui está uma breve explicação de como executá-lo:

## Para a execução do programa:
 Faça a instalação do Python (https://www.python.org) e siga os seguintes passos no CMD:

1 - Clonar repositório
```
git clone https://github.com/xhiowzin/backend_flask
```
2 - Entrar na pasta do arquivo
```
cd backend_flask
```
3 - Instalar requerimento
```
python -m pip install -r requirements.txt
```
4 - Executar programa
```
python TesteBackEnd.py
```
5 - Acesse a API
```
http://localhost:5000/?from=BRL&to=USD&amount=100
```

## Info:
 Altere a URL para mudar as informações.

 From - Moeda atual<br/>
 To - Moeda Final<br/>
 Amount - Quantidade<br/>
