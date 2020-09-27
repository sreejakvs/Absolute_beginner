def Quadratic_eqn(a,b,c):
    p=(-b+(pow(pow(b,2)-(4*a*c),0.5)))/(2*a)
    q=(-b-(pow(pow(b,2)-(4*a*c),0.5)))/(2*a)
    print("%.2f"%p)
    print("%.2f"%q)


a=int(input())
b=int(input())
c=int(input())
Quadratic_eqn(a,b,c)