# Read File
with open("text.txt", "r") as file:
    content = file.read()
    print(content)

# Write into file
with open("text.txt", "w") as file:
    content = file.write("Overwriting the text.txt file.\n")
    print(content)

# Append to file
with open("text.txt", "a+") as file:
    content = file.write("my name is conner.\n")
    print(content)
    print(file.read())


