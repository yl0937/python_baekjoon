# https://www.acmicpc.net/problem/1259

while(1):
    t = input()
    if(t[0]=="0"):
        break
    else:
        if(len(t)%2!=0):
          t = t[0:int(len(t)/2)] + t[int(len(t)/2)+1:]
        checkT = t[0:int(len(t)/2)] + "".join(reversed(t[0:int(len(t)/2)]))
        if(t!=checkT):
            print("no")
        else:
            print("yes")