import random
def otomatik(n):
    a=0
    b=0
    for i in range(n):
        x=random.random()
        y=random.random()
        if x**2+y**2<=1:
            a=a+1
        else:
            b=b+1
            print("değer=" ,a/b)
otomatik(100000000000000)