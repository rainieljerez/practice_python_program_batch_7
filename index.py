#Prog09. index() return the first location of the function parameter in the string. Create
#a program that do the same functionality without using index() function.
text = input("Enter the main string: ")
sub = input("Enter substring to find: ")

found_index = -1
for i in range(len(text) - len(sub) + 1):
    if text[i:i+len(sub)] == sub:
        found_index = i
        break

if found_index != -1:
    print(f"Found at index: {found_index}")
else:
    print("Substring not found.")