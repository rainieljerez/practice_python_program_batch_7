#Prog08. count() return how many time the function parameter appear in the string. Create a
#program that do the same functionality without using count() function.

text = input("Enter the main string: ")
sub = input("Enter substring to count: ")

count = 0
for i in range(len(text) - len(sub) + 1):
    if text[i:i+len(sub)] == sub:
        count += 1
print(f"Occurrences: {count}")