# https://brunch.co.kr/@princox/180

def lastName_and_FirstName(*Names):
    for name in Names:
        print("%s %s"%(name[0], name[1:3]), end=' ')
    print()
    print(type(Names),Names)

# lastName_and_FirstName("이천수")
# lastName_and_FirstName("이천수","안정환")
# lastName_and_FirstName("이천수","안정환","황선홍")
lastName_and_FirstName("이천수","안정환","황선홍","박지성")


def introduceEnglishName(**kwargs):
    for key,value in kwargs.items():
        print("{0} is {1}".format(key,value))

introduceEnglishName(MyName="Chris!!")

# 특정 키워드 인식
def introduceEnglishName2(**kwargs):
    for key,value in kwargs.items():
        if 'ant' in kwargs.keys():
            print("안녕하세요 ~~ 반갑습니다 ~~")
        print("{0} is {1}".format(key,value))

introduceEnglishName2(MyName="Chris!!")
introduceEnglishName2(ant="Chris!!")

#help(print)

print("안녕하세요, 파이썬 재미있나요? -1")
print("네, 너무 재미있습니다 -1")

print("안녕하세요, 파이썬 재미있나요? -2", end = ' ')
print("네, 너무 재미있습니다 -2")

print("안녕하세요, 파이썬 재미있나요? -3", end='(사실 너무 재미없어요,,)')
print("네, 너무 재미있습니다 -3")

def blog_pointer(name, *blogs):
    print(name)
    for post in blogs :
        print(post)

name = "내 이름 "
blog1 = "first blog"
blog2 = "second blog"
blog3 = "third blog"

blog_pointer(name,blog1,blog2,blog3)

# def blog_pointer(*name, blogs):
#     print(name)
#     for post in blogs :
#         print(post)
#
# name = "내 이름 "
# blog1 = "first blog"
# blog2 = "second blog"
# blog3 = "third blog"
#
# blog_pointer(name,blog1,blog2,blog3)

def blog_pointer(name, *blogs,**blog_benefits):
    '''
    name : 블로그 주인 이름
    *blogs : 블로그 만들 때 설명
    **blog_benefits : 해당 블로그 수익
    '''
    print(name)
    for post in blogs :
        print(post)
    for blog,benefits in blog_benefits.items():
        print(blog, "수익은 >> ", benefits)


name = "내 이름 "
blog1 = "first blog"
blog2 = "second blog"
blog3 = "third blog"
help(blog_pointer)
blog_pointer(name,blog1,blog2,blog3,blogcost1=30,blogcost2=50, blogcost3=100)