# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import itertools
from random import randint

k = int(input('Введите натуральную степень k = '))
factor = []
for i in range(1, k +2):
    factor.append(randint(1, 100))
result = []
for i in range(len(factor)):
    if k == 1:
        result.append(f'{factor[i]}*x')
    elif k == 0:
        result.append(f'{factor[i]}')
    else:
        result.append(f'{factor[i]}*x^{k}')
    signs = randint(0, 1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1
result.pop(-1)
result.append('=0')
record = open('data.txt', 'w')
record.write(''.join(result))
record.close()