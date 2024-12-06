def solution(str1, str2):
    answer = ''
    sol=[]
    for i in range(len(str1)):
        sol.append(str1[i])
        sol.append(str2[i])
        
    answer = "".join(sol)
    print(answer)
    return answer



print(solution("aaaaa", "bbbbb"))