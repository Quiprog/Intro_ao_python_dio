from datetime import date, time, datetime


def trabal():
    data_atual = datetime.now()
    data_a = data_atual.strftime('%H:%M:%S')
    # print(data_a)
    # print(data_atual)
    # print(data_atual.strftime('%c'))
    # print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2019, 5, 31, 13, 35, 36)
    print(data_criada)
    print(data_criada.strftime('%c'))


if __name__ == "__main__":
    trabal()
