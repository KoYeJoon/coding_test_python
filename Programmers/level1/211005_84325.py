def solution(table, languages, preference):
    category_dict={}

    for t in table :
        list_t = t.split()
        category = list_t[0]
        category_dict[category] = 0
        for i in range(1,6):
            if list_t[i] in languages:
                category_dict[category] += (6-i)*preference[languages.index(list_t[i])]

    cate_item = list(category_dict.items())
    cate_item.sort(key=lambda x : (-x[1],x[0]))

    return cate_item[0][0]

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["PYTHON", "C++", "SQL"],[7, 5, 5]))