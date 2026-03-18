#Prog02. removesuffix() remove the characters at the end of the string that matches
#the function parameter. Create a program that do the same functionality without using
#removesuffix() function.
text = input("Enter the main string: ")
suffix = input("Enter the suffix to remove: ")

if suffix and text[-len(suffix):] == suffix:
    print(f"Result: {text[:-len(suffix)]}")
else:
    print(f"Result: {text}")