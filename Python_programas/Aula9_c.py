def atualizar_arquivo(nome_arquivo, aluno):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(aluno)
    arquivo.close()

lista_media = []
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return(lista_media)


if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)
    # aluno = '\n Meire, 8, 5, 5, 10'
    # atualizar_arquivo('notas.txt', aluno)'