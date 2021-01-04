# def solution(phone_book):
#     phone_book.sort(key= lambda x:len(x))
#     for i in range(len(phone_book)) :
#         temp = phone_book[:i]+phone_book[i+1:]
#         for j in temp:
#             if phone_book[i]==j[:len(phone_book[i])] :
#                 return False
#     return True


def solution(phoneBook):
    phoneBook = sorted(phoneBook)


    print(list(zip(phoneBook, phoneBook[1:])))
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

print(solution(["97674223","1195524421","118","119"]))


