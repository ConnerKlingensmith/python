def fct1(a,b):
    return a+b

def fct2(*args):
    mysum = sum(args)
    return mysum

if __name__ == "__main__":
    print(fct1(10,10))
    print(fct2(30,20,10))
