import time

class PrimeGenerator:
    def __init__(self, num_digits, shift=0):
        self.num_digits = num_digits
        self.shift = shift


    def generate_prime(self, shift):
        q = self.generate_prime_q(shift)
        p = 2 * q + 1
        while not self.is_prime(p):
            q = self.generate_prime_q(shift)
            p = 2 * q + 1
        return p, q

    def generate_prime_q(self, shift):
        while True:
            candidate = self.get_current_milliseconds() % (10 ** (self.num_digits - 1)) + 10 ** (self.num_digits - 1) + self.shift
            if self.is_prime(candidate):
                return candidate

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fermat_test(self, n, k=5):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False

        for _ in range(k):
            a = self.get_current_milliseconds() % (n - 2) + 2
            if pow(a, n - 1, n) != 1:
                return False

        return True

    @staticmethod
    def get_current_milliseconds():
        return int(round(time.time() * 1000))

if __name__ == "__main__":
    num_digits = 5  # Задайте необходимое количество цифр для простого числа p
    shift = 100  # Задайте необходимый сдвиг

    generator = PrimeGenerator(num_digits, shift)

    p, q = generator.generate_prime(shift)

    print(f"Сгенерированное простое {num_digits}-значное число p:", p)
    print(f"Сгенерированное простое число q:", q)

    # Проверки
    print("Проверка простоты числа p методом пробных делений:", generator.is_prime(p))
    print("Проверка простоты числа p тестом Ферма:", generator.fermat_test(p))

    print("Проверка простоты числа q методом пробных делений:", generator.is_prime(q))
    print("Проверка простоты числа q тестом Ферма:", generator.fermat_test(q))
