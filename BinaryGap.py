# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    listbin = [int(d) for d in str(bin(N))[2:]]
    count = 0
    gap = 0
    for i in range(len(listbin)-1):
        if listbin[i] == 1:
            if listbin[i+1] == 0:
                count = 0
                for j in range(i+1, len(listbin)):
                    if listbin[j] == 0:
                        count += 1
                    if listbin[j] == 1:
                        if count > gap:
                            gap = count
                        break
    
    return gap
