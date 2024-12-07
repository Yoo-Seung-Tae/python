def solution(babbling):
    answer = 0
    a=["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        for k in range(len(babbling[i])-len(a)+1):
            for l in range(len(a)):
                babbling[i].lstrip(a[l])
        if babbling[i]=='':
            answer+=1
    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))