def Table(n):
    
    if n==0 or n<0:
        print("NULL")

    else:
        for i in range (1,n+1):
            print(i*9)



n=int(input())
Table(n)

