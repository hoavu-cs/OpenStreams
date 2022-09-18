

class Misra_Gries:

    # initialize
    def __init__(self, num_buckets = 1):
        self.num_buckets = num_buckets
        self.buckets = {}

    # insert an element to the data structure
    def insert(self, token):
        # if the element is already in a bucket
        if token in self.buckets:
            self.buckets[token] += 1
        else:
            # if there are still empty bucket(s)
            if len(self.buckets) < self.num_buckets:
                self.buckets[token] = 1
            else:
                for y in list(self.buckets):
                    self.buckets[y] -= 1
                    if self.buckets[y] == 0:
                        del self.buckets[y]

    # return the buckets of top estimate counts
    # count - stream length/num_buckets <= estimate count <= count
    def top_buckets(self, amount):
        sorted_freq = sorted(self.buckets, key=self.buckets.get, reverse=True)

        sorted_buckets = {}
        for y in sorted_freq[:amount]:
            sorted_buckets[y] = self.buckets[y]

        return sorted_buckets
