import sketches
from random import randrange
from collections import Counter
import mmh3
import math
#test_input = [1,2,1,1,3,4,2,2,2,3,3,4,4,4,4,4,4]

test_input = [randrange(100, 400) for i in range(10000)]
print(len(set(test_input)))

summary = sketches.Misra_Gries(2)
distinct = sketches.F0_estimate(epsilon = 0.1, C=5)

for i in test_input:
    distinct.insert(i)
#    summary.insert(i)
#    distinct.insert(i)#
#    print("number of distinct elements estimate" + str(distinct.estimator()))
#    print("insert " + str(i))
#    print(str(summary.buckets))

print("number of distinct elements estimate " + str(distinct.estimator()))
