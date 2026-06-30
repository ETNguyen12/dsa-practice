"""
06-30-2026 — DSA drills.  Fill in each function from memory, then click Run.
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
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


# ============================================================================
# 2. Find the middle node (second middle on even length). Fast/slow pointers.
# ============================================================================
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# ============================================================================
# 3. Detect a cycle in a linked list. Return True/False. Fast/slow pointers.
# ============================================================================
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# ============================================================================
# 4. [linked list] Delete the MIDDLE node (the floor(n/2)-th, 0-indexed) and
#     return the head. [1,2,3,4] -> [1,2,4]. [1] -> [] (None). Keep a prev pointer.
# ============================================================================
def delete_middle_node(head):
    if not head or not head.next:
        return None
    
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head


# ============================================================================
# 5. [linked list] Regroup so all ODD positions (1st,3rd,...) come first, then the
#     EVEN positions, preserving order. [1,2,3,4,5] -> [1,3,5,2,4]. By POSITION.
# ============================================================================
def odd_even_list(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head


# ============================================================================
# 6. BFS over an adjacency-list graph. Return nodes in first-visit order from
#     `start`, visiting neighbors in list order.
# ============================================================================
def bfs(graph, start):
    visited = {start}
    q = deque([start])
    order = []

    while q:
        node = q.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return order


# ============================================================================
# 7. Recursive DFS. Same return contract as bfs (visit order from `start`).
# ============================================================================
def dfs_recursive(graph, start):
    visited = set()
    order = []

    def dfs(node: ListNode) -> None:
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return order


# ============================================================================
# 8. Iterative DFS with an explicit stack. Same contract; order can differ from
#     the recursive version (see the test).
# ============================================================================
def dfs_iterative(graph, start):
    s = [start]
    res = []
    visited = set()

    while s:
        node = s.pop()
        if node in visited:
            continue
        visited.add(node)
        res.append(node)
        for neighbor in graph[node]:
            s.append(neighbor)
    return res


# ============================================================================
# 9. Return the k largest numbers from `nums`, sorted descending. Use a heap.
# ============================================================================
def top_k(nums, k):
    import heapq
    h = []
    for num in nums:
        heapq.heappush(h, num)
        if len(h) > k:
            heapq.heappop(h)
    return sorted(h, reverse=True)


# ============================================================================
# 10. Binary search. `nums` sorted ascending. Return index of `target`, else -1.
# ============================================================================
def binary_search(nums, target):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


# ============================================================================
# 11. Leftmost insertion point: index of the first element >= target.
#     [1,3,3,5], 3 -> 1.  4 -> 3.  6 -> 4.  0 -> 0.
# ============================================================================
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


# ============================================================================
# 12. Fixed-size sliding window. Max sum of any window of size k, in one pass.
# ============================================================================
def max_window_sum(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        best = max(best, window)
    return best


# ============================================================================
# 13. Variable sliding window. Length of the LONGEST substring of `s` with no
#     repeating characters. ("abcabcbb" -> 3, "bbbbb" -> 1)
# ============================================================================
def longest_unique_substring(s):
    seen = set()
    left, best = 0, 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best



# ============================================================================
# 14. [tree / DFS recursion] Max depth of a binary tree. Empty tree -> 0.
# ============================================================================
def max_depth(root):
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))


# ============================================================================
# 15. [tree / BFS] Level-order -> list of levels (each left-to-right, top-to-bottom).
#     [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]. [] -> [].
# ============================================================================
def level_order(root):
    if not root:
        return []

    q = deque([root])
    res = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


# ============================================================================
# 16. [BST / bounded recursion] True if a valid BST (every left subtree < node <
#     every right subtree, strictly).
# ============================================================================
def is_valid_bst(root):
    def valid(node, lo, hi) -> bool: 
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return valid(node.left, lo, node.val) and valid(node.right, node.val, hi)

    return valid(root, float('-inf'), float('inf'))


# ============================================================================
# 17. [BST search] Return the SUBTREE (node) whose value == val, else None. Use the
#     BST property — go left/right, don't scan the whole tree.
# ============================================================================
def search_bst(root, val):
    if not root:
        return None

    while root and root.val != val:
        root = root.left if root.val > val else root.right
    return root


# ============================================================================
# 18. [hash map grouping] Group anagrams together (order of/within groups free).
#     Key each word by its sorted letters.
# ============================================================================
def group_anagrams(strs):
    groups = {}
    for w in strs:
        letters = [0] * 26
        for c in w:
            letters[ord(c) - ord('a')] += 1
        groups.setdefault(tuple(letters), []).append(w)
    return list(groups.values())


# ============================================================================
# 19. [grid / flood fill] Count islands in a 2D grid of 0s and 1s, connected
#     4-directionally (up/down/left/right).
# ============================================================================
def num_islands(grid):
    if not grid:
        return 0
    
    count, rows, cols = 0, len(grid), len(grid[0])

    def dfs(r, c) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return
        grid[r][c] = 0
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1
                dfs(r, c)
    return count


# ============================================================================
# 20. [sort + two pointers] All UNIQUE triplets [a,b,c] with a+b+c == 0. No
#     duplicate triplets. [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]].
# ============================================================================
def three_sum(nums):
    nums.sort()
    res = []
    for i, n in enumerate(nums):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            threeSum = n + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                res.append([n, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left-1] == nums[left]:
                    left += 1
                while right > left and nums[right] == nums[right+1]:
                    right -= 1
    return res


# ============================================================================
# 21. [monotonic stack] For each day, how many days until a WARMER temperature
#     (0 if none). [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0].
# ============================================================================
def daily_temperatures(temperatures):
    res = [0] * len(temperatures)
    s = []
    for i, t in enumerate(temperatures):
        while s and temperatures[s[-1]] < t:
            j = s.pop()
            res[j] = i - j
        s.append(i)
    return res


# ============================================================================
# 22. [sort + sweep / intervals] Merge overlapping [start,end] intervals (unsorted
#     input). Return merged, sorted by start. [[1,3],[2,6],[8,10]] -> [[1,6],[8,10]].
# ============================================================================
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    res = []
    for start, end in intervals:
        if res and start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])
    return res


# ============================================================================
# 23. [BST delete] Delete the node with value `key`; return the (possibly new) root,
#     keeping the BST valid. Two-child case: replace with the in-order successor.
# ============================================================================
def delete_bst_node(root, key):
    if not root:
        return None
    if root.val > key:
        root.left = delete_bst_node(root.left, key)
    elif root.val < key:
        root.right = delete_bst_node(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        succ = root.right
        while succ.left:
            succ = succ.left
        root.val = succ.val
        root.right = delete_bst_node(root.right, root.val)
    return root


# ████████████████████████████████████████████████████████████████████████████
# BONUS — extra reps; these do NOT count toward your SCORE and never gate the
# timer or file cleanup. Solve them if you want, skip freely, or delete any.
# ████████████████████████████████████████████████████████████████████████████


# ============================================================================
# B1. [backtracking] Power set of distinct `nums` — every subset. Order free.
# ============================================================================
def subsets(nums):
    pass


# ============================================================================
# B2. [dynamic programming] Fewest coins (unlimited each) summing to `amount`, or -1
#     if impossible. coin_change([1,2,5],11) -> 3.
# ============================================================================
def coin_change(coins, amount):
    pass


# ============================================================================
# B3. [topological sort] True if all courses can finish (no cycle). prerequisites[i]
#     = [a, b] means b before a. course_schedule(2,[[1,0]]) -> True.
# ============================================================================
def course_schedule(num_courses, prerequisites):
    pass


# ============================================================================
# B4. [binary search on the answer] Smallest integer speed to eat all `piles` within
#     `h` hours (ceil(pile/speed) hours each). ([3,6,7,11], 8) -> 4.
# ============================================================================
def min_eating_speed(piles, h):
    pass


# ============================================================================
# B5. [2D dynamic programming] Unique paths top-left to bottom-right of an m x n grid
#     moving only right/down. unique_paths(3,7) -> 28.
# ============================================================================
def unique_paths(m, n):
    pass


# ============================================================================
# B6. [prefix sum + hash map] Count subarrays of `nums` whose sum equals k. Seed
#     {0: 1}. subarray_sum([1,1,1], 2) -> 2.
# ============================================================================
def subarray_sum(nums, k):
    pass


# ============================================================================
# B7. [tree post-order aggregation] Diameter = number of EDGES on the longest path
#     between any two nodes (may not pass through root). ([1,2,3,4,5]) -> 3.
# ============================================================================
def diameter_of_binary_tree(root):
    pass


if __name__ == "__main__":
    run_drills(globals())
