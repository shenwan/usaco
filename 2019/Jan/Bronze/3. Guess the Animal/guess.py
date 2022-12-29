'''
AC
'''

read = open("guess.in", "r").readline
write = open("guess.out", "w").write


class Bits:
    def __init__(self) -> None:
        self.data = []

    def size(self) -> int:
        return len(self.data)

    def get(self, index) -> bool:
        return 1 == self.data[index]

    def set(self, index) -> None:
        if (index >= len(self.data)):
            for n in range(len(self.data), index + 1):
                self.data.append(0)
        self.data[index] = 1


def count_both_set_bits(bits1, bits2) -> int:
    count = 0
    for i in range(min(bits1.size(), bits2.size())):
        if bits1.get(i) and bits2.get(i):
            count += 1
    return count


N = int(read())
ch2index = {}
num_ch = 0
animals = []

for i in range(N):
    line = read()
    strs = line.split()
    animal = strs[0]
    K = int(strs[1])

    ch_bits = Bits()
    for ch in strs[2:]:
        if ch in ch2index:
            index = ch2index[ch]
        else:
            index = num_ch
            ch2index[ch] = index
            num_ch += 1
        ch_bits.set(index)
    animals.append(ch_bits)

result = 0
for i in range(len(animals)):
    for j in range(i+1, len(animals)):
        n = count_both_set_bits(animals[i], animals[j])
        result = max(result, n)

write(str(result + 1))
