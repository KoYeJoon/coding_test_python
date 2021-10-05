def merge(b,c,a):
    i,j,k=0,0,0
    p=len(b)
    q=len(c)
    while i<p and j<q :
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1

    if i==p:
        a[k:] = c[j:]
    else :
        a[k:] = b[i:]


def mergesort(a):
    if len(a)>1 :
        mid = len(a)//2
        b = a[:mid]
        c = a[mid:]
        mergesort(b)
        mergesort(c)
        merge(b,c,a)
    return a

print(mergesort([3,29,30,24,39]))