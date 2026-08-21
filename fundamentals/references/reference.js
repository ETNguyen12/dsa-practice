// ============================================================================
// REFERENCE (JavaScript) - the answer key. Open ONLY when stuck >90 seconds.
// Read until the missing piece clicks, then CLOSE this and retype the whole
// function from memory in your drill file. Don't copy-paste.
//
// Each solution has a one-line note on the part people forget, plus JS-specific
// gotchas flagged with [JS].
//
// JS vs Python cheat notes:
//   - [].sort() is LEXICOGRAPHIC by default: [10,2,1].sort() -> [1,10,2].
//     ALWAYS pass a comparator for numbers: .sort((a,b) => a - b).
//   - There is NO built-in heap/priority queue. Use the MinHeap below, or sort.
//   - No integer type - everything is a float. Watch precision on huge sums.
//   - Use Map/Set for real hash structures; plain objects coerce keys to strings.
//   - Queue: array.shift() is O(n). Fine for drills; use an index pointer for perf.
// ============================================================================

// --- JS SURVIVAL KIT: a minimal binary MinHeap (JS has none built in) --------
// Push {val, ...} or raw numbers; pass a comparator (default: min by value).
class MinHeap {
  constructor(cmp = (a, b) => a - b) { this.h = []; this.cmp = cmp; }
  size() { return this.h.length; }
  peek() { return this.h[0]; }
  push(x) {
    const h = this.h; h.push(x);
    let i = h.length - 1;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (this.cmp(h[i], h[p]) >= 0) break;
      [h[i], h[p]] = [h[p], h[i]]; i = p;
    }
  }
  pop() {
    const h = this.h, top = h[0], last = h.pop();
    if (h.length) {
      h[0] = last; let i = 0;
      while (true) {
        let s = i, l = 2 * i + 1, r = 2 * i + 2;
        if (l < h.length && this.cmp(h[l], h[s]) < 0) s = l;
        if (r < h.length && this.cmp(h[r], h[s]) < 0) s = r;
        if (s === i) break;
        [h[i], h[s]] = [h[s], h[i]]; i = s;
      }
    }
    return top;
  }
}

// --- shared types ------------------------------------------------------------
class ListNode { constructor(val = 0, next = null) { this.val = val; this.next = next; } }
class TreeNode { constructor(val = 0, left = null, right = null) { this.val = val; this.left = left; this.right = right; } }

// ----------------------------------------------------------------------------
// Reverse a linked list.
// Forget-point: save curr.next BEFORE you overwrite it.
function reverseList(head) {
  let prev = null, curr = head;
  while (curr) {
    const nxt = curr.next;   // save next
    curr.next = prev;        // flip backward
    prev = curr;             // advance prev
    curr = nxt;              // advance curr
  }
  return prev;               // new head
}

// Delete the middle node (floor(n/2)-th, 0-indexed).
// Forget-point: keep a `prev` one step behind slow to splice it out. Single node -> null.
function deleteMiddleNode(head) {
  if (!head || !head.next) return null;
  let prev = null, slow = head, fast = head;
  while (fast && fast.next) {
    prev = slow;
    slow = slow.next;
    fast = fast.next.next;
  }
  prev.next = slow.next;     // skip the middle
  return head;
}

// Odd/Even linked list (group by POSITION, then reattach).
// Forget-point: stash evenHead BEFORE rewiring; loop while (even && even.next).
function oddEvenList(head) {
  if (!head || !head.next) return head;
  let odd = head, even = head.next;
  const evenHead = even;
  while (even && even.next) {
    odd.next = even.next;
    odd = odd.next;
    even.next = odd.next;
    even = even.next;
  }
  odd.next = evenHead;       // odds, then evens
  return head;
}

// BFS.
// Forget-point: mark visited at ENQUEUE time, not dequeue.
function bfs(graph, start) {
  const visited = new Set([start]);
  const q = [start];
  const order = [];
  while (q.length) {
    const node = q.shift();
    order.push(node);
    for (const neighbor of graph[node]) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        q.push(neighbor);
      }
    }
  }
  return order;
}

