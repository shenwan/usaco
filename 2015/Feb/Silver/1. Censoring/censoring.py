'''
http://www.usaco.org/index.php?page=viewproblem2&cpid=529
TLE: all cases except 1, 11
'''

import sys
import contextlib


@contextlib.contextmanager
def smart_input(filename=None):
    if filename and filename != '-':
        f = open(filename, 'r')
    else:
        f = sys.stdin

    try:
        yield f
    finally:
        if f is not sys.stdin:
            f.close()


@contextlib.contextmanager
def smart_output(filename=None):
    if filename and filename != '-':
        f = open(filename, 'w')
    else:
        f = sys.stdout

    try:
        yield f
    finally:
        if f is not sys.stdout:
            f.close()


def read_line_from_file(f):
    s = f.readline()
    return s.rstrip("\n")


S = ""
T = ""

# with smart_input() as input:
with smart_input("censor.in") as input:
    S = read_line_from_file(input)
    T = read_line_from_file(input)

M = len(S)
N = len(T)


class TreeNode:
    def __init__(self, value) -> None:
        self.children = []
        self.value = value

    def clone(self):
        root = TreeNode(self.value)
        for child in self.children:
            root.children.append(child.clone())
        return root


class PartialMatches:
    """Stores all different ways the already read characters can form prefixes of the pattern."""

    def __init__(self, pattern) -> None:
        self.pattern = pattern
        self.root = TreeNode(0)

    def clear(self) -> None:
        self.root = TreeNode(0)

    def print(self, output) -> None:
        assert self.root.value == 0
        prefixes = []
        node = self.root
        while len(node.children) > 0:
            node = node.children[0]
            prefixes.append(node.value)
        for prefix in reversed(prefixes):
            output.write(self.pattern[0:prefix])

    def add(self, ch) -> bool:
        assert self.root.value == 0

        nodeToAppend = None
        if ch == self.pattern[0]:
            nodeToAppend = self.root.clone()
            nodeToAppend.value = 1

        newRoot = TreeNode(0)
        for child in self.root.children:
            if ch == self.pattern[child.value]:
                child.value += 1
                if child.value == len(self.pattern):
                    child.value = 0
                    self.root = child
                    return True
                newRoot.children.append(child)

        if not nodeToAppend is None:
            newRoot.children.append(nodeToAppend)

        if len(newRoot.children) > 0:
            self.root = newRoot
            return True
        return False


def solve(output):
    p = PartialMatches(T)
    for ch in S:
        if not p.add(ch):
            p.print(output)
            p.clear()
            output.write(ch)
    p.print(output)
    output.write("\n")


# with smart_output() as output:
with smart_output("censor.out") as output:
    solve(output)
