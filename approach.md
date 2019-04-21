### Search:
+ Linear search
    + Comp : O(n)
+ Binary search
    + sorting is prerequisite
    + Comp : O(log n)
+ BST
    + no duplicates
    + Comp : O(h) avg, O(n) worst
___
### Sort:
+ Merge
    + Comp : O(n log n)
    + Choose sorted() over .sort() to not edit the input arr unless asked to optimize for space
+ Topological
    + Comp : O(V + E)
    + Look for **"prerequiste", "dependency"**
    + Only sorting algorithm for graph vertices
    + Only for DAG (directed acyclic graph)
+ Heap
    + Comp : O(n log n)
    + Either by .heapify() or .push() to empty heap
    + Mostly used to find nsmallest / nlargest
___
### Backtrack / recursion:
+ Look for **"all possible"**
+ Ask if stack space is not a issue
+ Problem types : all string permutations, all subsets, all palindrome partitions, DFS, topological sort
___
### Dynamic Programming:
+ Comp : O(n^2)
+ Reach a greater state from a lower state
+ Problem types : longest common substring, word split
___
### Greedy:
+ Best choice for as of that point
+ Problem types : activity selection, platform allocation, minimum number of coins
___
### Sliding window:
+ In any sliding window prob, we have **2 ptrs**.
    +  One right pointer whose job is to expand the current window and then we have the left pointer whose job is to contract a given window.
    + At any point in time only one of these pointers move and the other one remains fixed.
___
### Subarray:
+ Check if contiguous elements or not
+ Total number of subarrays : n * (n + 1) / 2
+ Problem Types: 
    + continuous subarray: len of longest, max sum, max len of equal 0 and 1