for x in range(int(input())):
    print("Case #", end="")
    print(x+1, end="")
    print(": ", end="")
    I = input()
    P = input()
    
    m = len(I)   
    n = len(P)
    i = 0
    j = 0
    cnt = 0
    while(j < n and i < m):
        if(I[i] == P[j]):
            i+=1
        else:
            cnt+=1
        j+=1
    if(i == m):
        print(cnt + n-j)
    else:
        print("IMPOSSIBLE")