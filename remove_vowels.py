def Remove_vowels(string):
    v="aeiouAEIOU"
    c=[]
    for i in string:
        if i not in v:
            c.append(i)
            
            
    for i in c:
        print(i,end="")


    


string=input()
Remove_vowels(string)

