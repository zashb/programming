def mapper(nums):
    mapOut = list(map(lambda x: (x, 1), nums))
    print("mapOut:\n", mapOut)
    return mapOut


def reducer(mapOut):
    reducerDict = {}
    for val, one in mapOut:
        if val in reducerDict:
            reducerDict[val] += one
        else:
            reducerDict[val] = 0
    print("reducerOut:\n", reducerDict)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    mapOut = mapper(nums)
    reducer(mapOut)
