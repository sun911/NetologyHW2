# def f(*args, **kwargs):
#     print('args: {}'.format(args))
#     print('kwarg: {}'.format(kwargs))
#     print('+++++++++++')
#
# f()
# f(1, 2, 3)
# f(x=100, y=200)
# f(1, 2, 3, x=100)


from time import sleep


def memoize(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            print('Ключ в кеше')
            return cache[key]

        print('Ключ не в кеше')
        res = f(*args, **kwargs)
        cache[key] = res
        return res
    return wrapper

@memoize
def sum_something(x, y, z):
    sleep(1)
    return x + y + z

print(sum_something(1, 2, 3))
print(sum_something(1, 2, 3))
print(sum_something(1, 2, 3))