from datetime import date, time

def trabalhando_com_datetime():

    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    print(type(data_atual))

    print(data_atual.strftime('%A - %B - %Y'))

    data_atual_str = data_atual.strftime('%A - %B - %Y')

    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=22)
    horario_str = horario.strftime('%H: %M: %S')
    print(horario_str)
    print(type(horario_str))


if __name__ == "__main__":
    #trabalhando_com_datetime()
    trabalhando_com_time()