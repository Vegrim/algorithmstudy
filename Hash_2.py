  def solution(clothes):
    answer = 0
    dict = {}
    
    for i in range(0,len(clothes)):
        type = clothes[i][1]
        cloth = clothes[i][0]
        
        if type not in dict:
            dict[type] = []
            
        dict[type].append(cloth)
    
    print(dict)
    a = 1
    for type in dict:
        print(type)
        cloth = dict[type]
        a=a*(len(cloth) + 1) 
    answer = a -1
    return answer
