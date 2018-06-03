def solution (A):
    list=A.split(',')
    count=1
    counts=[]
    flag=0

    for ind in range (0,(len(list)-1)):
        #print (str(list[ind])[2:3])
        if((str(list[ind])[2:3])==(str(list[ind+1])[0:1])):
            count +=1
            flag=1
        else:
            counts.append(count)
            count=1
            flag = 0

    if (flag==1):
        counts.append(count)

    if( len(list)==1):
        return 1

    if (len(counts)==0):
        return 0
    return max(counts)

#print(solution("1-1,3-5,5-2,2-3,2-4"))
#print(solution("1-1"))
#print(solution("1-2,1-2"))
#print(solution("3-2,2-1,1-4,4-4,5-4,4-2,2-1"))
print(solution("5-5,5-5,4-4,5-5,5-5,5-5,5-5,5-5,5-5,5-5"))
#print(solution("1-1,3-5,5-5,5-4,4-2,1-3"))
#print(solution("1-2,2-2,3-3,3-4,4-5,1-1,1-2"))