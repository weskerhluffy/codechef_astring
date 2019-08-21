'''
Created on 20 ago 2019

@author: ernestoalvarado
'''
# XXX: https://www.codechef.com/LTIME36/problems/ASTRING
# XXX: https://stackoverflow.com/questions/35714003/smallest-lexicographic-subsequence-of-size-k-in-an-array

import sys
import os
from _functools import reduce


# XXX: https://gist.github.com/m00nlight/1f226777a49cfc40ed8f
class RMQ:

    def __init__(self, n):
        self.sz = 1
        self.inf = sys.maxsize
        while self.sz <= n:
            self.sz <<= 1
        self.dat = [self.inf] * (2 * self.sz - 1)

    def update(self, idx, x):
            idx += self.sz - 1
            self.dat[idx] = x
            while idx > 0:
                idx = (idx - 1) >> 1
                self.dat[idx] = min(self.dat[idx * 2 + 1], self.dat[idx * 2 + 2])

    def query(self, a, b):
        return self.query_help(a, b, 0, 0, self.sz - 1)

    def query_help(self, a, b, k, l, r):
        if r < a or b < l:
            return self.inf
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            return min(self.query_help(a, b, 2 * k + 1, l, (l + r) >> 1), self.query_help(a, b, 2 * k + 2, ((l + r) >> 1) + 1, r))


def core(s, k):
    s = list(map(ord, s))
    s_len = len(s)
    rmq = reduce(lambda a, item:(a.update(item[0], item[1]) or a), enumerate(s), RMQ(s_len))

    i = 0
    j = s_len - k
    r = []
    while k:
        c = rmq.query(i, j)
        while i < s_len and s[i] != c:
            i += 1
        i = min(i + 1, s_len - 1)
        j = min(j + 1, s_len - 1)
        k -= 1
        r.append(c)
    return "".join(map(chr, r))


if __name__ == '__main__':
    if "STDIN" in os.environ:
        f = open(os.environ["STDIN"], "r")
        input_fn = f.readline
    else:
        input_fn = input
    t = int(input_fn())
    while t:
        s = input_fn().strip()
        k = int(input_fn())
        r = core(s, k)
        print(r)
        t -= 1
