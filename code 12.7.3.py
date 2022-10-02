per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} 
money = int(input("Введите сумму вклада:"))
deposit = []
for key in per_cent:
    per_cent[key] = int(money * per_cent[key]  /100)
    deposit.append(per_cent[key])
print(deposit)
print("Mаксимальная сумма, которую вы можете заработать -", max(deposit))
