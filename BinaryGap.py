# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    N = bin(N)[2:]
    count = 0
    maxgap = 0
    for k in N:
        if int(k) == 0:
            count += 1
        elif int(k) == 1:
            maxgap = max(count, maxgap)
            count = 0
    return maxgap
