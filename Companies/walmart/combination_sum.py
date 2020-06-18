l = [2, 4, 4, 5]
s = [1, 3, 5, 7]
k = 8

result = []
r = []
def sortsample(array_sample):
    d = []
    for i in range(0, len(array_sample)) :
        t = []
        d = array_sample[i] + array_sample[i + 1]
        t.append(array_sample[i])
        t.append(array_sample[i + 1])
        if d == k:
           result.append("True Set")
           print(array_sample[i], array_sample[i + 1])
           return result

def binary(array_sample):
    lenght = len(array_sample) % 2
    print(lenght)
    for i in range(0, len(array_sample)) :
        t = []
        d = array_sample[i] + array_sample[i + 1]
        t.append(array_sample[i])
        t.append(array_sample[i + 1])
        if d == k:
            result.append("True Set")
            print(array_sample[i], array_sample[i + 1])
            return result

print("Successful Combination " + str(len(sortsample(s))))
print("Successful Combination " + str(len(sortsample(l))))
