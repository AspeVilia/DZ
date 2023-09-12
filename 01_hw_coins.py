import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None
    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.randint(0, 1)  # random.choice['heads','tails']; random.randint(0, 1)
# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
tails = 0
coins_list = []
n = int(input('Введите количество монет для генерации: '))
for _ in range(n):
    coin = Coin()
    coins_list.append(coin)
for c in coins_list:
    c.flip()
    if c.side:
        tails += 1
heads = n - tails
print(f'Орлов {heads / n:.0%}, Решек: {tails / n:.0%}')