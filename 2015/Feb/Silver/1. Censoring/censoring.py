'''
http://www.usaco.org/index.php?page=viewproblem2&cpid=529
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

# TODO: implementation

# print(S)
with open("censor.out", "w") as output_file:
    output_file.write(S)
