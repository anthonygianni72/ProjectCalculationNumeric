import math
#M a0 a1 a2 a3 a4 a5 Nmax e1 e2 a b

entrada="2 -23 -0.112 21 0.13 -0.0004 -1 1000000 0.0001 0.0001 2904 2915"

entradaconvert=entrada.split(" ")   
M=float(entradaconvert[0])
a0=float(entradaconvert[1])
a1=float(entradaconvert[2])
a2=float(entradaconvert[3])
a3=float(entradaconvert[4])
a4=float(entradaconvert[5])
a5=float(entradaconvert[6])
Nmax=int(entradaconvert[7])
e1=float(entradaconvert[8])
e2=float(entradaconvert[9])
a=float(entradaconvert[10])
b=float(entradaconvert[11])

def f(A):
  return a0*math.cos(a1*A)+a2*math.sin(a3*A)+math.exp(a4*A)+a5

def bissecao(a,b,e1,e2,Nmax):
    p=0
    #tenho que zerar o X para que o while identificque um valor em f(X)

    X=0
    while (abs(a-b)>e1 and abs(f(X))>e2):
        p=p+1
        X=(a+b)/2
        if f(a)*f(X)<0:
            b=X
            #print 'entrouasdasdas'
        elif f(a)*f(X)>0:
            a=X
            #print 'enars aqui carai'
        #printando
        print 'Metodo: Bissecao'
        print 'Iteracao: ',p
        print 'NAO CONVERGIU'
        print 'Raiz final:',X
        print '|a-b|:',abs(a-b)
        print '|f(x_i)|:',f(X)
        print'\n'
    #aqui ele saiu do while pq convergiu
    X=(a+b)/2
    if f(a)*f(X)<0:
        b=X
            #print 'entrouasdasdas'
    elif f(a)*f(X)>0:
        a=X
    print 'Metodo: Bissecao'
    print 'Iteracao: ',p+1
    print 'CONVERGIU'
    print 'Raiz final:',X
    print '|a-b|:',abs(a-b)
    print '|f(x_i)|:',f(X)
    print'\n'


def secantes(x0,x1,e1,e2,Nmax):
    X=[x0,x1]
    a=1
    while abs(X[a]-X[a-1])>e1 and abs(f(X[a]))>e2:
        print 'Metodo: Secantes'
        print 'Iteracao: ',a
        print 'NAO CONVERGIU'
        X.append((X[a-1]*f(X[a])-X[a]*f(X[a-1]))/(f(X[a])-f(X[a-1])))
        print 'Raiz final:',abs(X[a+1])
        print '|a-b|:',abs(X[a+1]-X[a])
        print '|f(x_i)|:',abs(f(X[a+1]))
        print '\n'
        a+=1
       
    
    print 'Metodo: Secantes'
    print 'Iteracao: ',a
    print 'CONVERGIU'
    X.append((X[a-1]*f(X[a])-X[a]*f(X[a-1]))/(f(X[a])-f(X[a-1])))    
    print 'Raiz final:',(X[a+1])
    print '|x_i-x_(i-1)|:',abs(X[a+1]-X[a])
    print '|f(x_i)|:',abs(f(X[a+1]))
if M==1:
    bissecao(a,b,e1,e2,Nmax)
elif M==2:
    secantes(a,b,e1,e2,Nmax)


