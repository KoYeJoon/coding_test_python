# def test_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen = test_generator()
# # type(gen)
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
#
# import collections
# print(isinstance(gen,collections.Iterable))
# for i in test_generator():
#     print(i)
#
# # generator 2 개 생성 시
# h = test_generator()
# i = test_generator()
# print(h==i)
# print(h is i)
# print(next(h))
# print(next(i))
# print(next(h))
# print(next(i))
# print(next(h))
# print(next(i))

# yield 사이에 추가로 코드 입력하여 동작 확인
# def test_generator():
#     print('yield1 전')
#     yield 1
#     print('yield 1과 2 사이')
#     yield 2
#     print('yield 2와 3 사이 ')
#     yield 3
#     print('yield 3 후')
#
# g = test_generator()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def infinite_generator():
#     count = 0
#     while True :
#         count += 1
#         yield count
#
# gen = infinite_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

print(type(x*x for x in [2,4,6]))

# def three_generator():
#     a = [1,2,3]
#     for i in a:
#         yield i
#
# gen = three_generator()
# print(list(gen))

def three_generator():
    a = [1,2,3]
    yield from a

gen = three_generator()
print(list(gen))