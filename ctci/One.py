class One(object):
    def get_sum_product(self, nums):
        sum = 0
        product = 1
        for i in nums:
            sum += i
            product *= i
        return [sum, product]

    def get_reverse(self, nums):
        n = len(nums)
        for i in range(n // 2):
            other = n - i - 1
            nums[other], nums[i] = nums[i], nums[other]
        return nums

    def is_prime(self, n):
        for i in range(2, int(n ** 0.5)):
            if n % i == 0:
                return False
        return True

    def get_factorial(self, n):
        if n < 0:
            return -1
        elif n == 0:
            return 1
        else:
            return n * self.get_factorial(n - 1)

    def get_all_string_permutations(self, string, prefix, result):
        if len(string) == 0:
            result.append(prefix)
        else:
            for i in range(len(string)):
                string2 = string[:i] + string[i + 1:]
                prefix2 = prefix + string[i]
                self.get_all_string_permutations(string2, prefix2, result)
        return result

    def get_first_n_fibonacci(self, n, result):
        memory = [-99] * n
        for i in range(n):
            result.append(self.get_fib(i, memory))
        return result

    def get_fib(self, i, memory):
        if i <= 0:
            return 0
        elif i == 1:
            return 1
        elif memory[i] > 0:
            return memory[i]
        memory[i] = self.get_fib(i - 1, memory) + self.get_fib(i - 2, memory)
        return memory[i]

    def get_sum_of_digits(self, num):
        _sum = 0
        while num > 0:
            _sum += num % 10
            num //= 10
        return _sum
