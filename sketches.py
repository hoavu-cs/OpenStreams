

class Misra_Gries:

    # initialize
    def __init__(self, num_buckets = 1):
        self.num_buckets = num_buckets
        self.buckets = {}

    # insert an element to the data structure
    def insert(self, x):
        # if the element is already in a bucket
        if x in self.buckets:
            self.buckets[x] += 1
        else:
            # if there are still empty bucket(s)
            if len(self.buckets) < self.num_buckets:
                self.buckets[x] = 1
            else:
                for y in list(self.buckets):
                    self.buckets[y] -= 1
                    if self.buckets[y] == 0:
                        del self.buckets[y]

    # return the buckets of top counts
    # top counts are likely to be heavy hitters
    # be careful
    def top_buckets(self, amount):
        sorted_freq = sorted(self.buckets, key=self.buckets.get, reverse=True)

        sorted_buckets = {}
        for y in sorted_freq[:amount]:
            sorted_buckets[y] = self.buckets[y]

        return sorted_buckets


# Misra_Gries with time stamps to avoid duplicate insertions
# class Misra_Gries_With_Time_Stamp:
#
#     # initialize
#     def __init__(self, num_buckets = 1):
#         self.num_buckets = num_buckets
#         self.buckets = {}
#
#     # insert an element to the data structure
#     def insert(self, x, id):
#         # if the element is already in a bucket
#         if x in self.buckets:
#             # check for duplicates
#             if self.buckets[x]["id"] < id:
#                 self.buckets[x]["count"] += 1
#                 self.buckets[x]["id"] = id
#         else:
#             # if there are still empty bucket(s)
#             if len(self.buckets) < self.num_buckets:
#                 self.buckets[x] = {"count":1, "id": id}
#             else:
#                 for y in list(self.buckets):
#                     self.buckets[y]["count"] -= 1
#                     if self.buckets[y]["count"] == 0:
#                         del self.buckets[y]
#
#     # return the buckets of top counts
#     def top_buckets(self, amount):
#         buckets_no_id = {}
#         for y in self.buckets:
#             buckets_no_id[y] = self.buckets[y]["count"]
#
#         sorted_freq = sorted(buckets_no_id, key=buckets_no_id.get, reverse=True)
#         sorted_buckets = {}
#         for y in sorted_freq[:amount]:
#             sorted_buckets[y] = {}
#             sorted_buckets[y]["id"] = self.buckets[y]["id"]
#             sorted_buckets[y]["count"] = self.buckets[y]["count"]
#         return sorted_buckets
