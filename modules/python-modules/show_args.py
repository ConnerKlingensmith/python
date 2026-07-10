import sys

print(f"Script name: {sys.argv[0]}")
print(f"Number of arguments: {len(sys.argv)}")
print(f"All arguments: {sys.argv}")

# Print each argument
for i, arg in enumerate(sys.argv):
    print(f" argv[{i}] = {arg}")
