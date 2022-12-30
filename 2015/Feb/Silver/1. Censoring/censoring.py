'''
http://www.usaco.org/index.php?page=viewproblem2&cpid=529
TLE except cases 1,2,4,8
'''

import io
import os
import sys


# read = sys.stdin.readline
# write = sys.stdout.write
read = open("censor.in", "r").readline
write = open("censor.out", "w").write

S = read().strip()
T = read().strip()

M = len(S)
N = len(T)


class Interval:
    def __init__(self, begin, end) -> None:
        self.begin = begin
        self.end = end


class Partial:
    def __init__(self, pattern) -> None:
        self.pattern = pattern
        self.patternLen = len(pattern)
        self.intervals = [Interval(0, 0)]

    def add(self, i) -> None:
        self.intervals[-1].end = i + 1
        if self.matchPattern():
            self.removePattern()

    def matchPattern(self) -> bool:
        numToMatch = N
        for interval in reversed(self.intervals):
            n = min(numToMatch, interval.end - interval.begin)
            if T[numToMatch - n:numToMatch] != S[interval.end - n:interval.end]:
                return False
            numToMatch -= n
            if numToMatch == 0:
                return True
        return False

    def removePattern(self) -> None:
        nextBegin = self.intervals[-1].end
        numToRemove = N
        while numToRemove > 0:
            interval = self.intervals[-1]
            if numToRemove < interval.end - interval.begin:
                interval.end -= numToRemove
                self.intervals.append(Interval(nextBegin, nextBegin))
                return
            numToRemove -= interval.end - interval.begin
            self.intervals.pop()
        self.intervals.append(Interval(nextBegin, nextBegin))

    def print(self) -> None:
        for interval in self.intervals:
            write(S[interval.begin:interval.end])


p = Partial(T)
for i in range(M):
    p.add(i)
p.print()
