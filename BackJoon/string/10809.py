#10809.py
"""
str = input()
word_list=[]
word_num=[]
for i in str :
	word_list.append(ord(i))

for i in range(0,27):
	word_num.append(-1)

for c in range(len(word_list)):
	for j in range(0,27):
		if(word_list[c]-97 == j):
			if(word_num[j]==-1):
				word_num[j]=c

for i in range(0,27):
	print(word_num[i],end=" ")
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
word_list = []
word_num = []

word = str(input())


for i in word:
    word_list.append(i)

for character in alphabet:
    for i in range(len(word_list)):
        if character == word_list[i]:
            word_num.append(i)
            break
        elif i < len(word_list)-1: continue
        else:
            word_num.append(-1)
for i in word_num:
    print(i,end=" ")
