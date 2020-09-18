def Circum(r):
    if r<0:
        print("Error")

    else:
        circum=2*3.14*r
        print("%.2f" %circum)


radius=float(input())
Circum(radius)
