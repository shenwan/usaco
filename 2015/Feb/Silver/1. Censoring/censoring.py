'''
http://www.usaco.org/index.php?page=viewproblem2&cpid=529

timeout cases: 3,4,6,8,9,10,13
'''

# S = input()
# T = input()


def read_line_from_file(f):
    s = input_file.readline()
    return s.rstrip("\n")


with open("censor.in", "r") as input_file:
    S = read_line_from_file(input_file)
    T = read_line_from_file(input_file)

M = len(S)
N = len(T)

while True:
    S = S.replace(T, "", 1)
    new_len = len(S)
    if new_len == M:
        break
    M = new_len

# print(S)
with open("censor.out", "w") as output_file:
    output_file.write(S)
