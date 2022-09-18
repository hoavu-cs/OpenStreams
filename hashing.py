from Crypto.Util import number
from random import randrange

# generate a hash function from a k-wise family
class k_wise_hash():
    # initialize
    def __init__(self, k=2, prime=598509562964657, range=598509562964657-1):
        self.prime = prime
        self.range = range
        self.k = k

    def hash(self, x):
        output = randrange(1,self.prime-1)
        for i in range(1,self.k):
            output = output+pow(x,i)*randrange(0,self.prime-1)

        return (output % self.prime) % self.range
