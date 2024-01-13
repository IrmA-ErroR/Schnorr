import time

def my_random(limit):
    # Генерация случайного числа от 1 до limit
    seed = int(time.time())
    x = (seed % (limit - 1)) + 2
    return x

def generate_g(p, q):
    # Подбираем число g, удовлетворяющее условию
    while True:
        g = my_random(p)
        if pow(g, q, p) == 1:
            return g
        
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1
