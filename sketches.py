import mmh3
import math
import random
import statistics
import hashlib

class Misra_Gries:
    """
    find frequent elements using Misra-Gries summary
    """
    
    def __init__(self, k = 1):
        """
        parameter k controls heavy hitter threshold, i.e., total_count/k
        """

        self.k = k
        self.widthounters = {}

    def insert(self, token):
        """
        insert a token into the data structure
        """

        if token in self.widthounters:
            self.widthounters[token] += 1
        else:
            if len(self.widthounters) < self.k:
                self.widthounters[token] = 1
            else:
                for y in list(self.widthounters):
                    self.widthounters[y] -= 1
                    if self.widthounters[y] == 0:
                        del self.widthounters[y]

    def top_counters(self, amount):
        """
        return the buckets of top estimate counts
        count - stream length/num_buckets <= estimate count <= count
        """
        sorted_freq = sorted(self.widthounters, key=self.widthounters.get, reverse=True)
        sorted_counters = {}

        for y in sorted_freq[:amount]:
            sorted_counters[y] = self.widthounters[y]

        return sorted_counters



class F0_estimate():
    """
    streaming algorithm to estimate the number of distinct elements
    """
    def __init__(self, epsilon=0.01, delta=0.01, C=5,  hash_type = "mmh3"):
        """
        epsilon: relative error, delta: failure probability
        for each hash function h, maintain the smallest hash value H
        z = median of depth averages of width smallest hash values
        return 1/z - 1
        """

        self.seed = []
        self.width = C*math.ceil(1/(epsilon*epsilon))
        self.depth = math.ceil(math.log(2,1/delta))
        self.seed_range = 2*C*self.depth*self.width
        self.hash_type = hash_type
        self.max_128_int = pow(2,128)-1

        # initialize the seeds for hash functions
        self.seed = [[random.randrange(1,self.seed_range) for j in range(self.width)] for i in range(self.depth)]
        self.smallest_hash =[[1 for j in range(self.width)] for i in range(self.depth)]


    def _hash(self, token, seed):
        """
        Compute the hash of a token.
        """

        return mmh3.hash128(token, seed, signed = False)/self.max_128_int


    def insert(self, token):
        """
        Insert a token into the sketch. Token must be byte-like objects.
        """

        for i in range(self.depth):
            for j in range(self.width):
                hash_value = self._hash(token, self.seed[i][j])
                if hash_value < self.smallest_hash[i][j]:
                    self.smallest_hash[i][j] = hash_value

    def estimator(self):
        """
        Return the estimate for the number of distinct elements inserted so far.
        """
        avg = [statistics.mean(self.smallest_hash[i]) for i in range(self.depth)]
        median_of_means = statistics.median(avg)
        return math.ceil((1/median_of_means)-1)
