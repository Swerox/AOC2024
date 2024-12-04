"""RESULT IS NOT MINE IM TOO BAD FOR IT"""

import numpy as np

npa = lambda *s: np.array(list(map(list, s)))
swv = np.lib.stride_tricks.sliding_window_view
input = npa(*open('Day4/input.txt').read().splitlines())
n_matches = lambda k: np.sum(np.all(np.logical_or(swv(input, k.shape) == k, k == '.'), axis=(2, 3)))
num = lambda k: sum( n_matches(np.rot90(k, i)) for i in range(4) )
s2k = lambda *s: num(npa(*s))
result2 = s2k('M.S', '.A.', 'M.S')

print(result2)