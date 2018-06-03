def solution (A):
    letters=[]
    for value in A:
        letters.append(value[0:1])
    letters.append(A[-1][2:3])
    print (letters)

    order = [-1] * len(letters)


solution(["P>E","E>R","R>U"])
solution(["I>N","A>I","P>A","S>P"])