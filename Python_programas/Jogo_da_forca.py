# palavra = input("Digite a palavra secreta:").lower().strip()
# for x in range(100):
#     print()
# digitadas = []
# acertos = []
# erros = 0
# while True:
#     senha = ""
#     for letra in palavra:
#         senha += letra if letra in acertos else "."
#     print(senha)
#     if senha == palavra:
#         print("Você acertou!")
#         break
#     tentativa = input("\nDigite uma letra:").lower().strip()
#     if tentativa in digitadas:
#         print("Você já tentou esta letra!")
#         continue
#     else:
#         digitadas += tentativa
#         if tentativa in palavra:
#             acertos += tentativa
#         else:
#             erros += 1
#             print("Você errou!")
#     print("X==:==\nX  :   ")
#     print("X  O   " if erros >= 1 else "X")
#     linha2 = ""
#     if erros == 2:
#         linha2 = "  |   "
#     elif erros == 3:
#         linha2 = " \|   "
#     elif erros >= 4:
#         linha2 = " \|/ "
#     print("X%s" % linha2)
#     linha3 = ""
#     if erros == 5:
#         linha3 += " /     "
#     elif erros >= 6:
#         linha3 += " / \ "
#     print("X%s" % linha3)
#     print("X\n===========")
#     if erros == 6:
#         print("Enforcado!")
#         break


# class Fogao:
#     def __init__(self):
#         self.boca_liga = False
#         self.nivel = 1
#
#
#     def Power(self):
#         if self.boca_liga:
#             self.boca_liga = False
#         else:
#             self.boca_liga = True
#
#     def Reg_aum(self):
#         if self.boca_liga is True:
#             if self.nivel < 3:
#                 self.nivel += 1
#             else:
#                 print('Esta boca já está no nível máximo (nível 3)')
#         else:
#             print('Esta boca está desligada, lique-a primeiro')
#
#     def Reg_dim(self):
#         if self.boca_liga is True:
#             if self.nivel < 1:
#                 self.nivel -= 1
#             else:
#                 print('Esta boca já está no nível mínimo (nível 1)')
#         else:
#             print('Esta boca está desligada, lique-a primeiro')
#
#
# fogao = Fogao()
# print(fogao.boca_liga)
# fogao.Power()
# print(fogao.boca_liga)
# fogao.Reg_aum()
#
# fogao.Reg_dim()
#
# print(fogao.nivel)

class Classe_1:
  def funcao_da_classe_1(self, string):
    dicionario = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 100, 'D' : 500, 'M' : 1000}
    valor = 0
    for i in range(len(string)):
      if i > 0 and dicionario[string[i]] > dicionario[string[i - 1]]:
        valor += dicionario[string[i]] - 2 * dicionario[string[i - 1]]
      else:
        valor += dicionario[string[i]]
      return valor

b = Classe_1.funcao_da_classe_1('','V')
print(b)
