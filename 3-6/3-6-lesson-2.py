from time import time


def decorator(func):
    def wrapper(x, y):
        print('Идет вычисление')
        before = time()
        res = func(x, y)
        print('Вычисление заняло: {}'.format(time() - before))
        return res
    return wrapper


def decorator_with_arg(need_Time=False):
    def decorator(func):
        def wrapper(x, y):
            print('Идет вычисление')
            if need_Time:
                before = time()
            res = func(x, y)
            if need_Time:
                print('Вычисление заняло: {}'.format(time() - before))
            else:
                print('Время не считали')
            return res
        return wrapper
    return decorator


@decorator_with_arg(need_Time=True)
def sum_func(x, y):
    return x + y


@decorator
def div_func(x, y):
    return x // y


res = sum_func(1, 2)
print(res)
res2 = sum_func(3, 4)
print(res2)