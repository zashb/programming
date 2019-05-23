# """
# prob: Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that only one letter can be changed at a time and each intermediate word must exist in the dictionary. For example, given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# idea: queue of curr_word, curr_len
# comp:
# """
# from collections import deque
#
#
# def word_ladder(start, end, word_list):
#     # set of words to traverse
#     word_set = set()
#     for word in word_list:
#         word_set.add(word)
#     # since all words are the same len, we dont update the len later
#     word_len = len(start)
#     queue = deque([(start, 1)])
#     while queue:
#         curr_word, curr_len = queue.popleft()
#         if curr_word == end:
#             return curr_len
#         else:
#             for i in range(word_len):
#                 part1 = curr_word[:i]
#                 part2 = curr_word[i + 1:]
#                 for j in 'abcdefghijklmnopqrstuvwxyz':
#                     if curr_word[i] != j:
#                         next_word = part1 + j + part2
#                         if next_word in word_set:
#                             queue.append((next_word, curr_len + 1))
#                             word_set.remove(next_word)
#     return 0
#
#
# expected = 5
# actual = word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
# print(expected == actual)


# To check if strings differ by exactly one character
def is_adjacent(a, b):
    count = 0
    # Iterate through all characters and return false if there are more than one mismatching characters
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            break
    return count == 1


# Returns length of shortest chain to reach 'target' from 'start' using minimum number of adjacent moves
def shortest_chain_len(start, target, word_dict):
    # Create a queue for BFS and insert 'start' as source vertex
    stack = [[start, 1]]
    while len(stack) > 0:
        curr = stack.pop()
        # Go through all words of dictionary
        for i in word_dict:
            # Process a dictionary word if it is adjacent to current word (or vertex) of BFS
            temp = i
            if is_adjacent(curr[0], temp):
                # Add the dictionary word to Q
                item = [temp, curr[1] + 1]
                stack.append(item)
                # Remove from dictionary so that this word is not processed again. This is like marking visited
                word_dict.remove(temp)
                # If we reached target
                if temp == target:
                    return item[1]


expected = 7
actual = shortest_chain_len("toon", "plea", ["poon", "plee", "same", "poie", "plie", "poin", "plea"])
print(expected == actual)

expected = 6
actual = shortest_chain_len("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(expected == actual)
