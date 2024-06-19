import xmltodict

def nomes_moedas():
    with open("moedas.xml", "rb") as arquivo_moedas:
        dic_moedas = xmltodict.parse(arquivo_moedas)

    moedas =dic_moedas["xml"]
    return moedas

def conversoes_diponiveis():
    with open("conversoes.xml", "rb") as arquivo_coversoes:
        dic_coversoes = xmltodict.parse(arquivo_coversoes)
        conversoes = dic_coversoes["xml"]
        dic_coversoes_disponiveis = {} #cria um dicionario vazio

        for par_conversao in conversoes:
            #USD-BRL
            moeda_origem, moeda_destino = par_conversao.split("-")
            if moeda_origem in dic_coversoes_disponiveis:
                dic_coversoes_disponiveis[moeda_origem].append(moeda_destino)
            else:
                dic_coversoes_disponiveis[moeda_origem] = [moeda_destino]
        return dic_coversoes_disponiveis            

#{"USD": ["BRL", "AED", "CAD", "EUR", "GBP"], "BRL": ["USD", "EUR"]}