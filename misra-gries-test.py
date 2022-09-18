import sketches
from random import randrange
from collections import Counter
import mmh3
import math


test_input = [1,2,1,1,3,4,2,2,2,3,3,4,4,4,4,4,4]

mg = sketches.Misra_Gries(2)
distinct = sketches.F0_estimate(epsilon = 0.1, C=5)

for i in test_input:
    mg.insert(i)
    print(f"insert {i}")
    print(str(mg.counters))
