print("hello")

x = int(input("enter number: "))
try:
    print(x)
except:
    print("something is wrong")

print("bye")

# Raising exceptions

y = int(input("enter number between 10 and 20: "))
if(y<10 or y>20):
    raise ValueError("value should be between 10 and 20")
else:
    print(y)
