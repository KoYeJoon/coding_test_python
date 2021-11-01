size = 10
arr = [i * 2 for i in range(size)]

print(arr)
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

new_arr = [n * n for n in arr]

print(new_arr)
#[0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

word = '가나다'

print([c * 2 for c in word])
# ['가가', '나나', '다다']

# 조건문으로 필터링
size = 10
arr = [n for n in range(1, 11) if n % 2 == 0]

print(arr) #[2, 4, 6, 8, 10]

arr = [n for n in range(1, 31) if n % 2 == 0 if n % 3 == 0]

print(arr)# [6, 12, 18, 24, 30]

# set
set_magic = {n ** 2 for n in range(10)}
print(set_magic) #{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# tuple
tuple_magic = tuple(n for n in range(1, 10))
print(tuple_magic) #(1, 2, 3, 4, 5, 6, 7, 8, 9)

# dict
from string import ascii_lowercase as LOWERS

dict_magic = {c: n for c, n in zip(LOWERS, range(1, 27))}
print(dict_magic) #{'a': 1, 'b': 2, 'c': 3, ..., 'x': 24, 'y': 25, 'z': 26}
