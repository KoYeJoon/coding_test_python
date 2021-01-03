def solution(n):
    bin_n = bin(n)[2:]
    n_one_count = bin_n.count('1')
    big_n = n+1
    while True :
        bin_bigN = bin(big_n)[2:]
        bigN_one_count = bin_bigN.count('1')
        if n_one_count == bigN_one_count :
            break
        big_n += 1
    return big_n

print(solution(78))


n=11
bin_n = bin(n)
dec_n = int(bin_n,base=2)
print("n : %d,  2진수 n : %s,   10진수 n : %d" %(n,bin_n, dec_n))