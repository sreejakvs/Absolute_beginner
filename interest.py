def SI(p,t,r):
    if p<0 or t<0 or r<0:
        print("Incorrect info")

    else:
        interest=(p*t*r)/100
        print("%.f" %interest)

p=float(input())
t=float(input())
r=float(input())
SI(p,t,r)