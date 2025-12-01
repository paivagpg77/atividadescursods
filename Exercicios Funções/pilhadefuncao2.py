def g1(x):
    if x > 0 :
        if x % 3 == 0 :
            g2(x-2)
        else:
            g3(x-1)
    else:
        print('g1 TERMINOU:', x)

def g2(x):
    if x > 8:
        print('g2 reduzido:' ,x)
        g3(x-4)
    else:
        x = x + 2 
        print('g2 valor final:' , x)
def g3(x):
    if x > 15:
        for i in range(3):
            x-=3
            print('g3 laço:', x)
    else:
        print('g3 final:',x)
    g1(x)
g1(47)