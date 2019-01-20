def calculateSpan(price):
    span = [None] * len(price)
    span[0] = 1
    for i in range(1, len(price)):
        span[i] = 1
        j = i - 1
        # traverse left when price on left < price on right
        while j >= 0 and price[j] <= price[i]:
            span[i] += 1
            j -= 1
    print(span)


if __name__ == "__main__":
    price = [10, 4, 5, 90, 120, 80]
    calculateSpan(price)
