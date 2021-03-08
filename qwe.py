def fun1(n):
    for i in range(len(n)-1,-1,-1):
        print(n[i],end='')
    print()
def fun2(n):#29
    if n==0 or n==1:
        return n
    else:
        return fun2(n-1)+fun2(n-2)
    print(fun2(int(input())))
def fun3(a):
    for i in range(len(a)):
        if i%2==0:
            print(a[i],end='~')
        elif i%2!=0:
            print(a[i],end='_')
def fun4(n): #遞迴
    if n<10:
        return 1
    else:
        return 1+fun4(n//10)
def fun5(n):#遞迴2
    if n==2:
        return n
    else:
        return n*fun5(n-1)

