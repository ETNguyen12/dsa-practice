"""
06-12-2026 — DSA drills.  Fill in each function from memory, then click Run.
The test runner + timer live in start.py; you only edit the functions below.

  1. No reference.py until you've been stuck >90 seconds.
  2. On a peek, read till it clicks, then retype the WHOLE function from the top.
"""

import os, sys
from collections import deque
import heapq

# start.py sits in this same folder; make it importable, then pull the runner
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from start import run_drills, ListNode, TreeNode


# ============================================================================
# 1. Reverse a linked list. Return the new head.
# ============================================================================
def reverse_list(head):
    pass


# ============================================================================
# 2. Find the middle node (second middle on even length). Fast/slow pointers.
# ============================================================================
def find_middle(head):
    pass


# ============================================================================
# 3. Detect a cycle in a linked list. Return True/False. Fast/slow pointers.
# ============================================================================
def has_cycle(head):
    pass


# ============================================================================
# 4. [linked list] Delete the MIDDLE node (the floor(n/2)-th, 0-indexed) and
#     return the head. [1,2,3,4] -> [1,2,4]. [1] -> [] (None). Keep a prev pointer.
# ============================================================================
def delete_middle_node(head):
    pass


# ============================================================================
# 5. [linked list] Regroup so all ODD positions (1st,3rd,...) come first, then the
#     EVEN positions, preserving order. [1,2,3,4,5] -> [1,3,5,2,4]. By POSITION.
# ============================================================================
def odd_even_list(head):
    pass


# ============================================================================
# 6. BFS over an adjacency-list graph. Return nodes in first-visit order from
#     `start`, visiting neighbors in list order.
# ============================================================================
def bfs(graph, start):
    pass


# ============================================================================
# 7. Recursive DFS. Same return contract as bfs (visit order from `start`).
# ============================================================================
def dfs_recursive(graph, start):
    pass


# ============================================================================
# 8. Iterative DFS with an explicit stack. Same contract; order can differ from
#     the recursive version (see the test).
# ============================================================================
def dfs_iterative(graph, start):
    pass


# ============================================================================
# 9. Return the k largest numbers from `nums`, sorted descending. Use a heap.
# ============================================================================
def top_k(nums, k):
    pass


# ============================================================================
# 10. Binary search. `nums` sorted ascending. Return index of `target`, else -1.
# ============================================================================
def binary_search(nums, target):
    pass


# ============================================================================
# 11. Leftmost insertion point: index of the first element >= target.
#     [1,3,3,5], 3 -> 1.  4 -> 3.  6 -> 4.  0 -> 0.
# ============================================================================
def lower_bound(nums, target):
    pass


# ============================================================================
# 12. Fixed-size sliding window. Max sum of any window of size k, in one pass.
# ============================================================================
def max_window_sum(nums, k):
    pass


# ============================================================================
# 13. Variable sliding window. Length of the LONGEST substring of `s` with no
#     repeating characters. ("abcabcbb" -> 3, "bbbbb" -> 1)
# ============================================================================
def longest_unique_substring(s):
    pass


# ============================================================================
# 14. [tree / DFS recursion] Max depth of a binary tree. Empty tree -> 0.
# ============================================================================
def max_depth(root):
    pass


# ============================================================================
# 15. [tree / BFS] Level-order -> list of levels (each left-to-right, top-to-bottom).
#     [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]. [] -> [].
# ============================================================================
def level_order(root):
    pass


# ============================================================================
# 16. [BST / bounded recursion] True if a valid BST (every left subtree < node <
#     every right subtree, strictly).
# ============================================================================
def is_valid_bst(root):
    pass


# ============================================================================
# 17. [BST search] Return the SUBTREE (node) whose value == val, else None. Use the
#     BST property — go left/right, don't scan the whole tree.
# ============================================================================
def search_bst(root, val):
    pass


# ============================================================================
# 18. [BST delete] Delete the node with value `key`; return the (possibly new) root,
#     keeping the BST valid. Two-child case: replace with the in-order successor.
# ============================================================================
def delete_bst_node(root, key):
    pass


# ============================================================================
# 19. [grid / flood fill] Count islands in a 2D grid of 0s and 1s, connected
#     4-directionally (up/down/left/right).
# ============================================================================
def num_islands(grid):
    pass


# ============================================================================
# 20. [sort + two pointers] All UNIQUE triplets [a,b,c] with a+b+c == 0. No
#     duplicate triplets. [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]].
# ============================================================================
def three_sum(nums):
    pass


# ============================================================================
# 21. [monotonic stack] For each day, how many days until a WARMER temperature
#     (0 if none). [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0].
# ============================================================================
def daily_temperatures(temperatures):
    pass


# ============================================================================
# 22. [sort + sweep / intervals] Merge overlapping [start,end] intervals (unsorted
#     input). Return merged, sorted by start. [[1,3],[2,6],[8,10]] -> [[1,6],[8,10]].
# ============================================================================
def merge_intervals(intervals):
    pass


# ============================================================================
# 23. [backtracking] Power set of distinct `nums` — every subset. Order free.
# ============================================================================
def subsets(nums):
    pass


# ============================================================================
# 24. [dynamic programming] Fewest coins (unlimited each) summing to `amount`, or -1
#     if impossible. coin_change([1,2,5],11) -> 3.
# ============================================================================
def coin_change(coins, amount):
    pass


# ████████████████████████████████████████████████████████████████████████████
# BONUS — extra reps; these do NOT count toward your SCORE and never gate the
# timer or file cleanup. Solve them if you want, skip freely, or delete any.
# ████████████████████████████████████████████████████████████████████████████


# ============================================================================
# B1. [topological sort] True if all courses can finish (no cycle). prerequisites[i]
#     = [a, b] means b before a. course_schedule(2,[[1,0]]) -> True.
# ============================================================================
def course_schedule(num_courses, prerequisites):
    pass


# ============================================================================
# B2. [binary search on the answer] Smallest integer speed to eat all `piles` within
#     `h` hours (ceil(pile/speed) hours each). ([3,6,7,11], 8) -> 4.
# ============================================================================
def min_eating_speed(piles, h):
    pass


# ============================================================================
# B3. [2D dynamic programming] Unique paths top-left to bottom-right of an m x n grid
#     moving only right/down. unique_paths(3,7) -> 28.
# ============================================================================
def unique_paths(m, n):
    pass


# ============================================================================
# B4. [prefix sum + hash map] Count subarrays of `nums` whose sum equals k. Seed
#     {0: 1}. subarray_sum([1,1,1], 2) -> 2.
# ============================================================================
def subarray_sum(nums, k):
    pass


# ============================================================================
# B5. [hash map grouping] Group anagrams together (order of/within groups free).
#     Key each word by its sorted letters.
# ============================================================================
def group_anagrams(strs):
    pass


# ============================================================================
# B6. [tree post-order aggregation] Diameter = number of EDGES on the longest path
#     between any two nodes (may not pass through root). ([1,2,3,4,5]) -> 3.
# ============================================================================
def diameter_of_binary_tree(root):
    pass


if __name__ == "__main__":
    run_drills(globals())
