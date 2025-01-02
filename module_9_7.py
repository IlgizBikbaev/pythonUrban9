def is_prime(func):
    def num_type(*args):
        res = func(*args)
        if res <= 1:
            print(f'Число не простое и не сложное')
        for i in range(2, int(res ** 0.5) + 1):
            if res % i == 0:
                print(f'Число cocтавное')
            else:
                print(f'Число простое')
            return res
    return num_type



@ is_prime
def sum_three(a: int, b: int, c: int):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)