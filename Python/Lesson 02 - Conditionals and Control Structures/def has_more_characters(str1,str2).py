def has_more_characters(str1,str2):
    result1 = len(str1)
    result2 = len(str2)
    if result1 > result2:
        return str1
    else:
        return str2
string1 = input("Enter a string!  ")
string2 = input("Enter a second string!  ")

final = has_more_characters(string1,string2)
print(final)