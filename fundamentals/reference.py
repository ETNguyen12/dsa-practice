"""
REFERENCE — the answer key. Open ONLY when stuck >90 seconds.
Read until the missing piece clicks, then CLOSE this and retype the whole
function from memory in drills.py. Don't copy-paste.

Each solution has a one-line note on the part people forget.
"""

from collections import deque
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. Reverse a linked list.
# Forget-point: save curr.next BEFORE you overwrite it.
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next      # save next
        curr.next = prev     # flip pointer backward
        prev = curr          # advance prev
        curr = nxt           # advance curr
    return prev              # prev is the new head


# 2. Find the middle (second middle on even length).
# Forget-point: the loop condition `fast and fast.next` is what makes
# slow land on the second-middle / not crash.
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# 3. Detect a cycle.
# Forget-point: same fast/slow skeleton; they collide iff there's a loop.
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# 4. BFS.
# Forget-point: mark visited at ENQUEUE time, not dequeue — otherwise a node
# can get pushed twice before it's processed.
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


# 5a. Recursive DFS.
# Forget-point: the visited set is shared across calls — pass it down (or close
# over it), don't recreate it each call.
def dfs_recursive(graph, start):
    visited = set()
    order = []

    def go(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                go(neighbor)

    go(start)
    return order


# 5b. Iterative DFS.
# Forget-point: check `if node in visited: continue` AFTER popping (a node can
# be on the stack multiple times). This is why its order differs from 5a.
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            stack.append(neighbor)
    return order


# 6. Top K largest, descending.
# Forget-point: heapq is a MIN-heap. nlargest is the clean way; the manual way
# below keeps a size-k min-heap and evicts the smallest.
def top_k(nums, k):
    return heapq.nlargest(k, nums)

    # --- manual version, if asked to do it by hand ---
    # h = []
    # for n in nums:
    #     heapq.heappush(h, n)
    #     if len(h) > k:
    #         heapq.heappop(h)      # drop the smallest
    # return sorted(h, reverse=True)


# 7. Binary search.
# Forget-point: use `lo <= hi` (not `<`) so a single-element range is checked,
# and move past mid with mid+1 / mid-1 or you'll infinite-loop.
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# 8. Leftmost insertion point (lower_bound).
# Forget-point: this is the "boundary" template, NOT the find template. Use a
# half-open range hi = len(nums), condition `lo < hi`, and on the >= branch set
# hi = mid (don't skip mid — it might be the answer). lo is the result.
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid          # keep mid in range — it could be the boundary
    return lo


# 9. Fixed-size sliding window.
# Forget-point: seed the first window's sum, then for each new element ADD it
# and SUBTRACT the one leaving (nums[i-k]) — don't recompute the whole sum.
def max_window_sum(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best


# 10. Variable sliding window (longest substring w/o repeats).
# Forget-point: when you hit a repeat, shrink from the LEFT in a while-loop
# until the duplicate is gone — a single left+=1 isn't enough.
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
