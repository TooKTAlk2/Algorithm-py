import sys

input = sys.stdin.readline
s = input().strip()

freqList = [0 for _ in range(26)]

for _ in s:
    freqList[ord(_) - ord('a')] = freqList[ord(_) - ord('a')] + 1

for _ in freqList:
    sys.stdout.write("%d "%_)