list = [12, 5, 8, 8, 23, 15, 7, 8, 9, 12, 34, 6, 9, 16, 8, 23, 12, 7, 5, 3]
bus_capacity = 100


def getSum(list):
    sum = 0
    for num in list:
        sum = sum + num
    return sum


def findPackagesToLoad(list, bus_capacity):
    return findPackagesToLoadHelper(list, [], 0, bus_capacity)


def findPackagesToLoadHelper(list, targetList, i, bus_capacity):
    if getSum(targetList) > bus_capacity:
        return [-1]
    if i == len(list) - 1:
        return targetList
    else:
        loaded = findPackagesToLoadHelper(
            list, targetList + [list[i]], i+1, bus_capacity)
        left = findPackagesToLoadHelper(list, targetList, i+1, bus_capacity)
        if getSum(loaded) > getSum(left):
            return loaded
        else:
            return left


loaded = findPackagesToLoad(list, bus_capacity)
print(loaded)
print(getSum(loaded))
