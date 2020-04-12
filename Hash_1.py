def solution(phone_book):
    answer = True
    dict = {}
    for i in range(0,len(phone_book)):
        dict[phone_book[i]] = True
        
    for i in range(0,len(phone_book)):
        for j in range(1,len(phone_book[i])):
            b = phone_book[i][0:j]
            if b in dict:
                answer = False
    
    return answer
