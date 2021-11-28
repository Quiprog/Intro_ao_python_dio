import shutil

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/q_lai/Documents/Tecnologia da Informação/Python/Programas/'
                              'DigitalProject/Textos/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,
                    'C:/Users/q_lai/Documents/Tecnologia da Informação/Python/Programas/'
                    'DigitalProject/Textos/')

if __name__ == '__main__':
    move_arquivo('notas.txt')
