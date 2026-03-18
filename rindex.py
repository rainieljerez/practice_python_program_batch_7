#Prog10. rindex() return the first location of the function parameter in the string starting
#from the last character. Create a program that do the same functionality without using rindex() function.

text = input("Enter the main string: ")
sub = input("Enter substring to find from right: ")

found_index = -1
# range(start, stop, step) -> loops backward
for i in range(len(text) - len(sub), -1, -1):
    if text[i:i+len(sub)] == sub:
        found_index = i
        break

if found_index != -1:
    print(f"Last found at index: {found_index}")
else:
    print("Substring not found.")
