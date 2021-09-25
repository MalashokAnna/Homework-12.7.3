per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите число:")
c = float(money)
L = per_cent.values()

def umnozenije(n): return c*n/100

deposit = list(map(umnozenije, L))
D = max(deposit)
print("Максимальная сумма, которую вы можете заработать -", D)






