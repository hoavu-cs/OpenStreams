import sketches
from random import randrange
from collections import Counter
import mmh3
import math

test_input = [randrange(100, 400) for i in range(10000)]
print(f"true number of distinct elements: {len(set(test_input))}")

F0 = sketches.F0_estimate(epsilon = 0.1, C=5)

for i in test_input:
    F0.insert(i)

print(f"Number of distinct elements estimate returned by the sketch {str(F0.estimator())}")
