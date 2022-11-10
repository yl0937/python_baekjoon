# 1. 집합
set1 = set()

# 1-1 중복 X
set1.add(1)
set1.add(1)
set1.add(1)
print("set1 = " , set1)

# 1-2 데이터 입력
set1.add(2)
set1.add(3)
print("set1 = " , set1)

# 1-3 데이터 삭제
set1.remove(1)
print("set1 = " , set1)

# 1-4 집합 크기, 데이터 여부
print(len(set1))
print(2 in set1)

# 2. 집합 연산
setA = set([1,2,3,4,5])
setB = set([2,4,6,8,10])

# 2-1 합집합
print(setA | setB)

# 2-2 교집합
print(setA & setB)

# 2-3 차집합
print(setA-setB)