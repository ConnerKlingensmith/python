# Print even numbers between 1 - 25
for even in range(2, 26, 2):
    print(even)

# Prompt for password if its no equal to admin@123

while True:
    password = input("Enter password: ")

    if password == "admin@123":
        print("Successfully logged in")
        break
    else:
        print("incorect password, try again")

