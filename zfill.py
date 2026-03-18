#Prog07. zfill() add zero characters at the beginning of the string to complete the
#number of characters specifies in function parameter. Create a program that do the same
#functionality without using zfill() function.
text = input("Enter a string: ")
width = int(input("Enter total width: "))

padding = width - len(text)
result = ("0" * padding if padding > 0 else "") + text
print(f"Result: {result}")