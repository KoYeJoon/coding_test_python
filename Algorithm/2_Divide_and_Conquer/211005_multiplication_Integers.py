def prod(A,B):
    n = max(len(str(A)),len(str(B)))
    if A==0 or B==0 :
        return 0
    if n<threshold :
        return A*B
    else :
        m = n//2
        a1 = A // (10**m)
        a0 = A % (10**m)
        b1 = B // (10**m)
        b0 = B % (10**m)
        c2 = prod(a1,b1)
        c1 = prod(a1+a0,b1+b0)
        c0 = prod(a0,b0)
        return c2*(10**(2*m)) + (c1-(c2+c0))*(10**m)+c0

threshold = 4 # hardware 에서 최대로 연산할 수 있는 마지노선 ( 임의로 설정)
print(prod(2135,4014))