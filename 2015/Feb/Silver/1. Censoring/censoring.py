'''
http://www.usaco.org/index.php?page=viewproblem2&cpid=529
TLE except cases 1,2
'''

import math
import io
import os
import sys

io_std = False
if io_std:
    read = sys.stdin.readline
    write = sys.stdout.write
else:
    read = open("censor.in", "r").readline
    write = open("censor.out", "w").write

S = read().strip()
T = read().strip()

M = len(S)
N = len(T)

MOD = int(1E9 + 7)


# Function to find modulo inverse of b. It returns
# -1 when inverse doesn't
# modInverse works for prime m
def modInverse(b, m) -> int:
    g = math.gcd(b, m)
    assert g == 1, f"inverse of {b} modulo {m} does not exist!"
    # If b and m are relatively prime, then modulo inverse is b^(m-2) mod m
    return int(pow(b, m - 2, m))


class Interval:
    def __init__(self, begin, end) -> None:
        self.begin = begin
        self.end = end


def char2int(ch) -> int:
    return ord(ch) - ord("a")


def addChar(mod, ch) -> int:
    return (mod * 26 + char2int(ch)) % MOD


class Partial:
    def __init__(self, pattern) -> None:
        self.pattern = pattern
        self.patternMod = 0
        for ch in pattern:
            self.patternMod = addChar(self.patternMod, ch)
        self.shiftMod = 1
        for i in range(N - 1):
            self.shiftMod = (self.shiftMod * 26) % MOD
        self.tailLen = 0
        self.tailMod = 0
        self.intervals = [Interval(0, 0)]

    def charOut(self) -> str:
        n = N
        for interval in reversed(self.intervals):
            l = interval.end - interval.begin
            if n < l:
                return S[interval.begin + l - n - 1]
            n -= l

    def add(self, i) -> None:
        self.intervals[-1].end = i + 1
        self.tailLen += 1
        if self.tailLen > N:
            ch = self.charOut()
            self.tailMod -= char2int(ch) * self.shiftMod
        self.tailMod = addChar(self.tailMod, S[i])
        if self.matchPattern():
            self.removePattern()
            self.tailMod = self.computeTailMod()

    def computeTailMod(self) -> int:
        r = 0
        k = 0
        for interval in reversed(self.intervals):
            for i in reversed(range(interval.begin, interval.end)):
                r = (r + char2int(S[i]) * int(pow(26, k))) % MOD
                k += 1
                if k == N:
                    return r
        return r

    def quickMatch(self) -> bool:
        return self.patternMod == self.tailMod

    def matchPattern(self) -> bool:
        if not self.quickMatch():
            return False
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
        self.tailLen -= N
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
