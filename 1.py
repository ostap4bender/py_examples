bro = ''.join(list(map(lambda x: x.upper(), 'brouh')))
print(f'Go кодить, {bro}!1!')

print('Нужна ветка')
GREEN = 'gg_reen'


def green_metro_branch(is_green):
    print(is_green, end=3*'\t')
    if is_green in ['green', 'GREEN', GREEN, ]:
        return 'Great'
    return 'Try "GRE(EE)EN"'


import random

colors = (['green', 'red  ', 'green', 'yellow',
           'green', 'white', 'green', 'BLM  ', ])
for _ in range(10): print(green_metro_branch(random.choice(colors)))


print('Ура, я = MAIN')
print('__CODE_FOR_GET_PRIME_DIVIDERS__')


def get_div(a, div):
    for i in range(2, int(a**0.5)+1):
        if a % i == 0: return get_div(a / i, div + [i])
    return div + [int(a)]


for i in range(1, 10**4):
    print(i, get_div(i, []), sep=' -> ')

