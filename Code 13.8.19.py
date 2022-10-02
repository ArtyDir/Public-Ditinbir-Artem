ticket = int(input('Какое количество билетов хотите приобрести?'))
price = []
for i in range(1, ticket + 1):
    age = int(input(f'Возраст {i} посетителя'))
    if age < 18:
        price.append(0)
    elif 18 <= age <= 25:
        price.append(990)
    elif age > 25:
        price.append(1390)
print('Ваша цена билета(ов) -', price)
if ticket > 3:
    a = int(sum(price) - sum(price)/10)
    print('Сумма покупки со скидкой 10%:', a)
else:
    a = sum(price)
    print ('Сумма покупки:', a)
