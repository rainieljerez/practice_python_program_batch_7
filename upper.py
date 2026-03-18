#Prog03. upper() converts all characters of the string into upper case. Create a program
# that do the same functionality without using upper() function.

text = input("Enter a string to capitalize: ")
result = ""
for char in text:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    else:
        result += char
print(f"Result: {result}")