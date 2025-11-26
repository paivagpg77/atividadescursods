def fun1(a):
    if a > 0:
        fun2 (a-1)
    else:
        print(a)
    print(a)

def fun2(a):
    if a > 5 :
        fun3(a/2)
    else:
        print(a)
    print(a)

def fun3(a):
    for i in range(3):
        a-=1
        print(a)
    if  a>0 :
        fun1(a)
    else:
        print(a)
    
fun1(15)