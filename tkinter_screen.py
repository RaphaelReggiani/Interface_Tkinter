# Importando requests e a biblioteca Tkinker

import requests
from tkinter import *


def coletar_cotacoes():
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    cotacoes_dic = cotacoes.json()

    cot_dolar = cotacoes_dic['USDBRL']['bid']
    cot_euro = cotacoes_dic['EURBRL']['bid']
    cot_btc = cotacoes_dic['BTCBRL']['bid']

    exibir_texto = f'''

    A cotação do dólar é: {cot_dolar}.
    A cotação do euro é: {cot_euro}.
    A cotação do BitCoin é: {cot_btc}.

    '''

    texto_cotacoes['text'] = exibir_texto

janela = Tk()

janela.title('Cotações - Screen')

texto_exibir_frase_cotacoes = Label(janela, text = f'Aqui vocês pode ver as cotações.')
texto_exibir_frase_cotacoes.grid(row = 1, column = 1, padx = 50, pady = 50)

botao_clique_aqui = Button(janela, text = f'Clique aqui para ver as cotações.', command = coletar_cotacoes)
botao_clique_aqui.grid(row = 2, column = 1, padx = 50, pady = 50)

texto_cotacoes = Label(janela, text = "")
texto_cotacoes.grid(row = 3, column = 1, padx = 50, pady = 50)

janela.mainloop()