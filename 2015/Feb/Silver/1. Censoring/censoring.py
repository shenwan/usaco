'''
http://www.usaco.org/index.php?page=viewproblem2&cpid=529
'''

# S = input()
# T = input()


from collections import deque


def read_line_from_file(f):
    s = input_file.readline()
    return s.rstrip("\n")


with open("censor.in", "r") as input_file:
    S = read_line_from_file(input_file)
    T = read_line_from_file(input_file)

M = len(S)
N = len(T)

# TODO: implementation
s = deque()

start_print = 0


def print_deque(f, end):
    f.write(S[start_print:end])


with open("censor.out", "w") as output_file:
    num_matches = 0
    for i in range(M):
        ch = S[i]
        if num_matches == 0:
            if ch == T[0]:
                num_matches = 1
        else:
            if ch == T[0]:
                s.append((num_matches, i))
                num_matches = 1
                continue
            if ch == T[num_matches]:
                num_matches += 1
                if num_matches == N:
                    maybe_start_print = i + 1
                    if len(s) == 0:
                        num_matches = 0
                        continue
                    num_matches, end = s.pop()
            else:
                print_deque(output_file, end)
                start_print = maybe_start_print
                s.clear()
    print_deque(output_file, M)
