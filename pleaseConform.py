
cap1 = ['F','F','B','B','B','F','B','B','B','F','F','B','F'] # 13개 
#cap2 = ['F','F','B','B','B','F','B','B','B','F','F','F','F']

def pleaseConform(caps):
    start = forward = backward = 0
    intervals = []
    for i in range(1, len(caps)): # 1~13
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start])) # 간격 튜플이 리스트안으로 들어감
            if caps[start] == 'F':
                forward+=1
            else :
                backward+=1
            start = i      
    intervals.append((start, len(caps)-1, caps[start]))
    print(intervals)
    if caps[start] == 'F':
        forward+=1
    else :
        backward+=1
    if forward < backward:
        flip ='F'
    else :
        flip ='B'
    for t in intervals:
         if t[2] == flip : # intervals 리스트 안에 있는 3번째 요소 t[2] 가 B이면 출력하라 
             #print('People in position', t[0], 'through',t[1],'flip your caps!')
             if t[0] == t[1] :
                 print('People in position',t[1],'flip your cap!')
             else :
                 print('People in position', t[0], 'through',t[1],'flip your caps!')
                 
pleaseConform(cap1)
