#Prog04. islower() check if all characters of the string is on lower case. Create a
#program that do the same functionality without using islower() function.

text = input("Enter a string to check if lower: ")
has_alpha = False
is_lower = True

for char in text:
    if 'A' <= char <= 'Z':
        is_lower = False
        break
    if 'a' <= char <= 'z':
        has_alpha = True

print(f"Result: {is_lower and has_alpha}")