"""
06-11-2026 — DSA drills.  Fill in each function from memory, then click Run.
The test runner + timer live in start.py; you only edit the functions below.

  1. No reference.py until you've been stuck >90 seconds.
  2. On a peek, read till it clicks, then retype the WHOLE function from the top.
"""

import os, sys
from collections import deque
import heapq

# start.py sits in this same folder; make it importable, then pull the runner
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from start import run_drills, ListNode


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
# 2. Find the middle node (for even length, return the second middle).
#    Use fast/slow pointers.
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
        if slow == fast:
            return True
    return False


# ============================================================================
# 4. BFS over a graph (adjacency list: dict[node] -> list[neighbors]).
#    Return the list of nodes in the order they are first visited, starting
#    from `start`. Visit neighbors in the order they appear in the list.
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
# 5a. Recursive DFS. Same return contract as bfs (visit order from `start`).
# ============================================================================
def dfs_recursive(graph, start):
    visited = set()
    order = []

    def go(node: ListNode) -> None:
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                go(neighbor)

    go(start)
    return order


# ============================================================================
# 5b. Iterative DFS using an explicit stack. Same return contract.
#     (Order can differ from the recursive version — see the test.)
# ============================================================================
def dfs_iterative(graph, start):
    visited = set()
    s = [start]
    order = []

    while s:
        node = s.pop()
        if node in visited:
            continue
        order.append(node)
        visited.add(node)
        for neighbor in graph[node]:
            s.append(neighbor)
    return order


# ============================================================================
# 6. Return the k largest numbers from `nums`, sorted descending. Use a heap.
# ============================================================================
def top_k(nums, k):
    h = []
    for num in nums:
        heapq.heappush(h, num)
        if len(h) > k:
            heapq.heappop(h)
    return sorted(h, reverse=True)


# ============================================================================
# 7. Binary search. `nums` is sorted ascending. Return the index of `target`,
#    or -1 if not present.
# ============================================================================
def binary_search(nums, target):
    lo, hi = 0, len(nums) -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ============================================================================
# 8. Leftmost insertion point. Return the index of the first element >= target
#    (i.e. where you'd insert target to keep nums sorted, choosing the leftmost
#    valid spot). For nums=[1,3,3,5], target=3 -> 1. target=4 -> 3. target=6 -> 4.
# ============================================================================
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


# ============================================================================
# 9. Fixed-size sliding window. Return the maximum sum of any window of size k.
#    Assume 1 <= k <= len(nums). Do it in one pass (slide, don't re-sum).
# ============================================================================
def max_window_sum(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        best = max(best, window)
    return best


# ============================================================================
# 10. Variable sliding window. Return the length of the LONGEST substring of
#     `s` with no repeating characters. ("abcabcbb" -> 3, "bbbbb" -> 1)
# ============================================================================
def longest_unique_substring(s):
    seen = set()
    left = 0
    best = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    run_drills(globals())
