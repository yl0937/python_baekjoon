# https://www.acmicpc.net/problem/1764

n,m = map(int,input().split())

noHear = set()
noSee = set()

for n in range(0,n):
    name = input()
    noHear.add(name)
for m in range(0,m):
    name = input()
    noSee.add(name)

noHearSee = sorted(list(noHear&noSee))
print(len(noHearSee))
for name in noHearSee:
    print(name)