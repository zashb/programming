from collections import OrderedDict


class Two(object):
    def has_unique_chars(self, string):
        if len(string.lower()) == len(set(string.lower())):
            return True
        else:
            return False


    def are_anagrams(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        if n1 != n2:
            return False
        sorted_s1 = self.get_merge_sort(list(s1), 0, n1 - 1)
        sorted_s2 = self.get_merge_sort(list(s2), 0, n2 - 1)
        for i in range(n1):
            if sorted_s1[i] != sorted_s2[i]:
                return False
        return True
    def get_merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self.get_merge_sort(arr, left, mid)
            self.get_merge_sort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)
        return arr
    def merge(self, arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        left_arr = [arr[left + i] for i in range(n1)]
        right_arr = [arr[mid + 1 + i] for i in range(n2)]
        i, j, k = 0, 0, left
        while i < n1 and j < n2:
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = right_arr[j]
            j += 1
            k += 1


    def can_form_palindrome(self, string):
        MAX_NO_OF_CHARS = 256
        count = [0] * MAX_NO_OF_CHARS
        for i in string:
            count[ord(i)] += 1
        odd = 0
        for i in range(MAX_NO_OF_CHARS):
            if count[i] & 1:
                odd += 1
            if odd > 1:
                return False
        return True


    def is_edit_distance_one(self, s1, s2):
        m = len(s1)
        n = len(s2)
        if abs(m - n) > 1:
            return False
        count = 0
        i = 0
        j = 0
        while i < m and j < n:
            if s1[i] != s2[j]:
                if count == 1:
                    return False
                if m > n:
                    i += 1
                elif m < n:
                    j += 1
                else:
                    i += 1
                    j += 1
                count += 1
            else:
                i += 1
                j += 1
        if i < m or j < n:
            count += 1
        return count == 1


    def get_run_length_encoding(self, string):
        if not string or len(string) == 0:
            return string
        prev = string[0]
        count = 1
        out_string = ""
        out_string += prev
        for i in range(1, len(string)):
            curr = string[i]
            if curr == prev:
                count += 1
            else:
                prev = curr
                out_string += str(count)
                out_string += curr
                count = 1
        out_string += str(count)
        if len(out_string) < len(string):
            return out_string
        else:
            return string
