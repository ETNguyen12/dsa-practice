"""
DRILL GENERATOR + SHARED TEST RUNNER

Daily workflow:
  1. Run THIS file each morning:   python start.py
     -> stamps a fresh MM-DD-YYYY.py (just the stubs) beside start.py and
        opens it. Yesterday's file is KEPT as a reference for now.
     -> running start.py does NOT start any timer.
  2. In that dated file, fill in the functions and click Run.
     The clock starts on that first run. Re-run to check + see elapsed time.
  3. The moment you score 11/11 with a real time, the previous day's file is
     deleted automatically — so you keep your last good file until you've
     re-earned a full clear on the new one, then drop back to one file.

Keep start.py where it is; the daily file sits beside it and imports from it.
"""

import time, os
from collections import deque
import heapq


# --- shared types (imported by daily files) ---------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# >>> STUBS START (the stamper copies everything between these two markers) >>>
# ============================================================================
# 1. Reverse a linked list. Return the new head.
# ============================================================================
def reverse_list(head):
    pass


# ============================================================================
# 2. Find the middle node (for even length, return the second middle).
#    Use fast/slow pointers.
# ============================================================================
def find_middle(head):
    pass


# ============================================================================
# 3. Detect a cycle in a linked list. Return True/False. Fast/slow pointers.
# ============================================================================
def has_cycle(head):
    pass


# ============================================================================
# 4. BFS over a graph (adjacency list: dict[node] -> list[neighbors]).
#    Return the list of nodes in the order they are first visited, starting
#    from `start`. Visit neighbors in the order they appear in the list.
# ============================================================================
def bfs(graph, start):
    pass


# ============================================================================
# 5a. Recursive DFS. Same return contract as bfs (visit order from `start`).
# ============================================================================
def dfs_recursive(graph, start):
    pass


# ============================================================================
# 5b. Iterative DFS using an explicit stack. Same return contract.
#     (Order can differ from the recursive version — see the test.)
# ============================================================================
def dfs_iterative(graph, start):
    pass


# ============================================================================
# 6. Return the k largest numbers from `nums`, sorted descending. Use a heap.
# ============================================================================
def top_k(nums, k):
    pass


# ============================================================================
# 7. Binary search. `nums` is sorted ascending. Return the index of `target`,
#    or -1 if not present.
# ============================================================================
def binary_search(nums, target):
    pass


# ============================================================================
# 8. Leftmost insertion point. Return the index of the first element >= target
#    (i.e. where you'd insert target to keep nums sorted, choosing the leftmost
#    valid spot). For nums=[1,3,3,5], target=3 -> 1. target=4 -> 3. target=6 -> 4.
# ============================================================================
def lower_bound(nums, target):
    pass


# ============================================================================
# 9. Fixed-size sliding window. Return the maximum sum of any window of size k.
#    Assume 1 <= k <= len(nums). Do it in one pass (slide, don't re-sum).
# ============================================================================
def max_window_sum(nums, k):
    pass


# ============================================================================
# 10. Variable sliding window. Return the length of the LONGEST substring of
#     `s` with no repeating characters. ("abcabcbb" -> 3, "bbbbb" -> 1)
# ============================================================================
def longest_unique_substring(s):
    pass
# <<< STUBS END <<<


# ============================================================================
# SHARED TEST RUNNER  — imported and called by each daily file
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


def _fmt(secs):
    m, s = divmod(int(secs), 60)
    return f"{m}m {s:02d}s"


def _sweep_others(current_file):
    """Delete every drill file except `current_file` (and their .start markers).
    Called only after a full-score, real-time run, so your last good file lives
    on as a reference until you've re-earned 11/11."""
    import re
    folder = os.path.dirname(os.path.abspath(current_file))
    keep = os.path.basename(current_file)
    daily_re = re.compile(r"^\d{2}-\d{2}-\d{4}\.py$")
    removed = []
    for fn in os.listdir(folder):
        if daily_re.match(fn) and fn != keep:
            try:
                os.remove(os.path.join(folder, fn))
                marker = os.path.join(folder, "." + fn + ".start")
                if os.path.exists(marker):
                    os.remove(marker)
                removed.append(fn)
            except OSError:
                pass
    return removed


def run_drills(ns):
    """Run the suite against the drill functions in `ns` (pass globals()) and time the session."""
    reverse_list             = ns["reverse_list"]
    find_middle              = ns["find_middle"]
    has_cycle                = ns["has_cycle"]
    bfs                      = ns["bfs"]
    dfs_recursive            = ns["dfs_recursive"]
    dfs_iterative            = ns["dfs_iterative"]
    top_k                    = ns["top_k"]
    binary_search            = ns["binary_search"]
    lower_bound              = ns["lower_bound"]
    max_window_sum           = ns["max_window_sum"]
    longest_unique_substring = ns["longest_unique_substring"]

    # timer marker is unique per dated file
    daily = ns.get("__file__", __file__)
    start_file = os.path.join(
        os.path.dirname(os.path.abspath(daily)),
        "." + os.path.basename(daily) + ".start",
    )

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

    # --- timer: start on first run of THIS dated file, persist across re-runs ---
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

    if passed == len(results):
        if fresh:
            print("  TIME:  timer only started this run — code from the stubs to clock a real session")
            os.remove(start_file)       # reset; previous file kept until a real timed clear
        else:
            print(f"  TIME:  {_fmt(elapsed)}   (target: under 13m)")
            os.remove(start_file)       # reset so the next session starts fresh
            removed = _sweep_others(daily)
            if removed:
                print(f"  CLEANED: removed previous ({', '.join(removed)}) — one file left")
    else:
        print(f"  ELAPSED: {_fmt(elapsed)} so far")
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
from start import run_drills, ListNode


'''

_DAILY_FOOTER = '\n\n\nif __name__ == "__main__":\n    run_drills(globals())\n'


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


def _stamp_today():
    """Stamp today's drill file (stubs only) beside start.py and open it.
    The previous file is kept until you full-score today's — the runner deletes it then."""
    import datetime, sys

    here = os.path.dirname(os.path.abspath(__file__))
    today = datetime.date.today()
    name = today.strftime("%m-%d-%Y") + ".py"
    out_path = os.path.join(here, name)

    existed = os.path.exists(out_path)
    force = "--force" in sys.argv

    if existed and not force:
        print(f"\n  {name} already exists — leaving it alone (your work is safe).")
        print(f"  Opening it... click Run to start the clock.")
        print(f"  (Run  `python {os.path.basename(__file__)} --force`  to overwrite.)\n")
        _open_in_editor(out_path)
        return

    # pull just the stub block from this file
    with open(os.path.abspath(__file__), encoding="utf-8") as f:
        src = f.read()
    stubs = src[src.index("\n", src.index("STUBS START")) + 1:
                src.index("# <<< STUBS END")].rstrip()
    daily = _DAILY_HEADER.format(date=today.strftime("%m-%d-%Y")) + stubs + _DAILY_FOOTER

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(daily)

    verb = "Overwrote" if existed else "Stamped"
    print(f"\n  {verb}  {name}")
    print(f"  Opening it... the timer starts when you click Run, not now.")
    print(f"  (Yesterday's file stays until you score 11/11 here, then it's deleted.)\n")
    _open_in_editor(out_path)


if __name__ == "__main__":
    _stamp_today()