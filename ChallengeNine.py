for i in range(int(input())):
    n=input()
    print("Case #",end="")
    print(i+1,end="")
    print(": ",end="")
    sum=0
    for i in n:
        sum+=int(i)
    if sum%9==0:
        print(n)
    else:
        a=min(int(n+str(min(sum%9,9-sum%9))),int(str(min(sum%9,9-sum%9))+n))
        b=str(a)
        if b[0]=='0':
            print(b[1:])
        else:
            print(b)