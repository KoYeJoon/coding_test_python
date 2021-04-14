n,m,k = map(int, input().split())
data = list(map(int,input().split()))
data.sort(reverse=True)

result = 0
result += data[0] * ((k*(m//(k+1)))+m%(k+1))
result += data[1] * (m //(k+1))
print(result)