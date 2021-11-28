def escrever_arquivo(texto):
    # arquivo = open('C:/Users/q_lai/Documents/Tecnologia da Informação/Python/Programas/DigitalProject/Textos/texto_b.txt', 'w')
    # arquivo.write(texto)
    # arquivo.close()

def atualizar_arquivo(text_o):
    arquivo = open('C:/Users/q_lai/Documents/Tecnologia da Informação/Python/Programas/DigitalProject/Textos/texto_b.txt', 'a')
    arquivo.write(text_o)
    arquivo.close()

def ler_texto(agora):
    arquivo = open('C:/Users/q_lai/Documents/Tecnologia da Informação/Python/Programas/DigitalProject/Textos/texto_b.txt', 'r')
    agora = arquivo.read()
    print(agora)


if __name__ == '__main__':
    # escrever_arquivo('Primeira linha. \n')
    # atualizar_arquivo("Terceira linha. \n")
    ler_texto('agora')