// Recursive DFS.
// Forget-point: the visited set is shared across calls - close over it.
function dfsRecursive(graph, start) {
  const visited = new Set(), order = [];
  function go(node) {
    visited.add(node);
    order.push(node);
    for (const neighbor of graph[node])
      if (!visited.has(neighbor)) go(neighbor);
  }
  go(start);
  return order;
}

// Iterative DFS.
// Forget-point: check visited AFTER popping (a node can be on the stack twice).
function dfsIterative(graph, start) {
  const visited = new Set(), stack = [start], order = [];
  while (stack.length) {
    const node = stack.pop();
    if (visited.has(node)) continue;
    visited.add(node);
    order.push(node);
    for (const neighbor of graph[node]) stack.push(neighbor);
  }
  return order;
}

// Top K largest, descending.
// Forget-point: [JS] no heap built in. Clean way: sort desc, slice. (Comparator
// is mandatory or you get lexicographic order.)
function topK(nums, k) {
  return [...nums].sort((a, b) => b - a).slice(0, k);
  // --- heap way (size-k MinHeap, evict smallest) ---
  // const h = new MinHeap();
  // for (const n of nums) { h.push(n); if (h.size() > k) h.pop(); }
  // const res = []; while (h.size()) res.push(h.pop());
  // return res.reverse();
}

// Binary search.
// Forget-point: lo <= hi so a single-element range is checked; mid+1 / mid-1.
function binarySearch(nums, target) {
  let lo = 0, hi = nums.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if (nums[mid] === target) return mid;
    else if (nums[mid] < target) lo = mid + 1;
    else hi = mid - 1;
  }
  return -1;
}

// Leftmost insertion point (lower_bound).
// Forget-point: half-open range hi = length, lo < hi, on the >= branch hi = mid.
function lowerBound(nums, target) {
  let lo = 0, hi = nums.length;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (nums[mid] < target) lo = mid + 1;
    else hi = mid;             // keep mid - could be boundary
  }
  return lo;
}

// Fixed-size sliding window.
// Forget-point: seed the first window, then ADD nums[i] and SUBTRACT nums[i-k].
function maxWindowSum(nums, k) {
  let window = 0;
  for (let i = 0; i < k; i++) window += nums[i];
  let best = window;
  for (let i = k; i < nums.length; i++) {
    window += nums[i] - nums[i - k];
    best = Math.max(best, window);
  }
  return best;
}

// Variable sliding window (longest substring w/o repeats).
// Forget-point: on a repeat, shrink from the LEFT in a while-loop.
function longestUniqueSubstring(s) {
  const seen = new Set();
  let left = 0, best = 0;
  for (let right = 0; right < s.length; right++) {
    while (seen.has(s[right])) {
      seen.delete(s[left]);
      left++;
    }
    seen.add(s[right]);
    best = Math.max(best, right - left + 1);
  }
  return best;
}

// Max depth of a binary tree.
// Forget-point: base case null -> 0, then 1 + max(children).
function maxDepth(root) {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

// Level-order traversal.
// Forget-point: snapshot q.length BEFORE the inner loop = exactly this level.
function levelOrder(root) {
  if (!root) return [];
  const res = [], q = [root];
  while (q.length) {
    const n = q.length;        // fixed count = this level
    const level = [];
    for (let i = 0; i < n; i++) {
      const node = q.shift();
      level.push(node.val);
      if (node.left) q.push(node.left);
      if (node.right) q.push(node.right);
    }
    res.push(level);
  }
  return res;
}

// Validate BST.
// Forget-point: pass DOWN a (low, high) range; strict inequalities.
function isValidBst(root) {
  function ok(node, low, high) {
    if (!node) return true;
    if (!(low < node.val && node.val < high)) return false;
    return ok(node.left, low, node.val) && ok(node.right, node.val, high);
  }
  return ok(root, -Infinity, Infinity);
}

// Search in a BST (return the subtree).
// Forget-point: use the ordering to pick ONE side each step (O(height)).
function searchBst(root, val) {
  while (root && root.val !== val)
    root = val < root.val ? root.left : root.right;
  return root;
}

// Group anagrams.
// Forget-point: key by the canonical form - sorted letters. [JS] split/sort/join.
function groupAnagrams(strs) {
  const groups = new Map();
  for (const w of strs) {
    const key = [...w].sort().join('');
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(w);
  }
  return [...groups.values()];
}

// Number of islands.
// Forget-point: SINK each visited cell (set to 0); bounds/zero-check at the TOP.
function numIslands(grid) {
  if (!grid.length) return 0;
  const rows = grid.length, cols = grid[0].length;
  let count = 0;
  function sink(r, c) {
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] !== 1) return;
    grid[r][c] = 0;
    sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1);
  }
  for (let r = 0; r < rows; r++)
    for (let c = 0; c < cols; c++)
      if (grid[r][c] === 1) { count++; sink(r, c); }
  return count;
}

