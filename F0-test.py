import sketches
import random
from random import randrange
from collections import Counter
import mmh3
import math
import string

test_input = [''.join(random.choice(string.ascii_uppercase + string.digits) for k in range(20)) for i in range(500000)]
print(f"true number of distinct elements: {len(set(test_input))}")

F0 = sketches.F0_estimate(epsilon = 0.1, C=2)

for i in test_input:
    F0.insert(i)

print(f"Number of distinct elements estimate returned by the sketch {str(F0.estimator())}")
