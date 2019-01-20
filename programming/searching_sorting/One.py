class One(object):
    def __init__(self):
        pass
    
    def get_index_linear_search(self, nums, t):
        for i, j in enumerate(nums):
            if j == t:
                print(i)

    def get_index_binary_search_recursive(self, nums, t):
        nums = sorted(nums)
        mid = len(nums) // 2
        if t == nums[mid]:
            print(mid)
        elif t > nums[mid]:
            return self.get_index_binary_search(nums[mid:], t)
        else:
            return self.get_index_binary_search(nums[: mid + 1], t)
    
    def get_index_binary_search_iterative(self, nums, t):
        nums = sorted(nums)
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if t == nums[mid]:
                return mid
            elif t > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1        
    
    def get_last_occurance_binary_search(self, nums, t):
        nums = sorted(nums)
        low = 0
        high = len(nums) - 1
        lastFoundIndex = -1
        while low <= high:
            mid = (low + high) // 2
            if t == nums[mid]:
                lastFoundIndex = mid
                low = mid + 1
            elif t > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return lastFoundIndex

    def get_first_occurance_binary_search(self, nums, t):
        nums = sorted(nums)
        low = 0
        high = len(nums) - 1
        firstFoundIndex = -1
        while(low <= high):
            mid = (low + high) // 2
            if t == nums[mid]:
                firstFoundIndex = mid
                high = mid - 1
            elif t > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return firstFoundIndex

    def check_duplicates_sorting(self, nums):
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return "duplicates exist for {}".format(nums[i])
        return "no duplicates exist"

    def find_sum_two_lists(self, nums1, nums2, target_sum):
        nums1 = sorted(nums1) # because you do bin search later
        for i in nums2:
            diff = target_sum - i
            if self.get_index_binary_search_iterative(nums1, diff) != -1:
                return "target exists"
        return "target does not exist"

    def find_in_rotated_sorted_array(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return "{} found at index {} ".format(target, mid)
            if nums[mid] >= nums[low]:
                if nums[mid] > target >= nums[low]: # remember this step and write the outer if/else later
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return "target not found"

    def find_missing_number(self, nums):
        for i in range(1, len(nums)):
            found = 0
            for j in nums:
                if j == i:
                    found = 1
            if found == 0:
                return "missing number is {}".format(i)
        return "no missing number"

    def find_missing_number_in_range(self, nums):
        missing_num = float("-inf")
        S = [missing_num] * len(nums)
        X = min(nums)
        Y = max(nums)
        for i in nums:
            S[i - X] = i
        for i in range(len(nums)):
            if(S[i] == missing_num):
                return "missing number is {}".format(X + i)
        return "no number is missing"

    def find_first_non_repeating_char(self, string):
        hash = {}
        for i in string.lower():
            if i in hash:
                hash[i] += 1
            elif i != " ": # remember this for any char
                hash[i] = 1
            else:
                hash[i] = 0
        for i in string.lower():
            if hash[i] == 1:
                return "first non-repeating char in {} is {}".format(string, i)
        return "no non-repeating chars in {}".format(string)

    def find_first_repeated_among_repeated(self, nums):
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
            elif i != " ":
                hash[i] = 1
            else:
                hash[i] = 0
        for i in nums:
            if hash[i] > 1:
                return "first repeated element among repeated elements is {}".format(i)

    def get_max_index_diff_brute_force(self, nums):
        max_diff = max_left = max_right = -1
        n = len(nums)
        for i in range(n):
            j = n - 1
            while j > i:
                if nums[j] > nums[i] and (j - i) > max_diff:
                    max_diff = j - i
                    max_left = i
                    max_right = j
                j -= 1
        return "max diff is {}".format(max_diff)

    def get_max_index_diff_efficient(self, nums):
        n = len(nums)
        min_lefts = [0] * n
        min_lefts[0] = nums[0]
        max_rights = [0] * n
        max_rights[n - 1] = nums[n - 1]
        for i in range(1, n):
            min_lefts[i] = min(min_lefts[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            max_rights[i] = max(max_rights[i + 1], nums[i])
        left, right, max_diff = 0, 0, -1
        while left < n and right < n:
            if max_rights[right] > min_lefts[left]:
                max_diff = max(max_diff, right - left)
                right += 1
            else:
                left += 1
        return "max diff is {}".format(max_diff)

    def max_repitions_hash(self, nums):
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
            elif i != " ":
                hash[i] = 1
            else:
                hash[i] = 0
        max = 0
        for i in nums:
            if hash[i] > max:
                max = hash[i]
                max_element = i
        return "max repeated element is {}".format(max_element)

    def move_spaces_to_beginning(self, string):
        string_list = list(string)
        i = len(string) - 1
        for j in range(i, -1, -1):
            if not string_list[j].isspace():
                temp = string_list[i]
                string_list[i] = string_list[j]
                string_list[j] = temp
                i -= 1
        return "".join(string_list)

    def move_space_to_beginning_efficient(self, A):
        n = len(A) - 1
        datalist = list(A)
        count = n
        for j in range(n, 0, -1):
            if(not datalist[j].isspace()):
                datalist[count] = datalist[j]
                count -= 1
        while(count >= 0):
            datalist[count] = ' '
            count -= 1
        return ''.join(datalist)