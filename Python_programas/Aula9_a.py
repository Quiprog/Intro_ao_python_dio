
arquivo = open('texto_teste.txt', 'w')
arquivo.write(' Minha primeira escrita.')
arquivo.close()

arquivo = open('texto_teste.txt', 'a')
arquivo.write('\n Minha terceira escrita.')
arquivo.close()

arquivo = open('texto_teste.txt', 'r')
texto = arquivo.read()
print(texto)



