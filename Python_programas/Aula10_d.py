from datetime import date, datetime, time, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    data_a = data_atual.strftime('%H:%M:%S')
    print(data_a)
    # print(data_atual)
    # print(data_atual.strftime('%c'))
    # print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2019, 5, 31, 13, 35, 36)
    print(data_criada)
    print(data_criada.strftime('%c'))


    data_string = '01/02/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=25)
    print(nova_data)

if __name__ == '__main__':
    trabalhando_com_datetime()



