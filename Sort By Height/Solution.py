def solution(a):
    trees = [i for i,el in enumerate(a) if el==-1]

    k=0
    for i in range(len(a)):
        i+=k
        if a[i]==-1:
            a.remove(a[i])
            k-=1
    a.sort()
    
    i=0
    for el in trees:
        el+i
        a.insert(el,-1)
        i+=1
    
    return print(a)
        

a = [-1, 150, 190, 170, -1, -1, 160, 180]
a = [4, 2, 9, 11, 2, 16]
solution(a)