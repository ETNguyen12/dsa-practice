"""
DRILL GENERATOR + SHARED TEST RUNNER

Daily workflow:
  1. Run THIS file each morning:   python start.py
     -> stamps a fresh MM-DD-YYYY.py (just the stubs) beside start.py, opens it.
     -> if today's file already exists, stamps the NEXT one: MM-DD-YYYY_2.py,
        _3.py, ... (a fresh cold attempt). Same-day files live side by side.
     -> running start.py does NOT start any timer.
  2. Fill in the functions and click Run. The clock starts on that first run.
  3. On a timed full clear of the CORE set, every EARLIER DAY's file is deleted.
     Today's own siblings are kept until a later day is full-scored.

╔══════════════════════════════════════════════════════════════════════════╗
║  TO REORDER OR RE-TIER PROBLEMS: just edit the CORE and BONUS lists below. ║
║  - Order of names = order they appear in the stamped file and the results. ║
║  - CORE names count toward SCORE and gate the timer/cleanup.               ║
║  - BONUS names run but never affect SCORE/timer/cleanup.                   ║
║  - Move a name between the two lists to re-tier it. Delete a name to drop  ║
║    it. To ADD a new problem, add an entry to PROBLEMS (sig/desc/test) too. ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import time, os
from collections import deque
import heapq


# ============================================================================
# EDIT HERE — the only things you normally touch
# ============================================================================
CORE = [
    # linked list
    "reverse_list", "delete_middle_node", "odd_even_list",
    # graph
    "dfs_iterative", "bfs", "dfs_recursive",
    # heap
    "top_k",
    # binary search
    "binary_search", "lower_bound",
    # sliding window
    "max_window_sum", "longest_unique_substring",
    # trees / BST
    "max_depth", "level_order", "is_valid_bst", "search_bst",
    # hash map grouping
    "group_anagrams",
    # grid
    "num_islands",
    # arrays / stack 
    "three_sum", "daily_temperatures", 
    # intervals 
    "merge_intervals", 
    # BST
    "delete_bst_node",
    # backtracking 
    "subsets",
    # binary search on the answer
    "min_eating_speed",
    # prefix sum + hash map
    "subarray_sum",

]

BONUS = [
    "coin_change",              # dp
    "course_schedule",          # topological sort
    "unique_paths",             # 2D dynamic programming
    "diameter_of_binary_tree",  # tree post-order aggregation
]

DEPRECATED = [
    "find_middle", 
    "has_cycle"
]
# ============================================================================


# --- shared types (imported by daily files) ---------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- test helpers -----------------------------------------------------------
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


def _build_tree(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals):
            if vals[i] is not None:
                node.left = TreeNode(vals[i]); q.append(node.left)
            i += 1
        if i < len(vals):
            if vals[i] is not None:
                node.right = TreeNode(vals[i]); q.append(node.right)
            i += 1
    return root


def _inorder(root):
    out = []
    def go(n):
        if not n:
            return
        go(n.left); out.append(n.val); go(n.right)
    go(root)
    return out


_G = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}


# --- tests: each takes ns (the daily file's globals) and returns True/False --
def _t_reverse_list(ns):
    f = ns["reverse_list"]
    return (_to_list(f(_build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
            and _to_list(f(_build([]))) == []
            and _to_list(f(_build([1]))) == [1])

def _t_find_middle(ns):
    f = ns["find_middle"]
    return f(_build([1, 2, 3, 4, 5])).val == 3 and f(_build([1, 2, 3, 4])).val == 3

def _t_has_cycle(ns):
    f = ns["has_cycle"]
    a = ListNode(1); b = ListNode(2); c = ListNode(3)
    a.next = b; b.next = c; c.next = a
    return f(a) is True and f(_build([1, 2, 3])) is False

def _t_delete_middle_node(ns):
    f = ns["delete_middle_node"]
    return (_to_list(f(_build([1, 3, 4, 7, 1, 2, 6]))) == [1, 3, 4, 1, 2, 6]
            and _to_list(f(_build([1, 2, 3, 4]))) == [1, 2, 4]
            and _to_list(f(_build([2, 1]))) == [2]
            and _to_list(f(_build([1]))) == [])

def _t_odd_even_list(ns):
    f = ns["odd_even_list"]
    return (_to_list(f(_build([1, 2, 3, 4, 5]))) == [1, 3, 5, 2, 4]
            and _to_list(f(_build([2, 1, 3, 5, 6, 4, 7]))) == [2, 3, 6, 7, 1, 5, 4]
            and _to_list(f(_build([]))) == []
            and _to_list(f(_build([1]))) == [1])

def _t_bfs(ns):
    return ns["bfs"](_G, 0) == [0, 1, 2, 3]

def _t_dfs_recursive(ns):
    return ns["dfs_recursive"](_G, 0) == [0, 1, 3, 2]

def _t_dfs_iterative(ns):
    return ns["dfs_iterative"](_G, 0) == [0, 2, 3, 1]

def _t_top_k(ns):
    f = ns["top_k"]
    return f([3, 1, 8, 2, 9, 4], 3) == [9, 8, 4] and f([5], 1) == [5]

def _t_binary_search(ns):
    f = ns["binary_search"]
    return (f([1, 3, 5, 7, 9], 7) == 3 and f([1, 3, 5, 7, 9], 1) == 0
            and f([1, 3, 5, 7, 9], 9) == 4 and f([1, 3, 5, 7, 9], 4) == -1
            and f([], 1) == -1)

def _t_lower_bound(ns):
    f = ns["lower_bound"]
    return (f([1, 3, 3, 5], 3) == 1 and f([1, 3, 3, 5], 4) == 3
            and f([1, 3, 3, 5], 6) == 4 and f([1, 3, 3, 5], 0) == 0)

def _t_max_window_sum(ns):
    f = ns["max_window_sum"]
    return f([2, 1, 5, 1, 3, 2], 3) == 9 and f([1, 2, 3], 3) == 6 and f([4], 1) == 4

def _t_longest_unique_substring(ns):
    f = ns["longest_unique_substring"]
    return (f("abcabcbb") == 3 and f("bbbbb") == 1 and f("pwwkew") == 3 and f("") == 0)

def _t_max_depth(ns):
    f = ns["max_depth"]
    return (f(_build_tree([3, 9, 20, None, None, 15, 7])) == 3
            and f(_build_tree([])) == 0 and f(_build_tree([1])) == 1
            and f(_build_tree([1, 2, None, 3])) == 3)

def _t_level_order(ns):
    f = ns["level_order"]
    return (f(_build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
            and f(_build_tree([])) == [] and f(_build_tree([1])) == [[1]])

def _t_is_valid_bst(ns):
    f = ns["is_valid_bst"]
    return (f(_build_tree([2, 1, 3])) is True
            and f(_build_tree([5, 1, 4, None, None, 3, 6])) is False
            and f(_build_tree([5, 4, 6, None, None, 3, 7])) is False
            and f(_build_tree([1])) is True)

def _t_search_bst(ns):
    f = ns["search_bst"]
    r = f(_build_tree([4, 2, 7, 1, 3]), 2)
    return (r is not None and r.val == 2 and _inorder(r) == [1, 2, 3]
            and f(_build_tree([4, 2, 7, 1, 3]), 5) is None)

def _t_delete_bst_node(ns):
    f = ns["delete_bst_node"]
    return (_inorder(f(_build_tree([5, 3, 6, 2, 4, None, 7]), 3)) == [2, 4, 5, 6, 7]
            and _inorder(f(_build_tree([5, 3, 6, 2, 4, None, 7]), 7)) == [2, 3, 4, 5, 6]
            and _inorder(f(_build_tree([5, 3, 6, 2, 4, None, 7]), 5)) == [2, 3, 4, 6, 7]
            and _inorder(f(_build_tree([1]), 1)) == [])

def _t_num_islands(ns):
    f = ns["num_islands"]
    return (f([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]) == 3
            and f([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]) == 1
            and f([[0, 0], [0, 0]]) == 0)

def _t_three_sum(ns):
    f = ns["three_sum"]
    def norm(ts): return sorted(tuple(sorted(t)) for t in ts)
    return (norm(f([-1, 0, 1, 2, -1, -4])) == norm([[-1, -1, 2], [-1, 0, 1]])
            and norm(f([0, 0, 0])) == [(0, 0, 0)]
            and f([0, 1, 1]) == [])

def _t_daily_temperatures(ns):
    f = ns["daily_temperatures"]
    return (f([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
            and f([30, 40, 50, 60]) == [1, 1, 1, 0]
            and f([30, 60, 90]) == [1, 1, 0])

def _t_merge_intervals(ns):
    f = ns["merge_intervals"]
    return (f([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
            and f([[1, 4], [4, 5]]) == [[1, 5]]
            and f([[1, 4], [0, 2], [3, 5]]) == [[0, 5]])

def _t_subsets(ns):
    f = ns["subsets"]
    def norm(xss): return sorted(tuple(sorted(x)) for x in xss)
    return (norm(f([1, 2, 3])) == norm([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
            and norm(f([])) == [()] and norm(f([0])) == [(), (0,)])

def _t_coin_change(ns):
    f = ns["coin_change"]
    return (f([1, 2, 5], 11) == 3 and f([2], 3) == -1 and f([1], 0) == 0
            and f([1, 5, 10, 25], 30) == 2)

# bonus tests
def _t_course_schedule(ns):
    f = ns["course_schedule"]
    return (f(2, [[1, 0]]) is True and f(2, [[1, 0], [0, 1]]) is False
            and f(4, [[1, 0], [2, 1], [3, 2]]) is True)

def _t_min_eating_speed(ns):
    f = ns["min_eating_speed"]
    return (f([3, 6, 7, 11], 8) == 4 and f([30, 11, 23, 4, 20], 5) == 30
            and f([30, 11, 23, 4, 20], 6) == 23)

def _t_unique_paths(ns):
    f = ns["unique_paths"]
    return f(3, 7) == 28 and f(3, 2) == 3 and f(1, 1) == 1

def _t_subarray_sum(ns):
    f = ns["subarray_sum"]
    return f([1, 1, 1], 2) == 2 and f([1, 2, 3], 3) == 2 and f([1, -1, 0], 0) == 3

def _t_group_anagrams(ns):
    f = ns["group_anagrams"]
    def norm(gs): return sorted(tuple(sorted(g)) for g in gs)
    return norm(f(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
        norm([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

def _t_diameter_of_binary_tree(ns):
    f = ns["diameter_of_binary_tree"]
    return (f(_build_tree([1, 2, 3, 4, 5])) == 3 and f(_build_tree([1])) == 0
            and f(_build_tree([1, 2])) == 1)


# --- the registry: sig + description + test for every problem ---------------
PROBLEMS = {
    "reverse_list": dict(sig="reverse_list(head)", test=_t_reverse_list,
        desc="Reverse a linked list. Return the new head."),
    "find_middle": dict(sig="find_middle(head)", test=_t_find_middle,
        desc="Find the middle node (second middle on even length). Fast/slow pointers."),
    "has_cycle": dict(sig="has_cycle(head)", test=_t_has_cycle,
        desc="Detect a cycle in a linked list. Return True/False. Fast/slow pointers."),
    "delete_middle_node": dict(sig="delete_middle_node(head)", test=_t_delete_middle_node,
        desc="[linked list] Delete the MIDDLE node (the floor(n/2)-th, 0-indexed) and\n"
             "return the head. [1,2,3,4] -> [1,2,4]. [1] -> [] (None). Keep a prev pointer."),
    "odd_even_list": dict(sig="odd_even_list(head)", test=_t_odd_even_list,
        desc="[linked list] Regroup so all ODD positions (1st,3rd,...) come first, then the\n"
             "EVEN positions, preserving order. [1,2,3,4,5] -> [1,3,5,2,4]. By POSITION."),
    "bfs": dict(sig="bfs(graph, start)", test=_t_bfs,
        desc="BFS over an adjacency-list graph. Return nodes in first-visit order from\n"
             "`start`, visiting neighbors in list order."),
    "dfs_recursive": dict(sig="dfs_recursive(graph, start)", test=_t_dfs_recursive,
        desc="Recursive DFS. Same return contract as bfs (visit order from `start`)."),
    "dfs_iterative": dict(sig="dfs_iterative(graph, start)", test=_t_dfs_iterative,
        desc="Iterative DFS with an explicit stack. Same contract; order can differ from\n"
             "the recursive version (see the test)."),
    "top_k": dict(sig="top_k(nums, k)", test=_t_top_k,
        desc="Return the k largest numbers from `nums`, sorted descending. Use a heap."),
    "binary_search": dict(sig="binary_search(nums, target)", test=_t_binary_search,
        desc="Binary search. `nums` sorted ascending. Return index of `target`, else -1."),
    "lower_bound": dict(sig="lower_bound(nums, target)", test=_t_lower_bound,
        desc="Leftmost insertion point: index of the first element >= target.\n"
             "[1,3,3,5], 3 -> 1.  4 -> 3.  6 -> 4.  0 -> 0."),
    "max_window_sum": dict(sig="max_window_sum(nums, k)", test=_t_max_window_sum,
        desc="Fixed-size sliding window. Max sum of any window of size k, in one pass."),
    "longest_unique_substring": dict(sig="longest_unique_substring(s)", test=_t_longest_unique_substring,
        desc="Variable sliding window. Length of the LONGEST substring of `s` with no\n"
             "repeating characters. (\"abcabcbb\" -> 3, \"bbbbb\" -> 1)"),
    "max_depth": dict(sig="max_depth(root)", test=_t_max_depth,
        desc="[tree / DFS recursion] Max depth of a binary tree. Empty tree -> 0."),
    "level_order": dict(sig="level_order(root)", test=_t_level_order,
        desc="[tree / BFS] Level-order -> list of levels (each left-to-right, top-to-bottom).\n"
             "[3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]. [] -> []."),
    "is_valid_bst": dict(sig="is_valid_bst(root)", test=_t_is_valid_bst,
        desc="[BST / bounded recursion] True if a valid BST (every left subtree < node <\n"
             "every right subtree, strictly)."),
    "search_bst": dict(sig="search_bst(root, val)", test=_t_search_bst,
        desc="[BST search] Return the SUBTREE (node) whose value == val, else None. Use the\n"
             "BST property — go left/right, don't scan the whole tree."),
    "delete_bst_node": dict(sig="delete_bst_node(root, key)", test=_t_delete_bst_node,
        desc="[BST delete] Delete the node with value `key`; return the (possibly new) root,\n"
             "keeping the BST valid. Two-child case: replace with the in-order successor."),
    "num_islands": dict(sig="num_islands(grid)", test=_t_num_islands,
        desc="[grid / flood fill] Count islands in a 2D grid of 0s and 1s, connected\n"
             "4-directionally (up/down/left/right)."),
    "three_sum": dict(sig="three_sum(nums)", test=_t_three_sum,
        desc="[sort + two pointers] All UNIQUE triplets [a,b,c] with a+b+c == 0. No\n"
             "duplicate triplets. [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]."),
    "daily_temperatures": dict(sig="daily_temperatures(temperatures)", test=_t_daily_temperatures,
        desc="[monotonic stack] For each day, how many days until a WARMER temperature\n"
             "(0 if none). [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]."),
    "merge_intervals": dict(sig="merge_intervals(intervals)", test=_t_merge_intervals,
        desc="[sort + sweep / intervals] Merge overlapping [start,end] intervals (unsorted\n"
             "input). Return merged, sorted by start. [[1,3],[2,6],[8,10]] -> [[1,6],[8,10]]."),
    "subsets": dict(sig="subsets(nums)", test=_t_subsets,
        desc="[backtracking] Power set of distinct `nums` — every subset. Order free."),
    "coin_change": dict(sig="coin_change(coins, amount)", test=_t_coin_change,
        desc="[dynamic programming] Fewest coins (unlimited each) summing to `amount`, or -1\n"
             "if impossible. coin_change([1,2,5],11) -> 3."),

    "course_schedule": dict(sig="course_schedule(num_courses, prerequisites)", test=_t_course_schedule,
        desc="[topological sort] True if all courses can finish (no cycle). prerequisites[i]\n"
             "= [a, b] means b before a. course_schedule(2,[[1,0]]) -> True."),
    "min_eating_speed": dict(sig="min_eating_speed(piles, h)", test=_t_min_eating_speed,
        desc="[binary search on the answer] Smallest integer speed to eat all `piles` within\n"
             "`h` hours (ceil(pile/speed) hours each). ([3,6,7,11], 8) -> 4."),
    "unique_paths": dict(sig="unique_paths(m, n)", test=_t_unique_paths,
        desc="[2D dynamic programming] Unique paths top-left to bottom-right of an m x n grid\n"
             "moving only right/down. unique_paths(3,7) -> 28."),
    "subarray_sum": dict(sig="subarray_sum(nums, k)", test=_t_subarray_sum,
        desc="[prefix sum + hash map] Count subarrays of `nums` whose sum equals k. Seed\n"
             "{0: 1}. subarray_sum([1,1,1], 2) -> 2."),
    "group_anagrams": dict(sig="group_anagrams(strs)", test=_t_group_anagrams,
        desc="[hash map grouping] Group anagrams together (order of/within groups free).\n"
             "Key each word by its sorted letters."),
    "diameter_of_binary_tree": dict(sig="diameter_of_binary_tree(root)", test=_t_diameter_of_binary_tree,
        desc="[tree post-order aggregation] Diameter = number of EDGES on the longest path\n"
             "between any two nodes (may not pass through root). ([1,2,3,4,5]) -> 3."),
}


# --- misc runner helpers ----------------------------------------------------
def _fmt(secs):
    m, s = divmod(int(secs), 60)
    return f"{m}m {s:02d}s"


# MM-DD-YYYY.py  OR  MM-DD-YYYY_2.py, _3.py, ...  — group(1) captures the date stem.
_DAILY_RE = __import__("re").compile(r"^(\d{2}-\d{2}-\d{4})(?:_\d+)?\.py$")


def _sweep_others(current_file):
    """Delete every drill file from a DIFFERENT day than `current_file`
    (and their .start markers). Same-day siblings — e.g. 06-13-2026.py and
    06-13-2026_2.py — are kept together; they only get swept once a LATER
    day is full-scored."""
    folder = os.path.dirname(os.path.abspath(current_file))
    keep = os.path.basename(current_file)
    cur = _DAILY_RE.match(keep)
    cur_stem = cur.group(1) if cur else None
    removed = []
    for fn in os.listdir(folder):
        m = _DAILY_RE.match(fn)
        if not m or fn == keep:
            continue
        if m.group(1) == cur_stem:
            continue                      # same-day sibling — leave it
        try:
            os.remove(os.path.join(folder, fn))
            marker = os.path.join(folder, "." + fn + ".start")
            if os.path.exists(marker):
                os.remove(marker)
            removed.append(fn)
        except OSError:
            pass
    return removed


def _run_set(names, ns, scored):
    """Run the tests for `names` that exist in both PROBLEMS and ns.
    For scored (core) sets, a configured-but-missing function counts as 'absent'
    (not a pass). For bonus, missing functions are skipped silently."""
    out = []
    for key in names:
        if key not in PROBLEMS:
            out.append((key, "not in PROBLEMS — check spelling"))
            continue
        if key not in ns:
            if scored:
                out.append((key, "absent (stub deleted?)"))
            continue
        try:
            out.append((key, PROBLEMS[key]["test"](ns)))
        except Exception as e:
            out.append((key, f"crashed: {e}"))
    return out


def run_drills(ns):
    """Run CORE (scored) and BONUS (unscored) against the functions in `ns`."""
    daily = ns.get("__file__", __file__)
    start_file = os.path.join(
        os.path.dirname(os.path.abspath(daily)),
        "." + os.path.basename(daily) + ".start",
    )

    core = _run_set(CORE, ns, scored=True)
    bonus = _run_set(BONUS, ns, scored=False)

    # timer: start on first run of THIS dated file, persist across re-runs
    if os.path.exists(start_file):
        with open(start_file) as f:
            start = float(f.read().strip())
        fresh = False
    else:
        start = time.time()
        fresh = True
        with open(start_file, "w") as f:
            f.write(repr(start))
    elapsed = time.time() - start

    print("\n" + "=" * 40)
    passed = 0
    for name, res in core:
        if res is True:
            print(f"  PASS   {name}")
            passed += 1
        elif res is False:
            print(f"  FAIL   {name}  (wrong output)")
        else:
            print(f"  ERROR  {name}  ({res})")
    print("=" * 40)
    print(f"  SCORE: {passed}/{len(core)} cold")

    if passed == len(core) and len(core) > 0:
        if fresh:
            print("  TIME:  timer only started this run — code from the stubs to clock a real session")
            os.remove(start_file)
        else:
            print(f"  TIME:  {_fmt(elapsed)}")
            os.remove(start_file)
            removed = _sweep_others(daily)
            if removed:
                print(f"  CLEANED: removed earlier day(s): {', '.join(removed)}")
                print(f"  (today's siblings stay until a later day is full-scored)")
    else:
        print(f"  ELAPSED: {_fmt(elapsed)} so far")

    if bonus:
        bpass = sum(1 for _, r in bonus if r is True)
        print("- " * 20)
        print(f"  BONUS (not scored): {bpass}/{len(bonus)}")
        for name, res in bonus:
            if res is True:
                print(f"    pass   {name}")
            elif res is False:
                print(f"    fail   {name}")
            else:
                print(f"    err    {name}  ({res})")
    print("=" * 40 + "\n")


# ============================================================================
# STAMPER  — only used when you run start.py; never copied into daily files
# ============================================================================
_DAILY_HEADER = '''"""
{date} — DSA drills.  Fill in each function from memory, then click Run.
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


