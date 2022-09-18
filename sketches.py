import mmh3
import math
import random
import statistics


class Misra_Gries:

    # initialize: parameter k controls heavy hitter threshold, i.e., total_count/k
    def __init__(self, k = 1):
        self.k = k
        self.counters = {}

    # insert an element to the data structure
    def insert(self, token):
        # if the element is already in a bucket
        if token in self.counters:
            self.counters[token] += 1
        else:
            # if there are still empty bucket(s)
            if len(self.counters) < self.k:
                self.counters[token] = 1
            else:
                for y in list(self.counters):
                    self.counters[y] -= 1
                    if self.counters[y] == 0:
                        del self.counters[y]

    # return the buckets of top estimate counts
    # count - stream length/num_buckets <= estimate count <= count
    def top_counters(self, amount):

        sorted_freq = sorted(self.counters, key=self.counters.get, reverse=True)
        sorted_counters = {}

        for y in sorted_freq[:amount]:
            sorted_counters[y] = self.counters[y]

        return sorted_counters



class F0_estimate():

    # initialize
    # epsilon: relative error, delta: failure probability
    def __init__(self, epsilon=0.01, delta=0.01, C=5):

        # for each hash function h, maintain the smallest hash value H
        # basic esimate E = (1/H)-1
        # return the median of r averages of c basic estimators
        self.seed = []
        self.c = C*math.ceil(1/(epsilon*epsilon))
        self.r = math.ceil(math.log(2,1/delta))
        self.seed_range = C*C*self.r*self.c


        # initialize the seeds for hash functions
        self.seed = [[random.randrange(1,self.seed_range) for j in range(self.c)] for i in range(self.r)]
        self.smallest_hash =[[1 for j in range(self.c)] for i in range(self.r)]


    def hash(self, token, seed):
        max_32_int = pow(2,32)-1
        return mmh3.hash(token.to_bytes(5, 'big'), seed, signed = False)/max_32_int

    def insert(self, token):
        for i in range(self.r):
            for j in range(self.c):
                hash_value = self.hash(token, self.seed[i][j])
                if hash_value < self.smallest_hash[i][j]:
                    self.smallest_hash[i][j] = hash_value


    def estimator(self):
        avg = [statistics.mean(self.smallest_hash[i]) for i in range(self.r)]
        median_of_means = statistics.median(avg)
        return math.ceil((1/median_of_means) - 1)
