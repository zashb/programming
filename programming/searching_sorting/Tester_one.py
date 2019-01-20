import One
import time

def main():
    one = One.One()
    
    # one.get_index_linear_search([1,2,3,4,5],3)
    
    # one.get_index_binary_search_recursive([1,2,3,4,5], 3)

    # print(one.get_index_binary_search_iterative([1,2,3,4,5],5))

    # print("last occurance of {} in {} is at index {}".format(21,[5, 6, 9, 12, 15, 21, 21, 34, 45, 57, 70, 84],one.get_last_occurance_binary_search([5, 6, 9, 12, 15, 21, 21, 34, 45, 57, 70, 84],21)))

    # print("first occurance of {} in {} is at index {}".format(21,[5, 6, 9, 12, 15, 21, 21, 34, 45, 57, 70, 84],one.get_first_occurance_binary_search([5, 6, 9, 12, 15, 21, 21, 34, 45, 57, 70, 84],21)))

    # print(one.check_duplicates_sorting([3, 2, 1, 2, 2, 3]))

    # print(one.find_sum_two_lists([2, 3, 5, 7, 12, 15, 23, 32, 42],[3, 13, 13, 15, 22, 33],45))

    # print(one.find_in_rotated_sorted_array([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5))

    # print(one.find_missing_number([8, 2, 1, 4, 6, 5, 7, 9]))

    # print(one.find_missing_number_in_range([10, 16, 14, 12, 11, 10, 13 , 15, 17, 12, 19]))

    # print(one.find_first_non_repeating_char("careermonk"))

    # print(one.find_first_repeated_among_repeated([3, 2, 1, 1, 2, 1, 2, 5, 5]))

    # start = time.time()
    # print(one.get_max_index_diff_brute_force([34, 8, 10, 3, 2, 80, 30, 33, 1]))
    # end = time.time()
    # print("time taken : {}".format(end - start))

    # start = time.time()
    # print(one.get_max_index_diff_efficient([34, 8, 10, 3, 2, 80, 30, 33, 1]))
    # end = time.time()
    # print("time taken : {}".format(end - start))

    # print(one.max_repitions_hash([3, 2, 1, 3, 2, 3, 2, 3, 3]))

    # start = time.time()
    # print(one.move_spaces_to_beginning("move these spaces to beginning"))
    # end = time.time()
    # print("time taken : {}".format(end - start))

    start = time.time()
    print(one.move_space_to_beginning_efficient("move these spaces to beginning"))
    end = time.time()
    print("time taken : {}".format(end - start))

if __name__ == '__main__':
    main()