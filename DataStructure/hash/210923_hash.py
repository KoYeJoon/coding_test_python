import hashlib

hash_table = list([0 for i in range(100)])

def hash_func(key):
    return key % len(hash_table)

def get_key(data):
    encoded_string = data.encode()
    hexdigest = hashlib.sha256(encoded_string).hexdigest()
    return int(hexdigest,16)

def storage_data(data,value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    # hash table 충돌 방지 로 수정
    # hash_table[hash_address] = value
    if hash_table[hash_address] != 0:
        for idx in range(hash_address,len(hash_table)):
            if hash_table[idx]==0 :
                hash_table[idx] = [idx,value]
                return
            elif hash_table[idx][0] == index_key :
                hash_table[idx][1]= value
                return
    else:
        hash_table[hash_address]=[index_key,value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    # print(hash_address)
    # print(hash_table[hash_address])
    # hash 충돌 방지 시 읽는 법
    if hash_table[hash_address] != 0:
        for idx in range(hash_address,len(hash_table)):
            if hash_table[idx] == 0:
                return None
            elif hash_table[idx][0] == index_key :
                return hash_table[idx][1]
    else :
        return None

storage_data('hello','01012345678')
storage_data('hi','01023456789')


print(read_data('hello'))
print(read_data('hi'))

print(hash_table)

