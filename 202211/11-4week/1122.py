# https://www.acmicpc.net/problem/1181

t = int(input())
words = []
for i in range(t):
    words.append(input())
words = list(set(words))
words.sort()
words.sort(key=lambda words: len(words))
for word in words:
    print(word)