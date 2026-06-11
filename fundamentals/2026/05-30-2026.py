"""
DRILL FILE — fill in each function from memory, then run:  python drills.py

Rules:
  1. Do NOT open reference.py until you've been stuck >90 seconds.
  2. When you peek, read only until it clicks, close it, and retype the
     WHOLE function from the top — not just the line you forgot.
  3. Track your score (printed at the bottom) every morning.

Goal: all 10 passing, cold, no peeks, in under ~13 minutes total.
"""

from collections import deque
import heapq


# --- shared types -----------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================================
# 1. Reverse a linked list. Return the new head.
# ============================================================================
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
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

    def go(node):
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


# ============================================================================
# 6. Return the k largest numbers from `nums`, sorted descending. Use a heap.
# ============================================================================
def top_k(nums, k):
    h = []
    for n in nums:
        heapq.heappush(h, n)
        if len(h) > k:
            heapq.heappop(h)
    return sorted(h, reverse=True)


# ============================================================================
# 7. Binary search. `nums` is sorted ascending. Return the index of `target`,
#    or -1 if not present.
# ============================================================================
def binary_search(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ============================================================================
# 8. Leftmost insertion point. Return the index of the first element >= target
#    (i.e. where you'd insert target to keep nums sorted, choosing the leftmost
#    valid spot). For nums=[1,3,3,5], target=3 -> 1. target=4 -> 3. target=6 -> 4.
# ============================================================================
def lower_bound(nums, target):
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


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
        best = max(best, right-left+1)
    return best


# ============================================================================
# TEST RUNNER — don't edit below this line
# ============================================================================
def _build(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def _run():
    results = []

    # 1. reverse
    try:
        ok = (_to_list(reverse_list(_build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
              and _to_list(reverse_list(_build([]))) == []
              and _to_list(reverse_list(_build([1]))) == [1])
        results.append(("reverse_list", ok))
    except Exception as e:
        results.append(("reverse_list", f"crashed: {e}"))

    # 2. find_middle
    try:
        ok = (find_middle(_build([1, 2, 3, 4, 5])).val == 3
              and find_middle(_build([1, 2, 3, 4])).val == 3)
        results.append(("find_middle", ok))
    except Exception as e:
        results.append(("find_middle", f"crashed: {e}"))

    # 3. has_cycle
    try:
        a = ListNode(1); b = ListNode(2); c = ListNode(3)
        a.next = b; b.next = c; c.next = a            # cycle
        ok = has_cycle(a) is True and has_cycle(_build([1, 2, 3])) is False
        results.append(("has_cycle", ok))
    except Exception as e:
        results.append(("has_cycle", f"crashed: {e}"))

    g = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}

    # 4. bfs
    try:
        ok = bfs(g, 0) == [0, 1, 2, 3]
        results.append(("bfs", ok))
    except Exception as e:
        results.append(("bfs", f"crashed: {e}"))

    # 5a. dfs_recursive  (0 -> 1 -> 3 -> 2)
    try:
        ok = dfs_recursive(g, 0) == [0, 1, 3, 2]
        results.append(("dfs_recursive", ok))
    except Exception as e:
        results.append(("dfs_recursive", f"crashed: {e}"))

    # 5b. dfs_iterative — stack reverses neighbor order (0 -> 2 -> 3 -> 1)
    try:
        ok = dfs_iterative(g, 0) == [0, 2, 3, 1]
        results.append(("dfs_iterative", ok))
    except Exception as e:
        results.append(("dfs_iterative", f"crashed: {e}"))

    # 6. top_k
    try:
        ok = (top_k([3, 1, 8, 2, 9, 4], 3) == [9, 8, 4]
              and top_k([5], 1) == [5])
        results.append(("top_k", ok))
    except Exception as e:
        results.append(("top_k", f"crashed: {e}"))

    # 7. binary_search
    try:
        ok = (binary_search([1, 3, 5, 7, 9], 7) == 3
              and binary_search([1, 3, 5, 7, 9], 1) == 0
              and binary_search([1, 3, 5, 7, 9], 9) == 4
              and binary_search([1, 3, 5, 7, 9], 4) == -1
              and binary_search([], 1) == -1)
        results.append(("binary_search", ok))
    except Exception as e:
        results.append(("binary_search", f"crashed: {e}"))

    # 8. lower_bound
    try:
        ok = (lower_bound([1, 3, 3, 5], 3) == 1
              and lower_bound([1, 3, 3, 5], 4) == 3
              and lower_bound([1, 3, 3, 5], 6) == 4
              and lower_bound([1, 3, 3, 5], 0) == 0)
        results.append(("lower_bound", ok))
    except Exception as e:
        results.append(("lower_bound", f"crashed: {e}"))

    # 9. max_window_sum
    try:
        ok = (max_window_sum([2, 1, 5, 1, 3, 2], 3) == 9
              and max_window_sum([1, 2, 3], 3) == 6
              and max_window_sum([4], 1) == 4)
        results.append(("max_window_sum", ok))
    except Exception as e:
        results.append(("max_window_sum", f"crashed: {e}"))

    # 10. longest_unique_substring
    try:
        ok = (longest_unique_substring("abcabcbb") == 3
              and longest_unique_substring("bbbbb") == 1
              and longest_unique_substring("pwwkew") == 3
              and longest_unique_substring("") == 0)
        results.append(("longest_unique_substring", ok))
    except Exception as e:
        results.append(("longest_unique_substring", f"crashed: {e}"))

    print("\n" + "=" * 40)
    passed = 0
    for name, res in results:
        if res is True:
            print(f"  PASS   {name}")
            passed += 1
        elif res is False:
            print(f"  FAIL   {name}  (wrong output)")
        else:
            print(f"  ERROR  {name}  ({res})")
    print("=" * 40)
    print(f"  SCORE: {passed}/{len(results)} cold")
    print("=" * 40 + "\n")


if __name__ == "__main__":
    _run()
