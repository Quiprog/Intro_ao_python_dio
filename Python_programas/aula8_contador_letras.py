def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        print(quantidade)
        contador.append(quantidade)
    return contador

def teste():
    return 'teste'


if __name__ == '__main__':
    lista = ['rinoceronte', 'gato']
    print(contador_letras(lista))

    print(teste())

