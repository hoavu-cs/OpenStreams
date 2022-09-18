import sketches


test_input = [1,2,1,1,3,4,2,2,2,3,3,4,4,4,4,4,4]

summary = sketches.Misra_Gries(2)

for i in test_input:
    summary.insert(i)
    print("insert " + str(i))
    print(str(summary.buckets))
