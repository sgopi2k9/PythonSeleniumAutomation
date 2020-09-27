def arrange():
    a = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34,-1,0]
    b=[]
    min = a[0]
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                t = a[i]
                a[i] = a[j]
                a[j] = t

    print(str(a))

arrange()