// 3Sum (unique triplets summing to 0).
// Forget-point: sort first ([JS] numeric comparator!); fix i, two-pointer rest;
// skip duplicate i's AND after a hit skip duplicate lo/hi.
function threeSum(nums) {
  nums = [...nums].sort((a, b) => a - b);
  const res = [], n = nums.length;
  for (let i = 0; i < n - 2; i++) {
    if (nums[i] > 0) break;
    if (i > 0 && nums[i] === nums[i - 1]) continue;   // skip duplicate anchor
    let lo = i + 1, hi = n - 1;
    while (lo < hi) {
      const total = nums[i] + nums[lo] + nums[hi];
      if (total < 0) lo++;
      else if (total > 0) hi--;
      else {
        res.push([nums[i], nums[lo], nums[hi]]);
        lo++; hi--;
        while (lo < hi && nums[lo] === nums[lo - 1]) lo++;   // skip dup
        while (lo < hi && nums[hi] === nums[hi + 1]) hi--;   // skip dup
      }
    }
  }
  return res;
}

// Daily temperatures.
// Forget-point: the stack holds INDICES with strictly decreasing temps.
function dailyTemperatures(temperatures) {
  const n = temperatures.length, res = new Array(n).fill(0), stack = [];
  for (let i = 0; i < n; i++) {
    while (stack.length && temperatures[stack[stack.length - 1]] < temperatures[i]) {
      const j = stack.pop();
      res[j] = i - j;
    }
    stack.push(i);
  }
  return res;
}

// Merge intervals.
// Forget-point: SORT by start first ([JS] comparator!); merge when
// next.start <= last.end, extend with max(last.end, next.end).
function mergeIntervals(intervals) {
  const sorted = [...intervals].sort((a, b) => a[0] - b[0]);
  const merged = [];
  for (const iv of sorted) {
    const last = merged[merged.length - 1];
    if (merged.length && iv[0] <= last[1]) last[1] = Math.max(last[1], iv[1]);
    else merged.push([...iv]);        // copy so we don't mutate input
  }
  return merged;
}

// Delete a node in a BST.
// Forget-point: reassign left/right = recurse so links rebind. Two-child case:
// copy in-order successor (min of RIGHT subtree), then delete THAT value.
function deleteBstNode(root, key) {
  if (!root) return null;
  if (key < root.val) root.left = deleteBstNode(root.left, key);
  else if (key > root.val) root.right = deleteBstNode(root.right, key);
  else {
    if (!root.left) return root.right;      // 0 or 1 child
    if (!root.right) return root.left;
    let succ = root.right;                   // in-order successor
    while (succ.left) succ = succ.left;
    root.val = succ.val;
    root.right = deleteBstNode(root.right, succ.val);
  }
  return root;
}

// Subsets / power set.
// Forget-point: start with [[]] and for each num add it to a COPY of every subset.
function subsets(nums) {
  let res = [[]];
  for (const x of nums)
    res = res.concat(res.map(cur => [...cur, x]));
  return res;
}

