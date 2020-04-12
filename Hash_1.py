def solution(phone_book):
    answer = True
    dict = {}
    a = []
    for i in range(0,len(phone_book)):
        a.append(i)
        a[i] = str(phone_book[i])
        dict[a[i]] = True
    
    for i in range(0,len(a)):
        for j in range(1,len(a[i])):
            b = a[i][0:j]
            if b in dict:
                answer = False
                return answer
            else :
                answer = True
                
    return answer
