# lista_media = []
# def media_notas(nome_arquivo):
#     arquivo = open(nome_arquivo, 'r')
#     aluno_nota = arquivo.read()
#     # print(aluno_nota)
#     aluno_nota = aluno_nota.split('\n')
#     # print(aluno_nota)
#     # print(aluno_nota)
#     for x in aluno_nota:
#         # print(aluno_nota)
#         lista_notas = x.split(',')
#         # print(lista_notas)
#         aluno = lista_notas[0]
#         lista_notas.pop(0)
#         # print(aluno)
#         # print(lista_notas)
#         media = lambda notas: sum([int(i) for i in notas]) / 4
#         # print(media(lista_notas))
#         lista_media.append({aluno:media(lista_notas)})
#         # print(lista_media)
#     return(lista_media)
#
#
# if __name__ == '__main__':
#     media_notas('notas.txt')
#     lista_media = media_notas('notas.txt')
#     print(lista_media)
#     # aluno = '\n Meire, 8, 5, 5, 10'
#     # atualizar_arquivo('notas.txt', aluno)'

import json
import requests

r = requests.post('http://httpbin.org/stream/20', stream=True)

for line in r.iter_lines():

    # filtrar novas linhas de keep-alive
    if line:
        print json.loads(line)