// Koko / min eating speed.
// Forget-point: binary-search the SPEED (1..max pile); feasibility is monotonic.
// hours per pile = ceil(pile/speed).
function minEatingSpeed(piles, h) {
  let lo = 1, hi = Math.max(...piles);
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    let hours = 0;
    for (const p of piles) hours += Math.ceil(p / mid);
    if (hours <= h) hi = mid;         // feasible - try slower
    else lo = mid + 1;
  }
  return lo;
}

// Subarray sum equals k (count).
// Forget-point: seed {0: 1}; for each running total add prior prefixes equal to total - k.
function subarraySum(nums, k) {
  let count = 0, total = 0;
  const seen = new Map([[0, 1]]);
  for (const x of nums) {
    total += x;
    if (seen.has(total - k)) count += seen.get(total - k);
    seen.set(total, (seen.get(total) || 0) + 1);
  }
  return count;
}

// ████████████████████████████████████████████████████████████████████████████
// BONUS
// ████████████████████████████████████████████████████████████████████████████

// Coin change (fewest coins).
// Forget-point: dp[0]=0, rest = Infinity; dp[a] = min over coins of dp[a-c]+1.
function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  for (let a = 1; a <= amount; a++)
    for (const c of coins)
      if (c <= a) dp[a] = Math.min(dp[a], dp[a - c] + 1);
  return dp[amount] === Infinity ? -1 : dp[amount];
}

// Course schedule (can all finish?).   [topological sort / Kahn]
// Forget-point: prereq [a, b] means b -> a. Peel in-degree-0 nodes; finish iff
// you process ALL nodes.
function courseSchedule(numCourses, prerequisites) {
  const indeg = new Array(numCourses).fill(0);
  const adj = Array.from({ length: numCourses }, () => []);
  for (const [a, b] of prerequisites) { adj[b].push(a); indeg[a]++; }
  const q = [];
  for (let i = 0; i < numCourses; i++) if (indeg[i] === 0) q.push(i);
  let seen = 0;
  while (q.length) {
    const node = q.shift();
    seen++;
    for (const nxt of adj[node]) if (--indeg[nxt] === 0) q.push(nxt);
  }
  return seen === numCourses;
}

// Unique paths in an m x n grid.   [2D DP]
// Forget-point: each cell = above + left; first row/col all 1. Rolling row: dp[j] += dp[j-1].
function uniquePaths(m, n) {
  const dp = new Array(n).fill(1);
  for (let i = 1; i < m; i++)
    for (let j = 1; j < n; j++)
      dp[j] += dp[j - 1];
  return dp[n - 1];
}

// Diameter of a binary tree (edges on longest path).
// Forget-point: update best DURING depth(): best = l + r; RETURN 1 + max(l, r).
function diameterOfBinaryTree(root) {
  let best = 0;
  function depth(node) {
    if (!node) return 0;
    const l = depth(node.left), r = depth(node.right);
    best = Math.max(best, l + r);     // path bending here
    return 1 + Math.max(l, r);
  }
  depth(root);
  return best;
}

// ████████████████████████████████████████████████████████████████████████████
// DEPRECATED - already comfortable
// ████████████████████████████████████████████████████████████████████████████

// Find the middle (second middle on even length).
function findMiddle(head) {
  let slow = head, fast = head;
  while (fast && fast.next) { slow = slow.next; fast = fast.next.next; }
  return slow;
}

// Detect a cycle.
function hasCycle(head) {
  let slow = head, fast = head;
  while (fast && fast.next) {
    slow = slow.next; fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}

if (typeof module !== 'undefined') module.exports = {
  MinHeap, ListNode, TreeNode, reverseList, deleteMiddleNode, oddEvenList, bfs,
  dfsRecursive, dfsIterative, topK, binarySearch, lowerBound, maxWindowSum,
  longestUniqueSubstring, maxDepth, levelOrder, isValidBst, searchBst,
  groupAnagrams, numIslands, threeSum, dailyTemperatures, mergeIntervals,
  deleteBstNode, subsets, minEatingSpeed, subarraySum, coinChange,
  courseSchedule, uniquePaths, diameterOfBinaryTree, findMiddle, hasCycle,
};
