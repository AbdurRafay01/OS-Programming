
list2 = [2,5, 11 , 15] # target = 6
target = 17
prev_value = dict()
index = 0
for i in range(len(list2)):
    num = list2[i]
    needval = target - num
    if needval in prev_value:
        print(prev_value[needval] , i)
    prev_value[num] = i

#just checking git from atom
def twoSumHashing(num_arr, pair_sum):

    hashTable = {}

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            print(hashTable[complement] , i)
        hashTable[num_arr[i]] = i

# Driver Code
num_arr = [4, 5, 1, 8]
pair_sum = 9

# Calling function
twoSumHashing(num_arr, pair_sum)
