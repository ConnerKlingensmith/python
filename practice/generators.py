def fun():
    print("hello")
    return 1

a = fun()
print(a)
print("=============")

def gun():
    yield 1
    yield 10
    yield 100

g = gun()
print(next(g))
print(next(g))
print(next(g))
