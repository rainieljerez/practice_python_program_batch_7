#Prog05. startswith() check if the string beginning part matches the function parameter.
#Create a program that do the same functionality without using startswith() function.

text = input("Enter the main string: ")
prefix = input("Enter the prefix to check: ")

is_match = text[:len(prefix)] == prefix
print(f"Starts with '{prefix}': {is_match}")