'''

_DAILY_FOOTER = '\n\n\nif __name__ == "__main__":\n    run_drills(globals())\n'

_BONUS_BANNER = (
    "# " + "\u2588" * 76 + "\n"
    "# BONUS — extra reps; these do NOT count toward your SCORE and never gate the\n"
    "# timer or file cleanup. Solve them if you want, skip freely, or delete any.\n"
    "# " + "\u2588" * 76
)


def _render_stub(label, spec):
    bar = "# " + "=" * 76
    lines = spec["desc"].split("\n")
    body = [bar, f"# {label}. {lines[0]}"]
    for ln in lines[1:]:
        body.append(f"#     {ln}" if ln else "#")
    body.append(bar)
    body.append(f"def {spec['sig']}:")
    body.append("    pass")
    return "\n".join(body)


def _build_daily_body():
    blocks = []
    for i, key in enumerate(CORE, 1):
        if key in PROBLEMS:
            blocks.append(_render_stub(str(i), PROBLEMS[key]))
    if BONUS:
        blocks.append(_BONUS_BANNER)
        for j, key in enumerate(BONUS, 1):
            if key in PROBLEMS:
                blocks.append(_render_stub(f"B{j}", PROBLEMS[key]))
    return "\n\n\n".join(blocks)


def _open_in_editor(path):
    """Best-effort: open `path` in VS Code, else the OS default. Never fatal."""
    import shutil, subprocess, sys
    try:
        code = shutil.which("code") or shutil.which("code.cmd")
        if code:
            subprocess.Popen([code, "-r", path])
            return
        if sys.platform.startswith("darwin"):
            subprocess.Popen(["open", path])
        elif os.name == "nt":
            os.startfile(path)  # type: ignore[attr-defined]
        else:
            subprocess.Popen(["xdg-open", path])
    except Exception:
        pass


def _next_free_path(here, stem):
    """Return (path, nth) for the next un-taken drill file for `stem` (the
    MM-DD-YYYY date). The first is stem.py (nth=1); then stem_2.py (nth=2),
    stem_3.py (nth=3), ... — so re-running start.py the same day makes a fresh
    sibling instead of clobbering or refusing."""
    first = os.path.join(here, stem + ".py")
    if not os.path.exists(first):
        return first, 1
    n = 2
    while True:
        cand = os.path.join(here, f"{stem}_{n}.py")
        if not os.path.exists(cand):
            return cand, n
        n += 1


def _stamp_today():
    """Stamp a drill file (stubs only) beside start.py and open it.
    - If today has no file yet -> MM-DD-YYYY.py.
    - If it already has one    -> the next sibling MM-DD-YYYY_2.py, _3.py, ...
    All of today's files are kept until a LATER day is full-scored; the runner
    deletes every earlier day then. `--force` overwrites today's BASE file
    (MM-DD-YYYY.py) instead of making a new sibling."""
    import datetime, sys

    here = os.path.dirname(os.path.abspath(__file__))
    today = datetime.date.today()
    stem = today.strftime("%m-%d-%Y")
    force = "--force" in sys.argv

    if force:
        out_path, nth = os.path.join(here, stem + ".py"), 1
        existed = os.path.exists(out_path)
    else:
        out_path, nth = _next_free_path(here, stem)
        existed = False                   # we always pick a free name

    daily = _DAILY_HEADER.format(date=stem) + _build_daily_body() + _DAILY_FOOTER
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(daily)

    name = os.path.basename(out_path)
    counts = f"({len(CORE)} core + {len(BONUS)} bonus)"
    if force and existed:
        print(f"\n  Overwrote  {name}  {counts}")
    elif nth == 1:
        print(f"\n  Stamped  {name}  {counts}")
    else:
        print(f"\n  Stamped  {name}  — attempt #{nth} for today  {counts}")
    print(f"  Opening it... the timer starts when you click Run, not now.")
    print(f"  (All of today's files stay until you full-score a LATER day — then they're deleted.)\n")
    _open_in_editor(out_path)


if __name__ == "__main__":
    _stamp_today()