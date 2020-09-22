def twoSum(nums, target):
    hashmap = {}
    for index, element in enumerate(nums):
        hashmap[element] = index
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]