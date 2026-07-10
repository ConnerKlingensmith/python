def my_dec(func):
    def wrapper():
        print("Starting the function")
        func()
        print("Ending the function")
    return wrapper

@my_dec
def decorator():
    print("testing the decorator")

decorator()
