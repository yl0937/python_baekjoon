# https://www.acmicpc.net/problem/5430
import sys
from collections import deque

T = int(sys.stdin.readline())
for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = deque( sys.stdin.readline().rstrip()[1:-1].split(","))
    p = p.replace("RR","")
    queue = deque(arr)

    if n ==0:
        arr = deque()
    R = 0
    status = 1
    for item in p:
        if item=='R':
            R += 1
        elif item=='D':
            if arr:
                if R % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print("error")
                status = 0
                break

    if status == 0:
        continue
    else:
        if R % 2 ==0:
            print("[" + ",".join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")