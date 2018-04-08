def sum_func(x, y):
    return x + y


def div_func(x, y):
    return x // y


def wrapper(x, y, func):
    print('Идет вычисление')
    res = func(x, y)
    return res

# декоратор возвращает функцию, не влияя на её поведение

def decorator(func):
    def wrapper(x, y):
        print('Идет вычисление')
        return func(x, y)
    return wrapper


sum_with_print = decorator(sum_func)
div_with_print = decorator(div_func)

res = sum_with_print(1, 2)
print(res)
res2 = sum_with_print(3, 4)
print(res2)
res3 = div_with_print(6, 2)
print(res3)
