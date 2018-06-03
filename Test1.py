def solution (A):
        word=[]
        for val in A:
            if (val[1:2]=='>'):
                word.insert(0,val[0:1])


solution(["P>E", "E>R", "R>U"])