def Remove_vowels(string):
    v="aeiouAEIOU"
    count = 0
    for i in string:
        if i in v:
            break
        else:
            count+=1
    if count == len(string):
        print("no")
    else:
        print("yes")

string=input()
Remove_vowels(string)