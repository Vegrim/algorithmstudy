  def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    d = 0
    e = 0
    f = 0
    for i in range(0,len(answers)-5):
        a.append(a[i])
    for i in range(0,len(answers)-8):
        b.append(b[i])
    for i in range(0,len(answers)-10):
        c.append(c[i])
    for i in range(0,len(answers)):
        if a[i] == answers[i]:
            d += 1
    for i in range(0, len(answers)):
        if b[i] == answers[i]:
            e += 1
    for i in range(0,len(answers)):
        if c[i] == answers[i]:
            f += 1
    if d == e == f :
        answer = [1,2,3]
    elif d>e and d>f :
        answer.append(1)
    elif e>d and e>f :
        answer.append(2)
    elif f>d and f>e :
        answer.append(3)
    elif d == e and d > f:
        answer = [1,2]
    elif d==f and d>e:
        answer = [1,3]
    elif e == f and e>d:
        answer = [2,3]
    return answer
