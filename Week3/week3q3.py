def print_longest_string():

    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    len1 = len(str1)
    len2 = len(str2)

    if len1 > len2:
        print(f"The longer string is: {str1}")
    elif len2 > len1:
        print(f"The longer string is: {str2}")
    else:
 
        print(f"Both strings have the same length: {str1} {str2}")

print_longest_string()
