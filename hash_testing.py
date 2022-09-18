import hashing

f = hashing.k_wise_hash(k=2, range = 100000)
for i in range(999999, 9999999, 100):
    print(f.hash(i))
