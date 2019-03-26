import collections

def main(nums,k):
    freqMap=collections.Counter(nums).most_common(k)
    return list(map(lambda x:x[0],freqMap))

if __name__ == '__main__':
    print(main([1,1,1,2,2,3],2))