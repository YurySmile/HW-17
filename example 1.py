money = int(input("Введите количество средств, которые Вы планируете положить на депозит"))
per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
a = 5.6*money/100
b = 5.9*money/100
c = 4.28*money/100
d = 4.0*money/100
profit = [a,b,c,d]
print ("Все возможные варианты, которую вы можете заработать в разных банках — ", (profit))
print ("Максимальная сумма, которую вы можете заработать — ", max(profit))