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
    return (div + [int(a)]) * (a >= 2)  # if a <2 -> []


# for i in range(0, 10**4):
#     print(i, get_div(i, []), sep=' -> ')


print('Хочу merge-ить')
print('__CODE_FOR_MATRIX__')


class MyMatrix:
    def __init__(self, size):
        self.size = size
        self.flag = True if self.size % 2 == 1 else False
        self.matrix = [[' ' for _ in range(size)]for _ in range(size)]
        self.begin = 0
        self.end = size-1
        self.index = 0
        self.draw_matrix()

    def draw_matrix(self):
        for i in range((self.size - self.size % 2) // 2):
            self.draw_right()
            self.draw_down()
            self.draw_left()
            self.draw_up()
            self.begin += 1
            self.end -= 1
        if self.flag: self.matrix[self.size // 2][self.size // 2] = self.index + 1
        print('FINAL')
        self.print()

    def draw_right(self):
        for i in range(self.begin, self.end + 1):
            self.index += 1
            self.matrix[self.begin][i] = self.index
            self.print()

    def draw_down(self):
        for i in range(self.begin+1, self.end + 1):
            self.index += 1
            self.matrix[i][self.end] = self.index
            self.print()

    def draw_left(self):
        for i in range(self.end-1, self.begin-1, -1):
            self.index += 1
            self.matrix[self.end][i] = self.index
            self.print()

    def draw_up(self):
        for i in range(self.end-1, self.begin, -1):
            self.index += 1
            self.matrix[i][self.begin] = self.index
            self.print()

    def print(self):
        for e in self.matrix: print(*e, sep='\t')
        print()


m = MyMatrix(10)

print('Ну когда уже merge??')



