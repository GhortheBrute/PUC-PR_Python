import json

lista = [10, 11, 12, 13, 14, 15]
with open('Teste.json', 'w') as t:
    json.dump(lista, t)

with open('Teste.json', 'r') as t:
    lista_lida = json.load(t)
    print(lista_lida)
print(lista)
lista = [1, 2, 3, 4, 5, 6]
with open('Teste.json', 'w') as t:
    json.dump(lista, t)

with open('Teste.json', 'r') as t:
    lista_lida = json.load(t)
    print(lista_lida)
print(lista)
lista_vazia = []
cont = 0
teste_id = {'id': 1, 'Name': 'Fulano'}
lista_vazia.append(teste_id)
with open('Indice.json', 'w', encoding='utf-8') as file:
    json.dump(lista_vazia, file)


def pegar_ultimo_id():
    try:
        with open('Indice.json', 'r', encoding='utf-8') as file:
            listagem = json.load(file)
            contagem = [entry['id'] for entry in listagem]
            ultimo_id = max(contagem)
    except:
        ultimo_id = 0

    return ultimo_id + 1


novo_teste = {'id': pegar_ultimo_id(), 'Nome': 'Afonso'}
lista_vazia.append(novo_teste)
with open('Indice.json', 'w', encoding='utf-8') as file:
    json.dump(lista_vazia, file)


def pesquisar_id(id):
    with open('Indice.json', 'r', encoding='utf-8') as file:
        b = json.load(file)
        if id in b:
            print('SIM')
        else:
            print('NÃO')


pesquisar_id(1)
