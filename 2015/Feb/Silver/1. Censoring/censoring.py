'''
http://www.usaco.org/index.php?page=viewproblem2&cpid=529
'''

S = input()
M = len(S)

T = input()
N = len(T)

while True:
    S = S.replace(T, "", 1)
    new_len = len(S)
    if new_len == M:
        break
    M = new_len

print(S)
