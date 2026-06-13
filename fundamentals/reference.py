"""
REFERENCE — the answer key. Open ONLY when stuck >90 seconds.
Read until the missing piece clicks, then CLOSE this and retype the whole
function from memory in the drill file. Don't copy-paste.

Each solution has a one-line note on the part people forget.
"""

from collections import deque
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Reverse a linked list.
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


# Find the middle (second middle on even length).
# Forget-point: the loop condition `fast and fast.next` is what makes
# slow land on the second-middle / not crash.
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# Detect a cycle.
# Forget-point: same fast/slow skeleton; they collide iff there's a loop.
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# Delete the middle node (⌊n/2⌋-th, 0-indexed).
# Forget-point: keep a `prev` one step behind slow so you can splice it out;
# the fast/fast.next loop lands slow exactly on the middle. Single node -> None.
def delete_middle_node(head):
    if not head or not head.next:
        return None
    prev = None
    slow = fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next     # skip the middle
    return head


# Odd/Even linked list (group by POSITION, then reattach).
# Forget-point: stash the even-head BEFORE rewiring, and reattach it to the tail
# of the odd chain at the end. Loop while `even and even.next`.
def odd_even_list(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even          # remember where the evens start
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head      # odds, then evens
    return head


# BFS.
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


# Recursive DFS.
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


# Iterative DFS.
# Forget-point: check `if node in visited: continue` AFTER popping (a node can
# be on the stack multiple times). This is why its order differs from 7.
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


# Top K largest, descending.
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


# Binary search.
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


# Leftmost insertion point (lower_bound).
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


# Fixed-size sliding window.
# Forget-point: seed the first window's sum, then for each new element ADD it
# and SUBTRACT the one leaving (nums[i-k]) — don't recompute the whole sum.
def max_window_sum(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best


# Variable sliding window (longest substring w/o repeats).
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


# Max depth of a binary tree.   [tree / DFS recursion]
# Forget-point: base case `not root -> 0`, then 1 + max(children). The +1 is
# for the current node; recursing without it counts edges, not levels.
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# Level-order traversal.   [tree / BFS]
# Forget-point: snapshot len(q) BEFORE the inner loop so you process exactly the
# nodes on this level — its children get appended but stay out of this batch.
def level_order(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):          # fixed count = this level only
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


# Validate BST.   [BST / bounded recursion]
# Forget-point: pass DOWN a (low, high) range — checking only node vs its direct
# children misses a deep descendant that violates a far ancestor's bound. Strict.
def is_valid_bst(root):
    def ok(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return ok(node.left, low, node.val) and ok(node.right, node.val, high)
    return ok(root, float("-inf"), float("inf"))


# Search in a BST (return the subtree).   [BST search]
# Forget-point: use the ordering to pick ONE side each step (O(height)); don't
# fall back to scanning both subtrees like a generic tree search.
def search_bst(root, val):
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root


# Group anagrams.   [hash map grouping]
# Forget-point: the key is the canonical form — sorted letters (as a tuple, so
# it's hashable). Bucket every word under its key.
def group_anagrams(strs):
    groups = {}
    for w in strs:
        key = tuple(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())


# Number of islands.   [grid / flood fill]
# Forget-point: SINK each cell you enter (set it to 0) so it can't be recounted,
# and bounds/zero-check at the TOP of the helper so recursion terminates.
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def sink(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
            return
        grid[r][c] = 0                   # mark visited by sinking it
        sink(r + 1, c); sink(r - 1, c)
        sink(r, c + 1); sink(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1
                sink(r, c)
    return count


# 3Sum (unique triplets summing to 0).   [sort + two pointers]
# Forget-point: sort first; fix i, two-pointer the rest. Skip duplicate i's,
# AND after a hit skip duplicate lo/hi values — otherwise you emit repeats.
def three_sum(nums):
    nums = sorted(nums)
    res = []
    n = len(nums)
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue                     # skip duplicate anchor
        lo, hi = i + 1, n - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1              # skip dup
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1              # skip dup
    return res

# def three_sum(nums):
#     nums = sorted(nums)
#     res = []
#     n = len(nums)
#     for i in range(n - 2):
#         if nums[i] > 0:
#             break
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         seen = set()
#         for j in range(i + 1, n):
#             complement = -nums[i] - nums[j]
#             if complement in seen:
#                 res.append([nums[i], complement, nums[j]])
#                 # skip duplicate nums[j]
#                 while j + 1 < n and nums[j] == nums[j + 1]:
#                     j += 1
#             seen.add(nums[j])
#     return res

# def three_sum(nums):
#     res = set()
#     dups = set()
#     seen = {}
#     for i, a in enumerate(nums):
#         if a in dups:
#             continue
#         dups.add(a)
#         for j in range(i + 1, len(nums)):
#             b = nums[j]
#             complement = -a - b
#             if complement in seen and seen[complement] == i:
#                 res.add(tuple(sorted((a, b, complement))))
#             seen[b] = i
#     return [list(t) for t in res]


# Daily temperatures.   [monotonic stack]
# Forget-point: the stack holds INDICES with strictly decreasing temps. When the
# current day is warmer, pop those waiting indices and set answer = i - j.
def daily_temperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []                           # indices, temps decreasing
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


# Merge intervals.   [sort + sweep]
# Forget-point: SORT by start first. Then merge when next.start <= last.end,
# extending with max(last.end, next.end) — don't assume next is fully inside.
def merge_intervals(intervals):
    intervals = sorted(intervals)        # by start
    merged = []
    for iv in intervals:
        if merged and iv[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], iv[1])
        else:
            merged.append(list(iv))      # copy so we don't mutate the input
    return merged


# ████████████████████████████████████████████████████████████████████████████
# BONUS ANSWERS — these mirror the non-scoring bonus stubs. Same rule: read till
# it clicks, close, retype from memory.
# ████████████████████████████████████████████████████████████████████████████


# Delete a node in a BST.   [BST delete]
# Forget-point: reassign root.left/right = recurse so links rebind. The two-child
# case: copy the in-order successor (smallest in the RIGHT subtree) into this
# node, then delete THAT value from the right subtree.
def delete_bst_node(root, key):
    if not root:
        return None
    if key < root.val:
        root.left = delete_bst_node(root.left, key)
    elif key > root.val:
        root.right = delete_bst_node(root.right, key)
    else:
        if not root.left:
            return root.right            # 0 or 1 child
        if not root.right:
            return root.left
        succ = root.right                # in-order successor = min of right
        while succ.left:
            succ = succ.left
        root.val = succ.val
        root.right = delete_bst_node(root.right, succ.val)
    return root


# Subsets / power set.   [backtracking]
# Forget-point: the iterative trick — start with [[]] and for each num, add it
# to a COPY of every subset so far (doubling the count each pass).
def subsets(nums):
    res = [[]]
    for x in nums:
        res += [cur + [x] for cur in res]
    return res

    # --- explicit backtracking version ---
    # res = []
    # def go(i, path):
    #     if i == len(nums):
    #         res.append(path[:]); return
    #     path.append(nums[i]); go(i + 1, path)   # choose
    #     path.pop();          go(i + 1, path)    # un-choose
    # go(0, [])
    # return res


# Coin change (fewest coins).   [dynamic programming]
# Forget-point: dp[0] = 0, every other amount starts at infinity; dp[a] is the
# min over coins of dp[a-c]+1. Return -1 if dp[amount] is still infinity.
def coin_change(coins, amount):
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != INF else -1


# B1. Course schedule (can all courses finish?).   [topological sort / Kahn]
# Forget-point: edge direction — prereq [a, b] means b -> a. Push in-degree-0
# nodes, peel them, and you finish iff you process ALL nodes (no cycle left).
def course_schedule(num_courses, prerequisites):
    indeg = [0] * num_courses
    adj = [[] for _ in range(num_courses)]
    for a, b in prerequisites:
        adj[b].append(a)          # b before a
        indeg[a] += 1
    q = deque([i for i in range(num_courses) if indeg[i] == 0])
    seen = 0
    while q:
        node = q.popleft()
        seen += 1
        for nxt in adj[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return seen == num_courses    # all reached => acyclic


# Koko / min eating speed.   [binary search on the ANSWER]
# Forget-point: you're binary-searching the speed, not an array. Search space is
# 1..max(pile); feasibility (hours <= h) is monotonic, so use the lower_bound
# template and return lo. hours per pile = ceil(pile/speed).
def min_eating_speed(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        hours = sum((p + mid - 1) // mid for p in piles)
        if hours <= h:
            hi = mid              # feasible — try slower
        else:
            lo = mid + 1
    return lo


# Unique paths in an m x n grid.   [2D dynamic programming]
# Forget-point: each cell = paths-from-above + paths-from-left; first row/col are
# all 1. A single rolling row works: dp[j] += dp[j-1].
def unique_paths(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]


# Subarray sum equals k (count).   [prefix sum + hash map]
# Forget-point: seed {0: 1} so a prefix that itself equals k counts; for each
# running total, add how many earlier prefixes equal total - k.
def subarray_sum(nums, k):
    count = 0
    total = 0
    seen = {0: 1}                 # prefix-sum -> how many times seen
    for x in nums:
        total += x
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count


# Diameter of a binary tree.   [tree post-order aggregation]
# Forget-point: the answer is updated DURING a depth() helper — at each node the
# best path THROUGH it is left_depth + right_depth (edges), while the function
# RETURNS 1 + max(child depths) upward. Track best in an outer variable.
def diameter_of_binary_tree(root):
    best = 0

    def depth(node):
        nonlocal best
        if not node:
            return 0
        l = depth(node.left)
        r = depth(node.right)
        best = max(best, l + r)   # longest path bending at this node
        return 1 + max(l, r)

    depth(root)
    return best