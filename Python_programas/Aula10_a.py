from datetime import date
data_atual = date.today()
print(data_atual.strftime('%d/%m/%Y'))
print(type(data_atual))

print(data_atual.strftime('%A - %B - %Y'))

data_atual_str = data_atual.strftime('%A - %B - %Y')

print(type(data_atual_str))
