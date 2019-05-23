import One
import Two


def main():
    # run_one_test_methods()
    run_two_test_methods()

def run_two_test_methods():
    two = Two.Two()
    string = "abcc"
    print("Does '{}' have all unique characters : {}".format(string, two.has_unique_chars(string)))
    s1, s2 = "test", "ttes"
    print("Are '{}' and '{}' anagrams : {}".format(s1, s2, two.are_anagrams(s1, s2)))
    string = "geeksogeeks"
    print("Can '{}' form a palindrome : {}".format(string, two.can_form_palindrome(string)))
    s1, s2 = "ab", "adc"
    print("Are '{}' and '{}' one edit distance : {}".format(s1, s2, two.is_edit_distance_one(s1, s2)))
    string = "geeksforgeeks"
    print("Run Length Encoding of '{}' is : {}".format(string, two.get_run_length_encoding(string)))

def run_one_test_methods():
    one = One.One()
    nums = [1, 2, 3, 4, 5]
    print("sum and product of '{}' are : '{}'".format(nums, one.get_sum_product(nums)))
    print("reverse of '{}' is '{}'".format(nums, one.get_reverse(nums)))
    n = 101
    print("is '{}' prime ? : '{}'".format(n, one.is_prime(n)))
    n = 5
    print("'{}' factorial is : '{}'".format(n, one.get_factorial(n)))
    string, prefix, result = "abc", "", []
    print("all permutations of '{}' are '{}'".format(string, one.get_all_string_permutations(string, prefix, result)))
    n, result = 10, []
    print("first '{}' fibonacci numbers are : '{}'".format(n, one.get_first_n_fibonacci(n, result)))
    num = 12345
    print("sum of digits in {} is {}".format(num, one.get_sum_of_digits(num)))


if __name__ == '__main__':
    main()
