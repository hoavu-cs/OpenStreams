import sketches
import random
from random import randrange
from collections import Counter
import mmh3
import math
import string
import os, psutil

#test_input = [''.join(random.choice(string.ascii_uppercase + string.digits) for k in range(20)) for i in range(500000)]
#print(f"true number of distinct elements: {len(set(test_input))}")

process = psutil.Process(os.getpid())
F0 = sketches.F0_estimate(epsilon = 0.1, delta = 0.1, C=2)


for i in range(500000):
#    token=''.join(random.choice(string.ascii_uppercase + string.digits) for k in range(10))
    token = randrange(3000,4500)
    F0.insert(str(token))

print(f"Number of distinct elements estimate returned by the sketch {str(F0.estimator())}")

print(process.memory_info().rss)  # in bytes
