import time

def get_x(q, used_xs=None, id=0):
    if used_xs is None:
        used_xs = set()

    hash_value = 0x811c9dc5
    hash_value *= id

    current_time = int(time.time() * 1000)  # Текущее время в миллисекундах
    x_candidate = current_time % (q - 2) + 1

    while x_candidate in used_xs:
        x_candidate = (x_candidate * (hash_value % 1000000)) % (q - 1)

    used_xs.add(x_candidate)
    return x_candidate


def find_g(q, p, shift, used_gs=None):
    if used_gs is None:
        used_gs = set()

    for g in range(2 + shift, p):
        if pow(g, q, p) == 1 and g not in used_gs:
            return g
    return None


def find_y(g, x, p):
    y = 1
    for _ in range(x):
        y = (y * g) % p
    return y


if __name__ == "__main__":
    p = int(input("Введите число p: "))
    q = int(input("Введите число q: "))

    used_gs = set()

    for i in range(3):  # Пример для трех клиентов
        g = find_g(q, p, 10, used_gs)

        if g is not None:
            used_gs.add(g)
            print(f"Ответ для клиента {i + 1}: {g}")
        else:
            print(f"Не удалось найти подходящее g для клиента {i + 1}")

        q = int(input("Введите число q: "))
    
    used_xs = set()

    for i in range(3):  # Пример для трех клиентов
        x = get_x(q, used_xs)
        print(f"Сгенерированное x для клиента {i + 1}: {x}")

    g = 5  # Пример значения g
    x = 3  # Пример значения x
    p = 13  # Пример значения p

    y = find_y(g, x, p)
    print(f"Открытый ключ y: {y}")    