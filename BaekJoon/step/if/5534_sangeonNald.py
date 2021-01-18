#5534_sangeonNald.py
M=2000
B=2000

for i in range(3) :
	N=int(input())
	M=min(N,M)

for j in range(2):
	N=int(input())
	B=min(N,B)

print(M+B-50)
