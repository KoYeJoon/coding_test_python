import hashlib
import random as rnd
hash_table = list([0 for i in range(100)])
seed_n = 3
rnd.seed(seed_n)
rand_table = list([0 for i in range(100000)])

def hash_func(key):
    if rand_table[key] == 0 :
        rand_table[key] = rnd.random()
    key = int(key*rand_table[key])
    return key % len(hash_table)

def get_key(data):
    ind = sum([ord(d) for d in data])
    return ind

def storage_data(data,value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    # hash table 충돌 방지 로 수정
    # hash_table[hash_address] = value
    # hash 충돌한 경우
    if hash_table[hash_address] != 0:
        # 현재 address에서 뒤에 chaining으로 뒤에 값이 있는지 확인
        for idx in range(hash_address,len(hash_table)):
            # 다음 값에 값이 없는 경우, 넣어주기
            if hash_table[idx]==0 :
                hash_table[idx] = [data,value]
                return
            # 해당 Key와 같은 key가 있는 경우, value 업데이트
            elif hash_table[idx][0] == index_key :
                hash_table[idx][1]= value
                return
    else:
        # hash가 충돌되지 않은 경우, key와 value 저장
        hash_table[hash_address]=[data,value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    print(hash_address)
    print(hash_table[hash_address])
    # hash 충돌 방지 시 읽는 법
    # hash table에 해당 key에 해당하는 hash address가 있는 경우
    if hash_table[hash_address] != 0:
        for idx in range(hash_address,len(hash_table)):
            # 해당 hash address에 값이 없으면 없는 것
            if hash_table[idx] == 0:
                return None
            # 해당 hash_table index에 있는 key와 일치하는 경우, value return
            elif hash_table[idx][0] == index_key :
                return hash_table[idx][1]
    else :
        # hash table에 해당 key에 해당한는 hash address가 없는 경우
        return None

storage_data('hello','01012345678')
storage_data('hi','01023456789')


print(read_data('hello'))
print(read_data('hi'))

print(hash_table)

