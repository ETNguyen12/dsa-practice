// ============================================================================
// REFERENCE (Java) - the answer key. Open ONLY when stuck >90 seconds.
// Read until the missing piece clicks, then CLOSE this and retype the whole
// method from memory in your drill file. Don't copy-paste.
//
// Each solution has a one-line note on the part people forget, plus Java-specific
// gotchas flagged with [Java]. Signatures mirror LeetCode's Java style.
//
// Java vs Python cheat notes:
//   - PriorityQueue is a MIN-heap by default (like Python heapq, opposite of C++).
//     Use Collections.reverseOrder() or a comparator for a max-heap.
//   - [Java] the == trap: comparing Integer objects with == compares REFERENCES.
//     Use .equals() or unbox to int. (Autoboxing bites in maps/lists.)
//   - int overflows ~2.1e9 - use long for sums; long bounds for BST validation.
//   - Deque (ArrayDeque) is your stack AND your queue: push/pop, offer/poll.
// ============================================================================

import java.util.*;

public class Reference {

    public static class ListNode {
        int val; ListNode next;
        ListNode() {}
        ListNode(int v) { val = v; }
        ListNode(int v, ListNode n) { val = v; next = n; }
    }

    public static class TreeNode {
        int val; TreeNode left, right;
        TreeNode() {}
        TreeNode(int v) { val = v; }
        TreeNode(int v, TreeNode l, TreeNode r) { val = v; left = l; right = r; }
    }

    // ------------------------------------------------------------------------
    // Reverse a linked list.
    // Forget-point: save curr.next BEFORE you overwrite it.
    public static ListNode reverseList(ListNode head) {
        ListNode prev = null, curr = head;
        while (curr != null) {
            ListNode nxt = curr.next;   // save next
            curr.next = prev;           // flip backward
            prev = curr;                // advance prev
            curr = nxt;                 // advance curr
        }
        return prev;                    // new head
    }

    // Delete the middle node (floor(n/2)-th, 0-indexed).
    // Forget-point: keep a `prev` one step behind slow to splice it out. Single -> null.
    public static ListNode deleteMiddleNode(ListNode head) {
        if (head == null || head.next == null) return null;
        ListNode prev = null, slow = head, fast = head;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = slow.next;          // skip the middle
        return head;
    }

    // Odd/Even linked list (group by POSITION, then reattach).
    // Forget-point: stash evenHead BEFORE rewiring; loop while (even && even.next).
    public static ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode odd = head, even = head.next, evenHead = even;
        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;
            even.next = odd.next;
            even = even.next;
        }
        odd.next = evenHead;            // odds, then evens
        return head;
    }

    // BFS.
    // Forget-point: mark visited at ENQUEUE time, not dequeue.
    public static List<Integer> bfs(Map<Integer, List<Integer>> graph, int start) {
        Set<Integer> visited = new HashSet<>(); visited.add(start);
        Deque<Integer> q = new ArrayDeque<>(); q.offer(start);
        List<Integer> order = new ArrayList<>();
        while (!q.isEmpty()) {
            int node = q.poll();
            order.add(node);
            for (int neighbor : graph.get(node)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    q.offer(neighbor);
                }
            }
        }
        return order;
    }

    // Recursive DFS.
    // Forget-point: the visited set is shared across calls - pass it down.
    public static List<Integer> dfsRecursive(Map<Integer, List<Integer>> graph, int start) {
        Set<Integer> visited = new HashSet<>();
        List<Integer> order = new ArrayList<>();
        dfsGo(graph, start, visited, order);
        return order;
    }
    private static void dfsGo(Map<Integer, List<Integer>> graph, int node,
                              Set<Integer> visited, List<Integer> order) {
        visited.add(node);
        order.add(node);
        for (int neighbor : graph.get(node))
            if (!visited.contains(neighbor)) dfsGo(graph, neighbor, visited, order);
    }

    // Iterative DFS.
    // Forget-point: check visited AFTER popping (a node can be on the stack twice).
    public static List<Integer> dfsIterative(Map<Integer, List<Integer>> graph, int start) {
        Set<Integer> visited = new HashSet<>();
        Deque<Integer> stack = new ArrayDeque<>(); stack.push(start);
        List<Integer> order = new ArrayList<>();
        while (!stack.isEmpty()) {
            int node = stack.pop();
            if (visited.contains(node)) continue;
            visited.add(node);
            order.add(node);
            for (int neighbor : graph.get(node)) stack.push(neighbor);
        }
        return order;
    }

    // Top K largest, descending.
    // Forget-point: [Java] PriorityQueue is a MIN-heap by default - perfect for a
    // size-k heap that evicts the smallest.
    public static List<Integer> topK(int[] nums, int k) {
        PriorityQueue<Integer> h = new PriorityQueue<>();   // min-heap
        for (int n : nums) {
            h.offer(n);
            if (h.size() > k) h.poll();                     // drop the smallest
        }
        List<Integer> res = new ArrayList<>(h);
        res.sort(Collections.reverseOrder());               // descending
        return res;
    }

    // Binary search.
    // Forget-point: lo <= hi so a single-element range is checked; mid+1 / mid-1.
    // [Java] lo + (hi-lo)/2 avoids overflow.
    public static int binarySearch(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }

    // Leftmost insertion point (lower_bound).
    // Forget-point: half-open range hi = length, lo < hi, on the >= branch hi = mid.
    public static int lowerBound(int[] nums, int target) {
        int lo = 0, hi = nums.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] < target) lo = mid + 1;
            else hi = mid;              // keep mid - could be boundary
        }
        return lo;
    }

    // Fixed-size sliding window.
    // Forget-point: seed the first window, then ADD nums[i] and SUBTRACT nums[i-k].
    public static int maxWindowSum(int[] nums, int k) {
        int window = 0;
        for (int i = 0; i < k; i++) window += nums[i];
        int best = window;
        for (int i = k; i < nums.length; i++) {
            window += nums[i] - nums[i - k];
            best = Math.max(best, window);
        }
        return best;
    }

    // Variable sliding window (longest substring w/o repeats).
    // Forget-point: on a repeat, shrink from the LEFT in a while-loop.
    public static int longestUniqueSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            while (seen.contains(s.charAt(right))) {
                seen.remove(s.charAt(left));
                left++;
            }
            seen.add(s.charAt(right));
            best = Math.max(best, right - left + 1);
        }
        return best;
    }

    // Max depth of a binary tree.
    // Forget-point: base case null -> 0, then 1 + max(children).
    public static int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }

    // Level-order traversal.
    // Forget-point: snapshot q.size() BEFORE the inner loop = exactly this level.
    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> q = new ArrayDeque<>(); q.offer(root);
        while (!q.isEmpty()) {
            int n = q.size();           // fixed count = this level
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                TreeNode node = q.poll();
                level.add(node.val);
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            res.add(level);
        }
        return res;
    }

    // Validate BST.
    // Forget-point: pass DOWN a (low, high) range. [Java] use long bounds so int
    // extremes don't false-fail.
    public static boolean isValidBst(TreeNode root) {
        return bstOk(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    private static boolean bstOk(TreeNode node, long low, long high) {
        if (node == null) return true;
        if (!(low < node.val && node.val < high)) return false;
        return bstOk(node.left, low, node.val) && bstOk(node.right, node.val, high);
    }

    // Search in a BST (return the subtree).
    // Forget-point: use the ordering to pick ONE side each step (O(height)).
    public static TreeNode searchBst(TreeNode root, int val) {
        while (root != null && root.val != val)
            root = (val < root.val) ? root.left : root.right;
        return root;
    }

    // Group anagrams.
    // Forget-point: key by the canonical form - sorted letters.
    public static List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();
        for (String w : strs) {
            char[] a = w.toCharArray();
            Arrays.sort(a);
            String key = new String(a);
            groups.computeIfAbsent(key, x -> new ArrayList<>()).add(w);
        }
        return new ArrayList<>(groups.values());
    }

    // Number of islands.
    // Forget-point: SINK each visited cell (set to 0); bounds/zero-check at the TOP.
    public static int numIslands(int[][] grid) {
        if (grid.length == 0) return 0;
        int count = 0;
        for (int r = 0; r < grid.length; r++)
            for (int c = 0; c < grid[0].length; c++)
                if (grid[r][c] == 1) { count++; sink(grid, r, c); }
        return count;
    }
    private static void sink(int[][] grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] != 1) return;
        grid[r][c] = 0;
        sink(grid, r + 1, c); sink(grid, r - 1, c);
        sink(grid, r, c + 1); sink(grid, r, c - 1);
    }

    // 3Sum (unique triplets summing to 0).
    // Forget-point: sort first; fix i, two-pointer the rest; skip duplicate i's AND
    // after a hit skip duplicate lo/hi values.
    public static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;
        for (int i = 0; i < n - 2; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;   // skip duplicate anchor
            int lo = i + 1, hi = n - 1;
            while (lo < hi) {
                int total = nums[i] + nums[lo] + nums[hi];
                if (total < 0) lo++;
                else if (total > 0) hi--;
                else {
                    res.add(Arrays.asList(nums[i], nums[lo], nums[hi]));
                    lo++; hi--;
                    while (lo < hi && nums[lo] == nums[lo - 1]) lo++;   // skip dup
                    while (lo < hi && nums[hi] == nums[hi + 1]) hi--;   // skip dup
                }
            }
        }
        return res;
    }

    // Daily temperatures.
    // Forget-point: the stack holds INDICES with strictly decreasing temps.
    public static int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();          // indices, temps decreasing
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int j = stack.pop();
                res[j] = i - j;
            }
            stack.push(i);
        }
        return res;
    }

    // Merge intervals.
    // Forget-point: SORT by start first; merge when next.start <= last.end,
    // extend with max(last.end, next.end).
    public static int[][] mergeIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        for (int[] iv : intervals) {
            if (!merged.isEmpty() && iv[0] <= merged.get(merged.size() - 1)[1])
                merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], iv[1]);
            else
                merged.add(new int[]{iv[0], iv[1]});        // copy so we don't mutate input
        }
        return merged.toArray(new int[0][]);
    }

    // Delete a node in a BST.
    // Forget-point: reassign left/right = recurse so links rebind. Two-child case:
    // copy in-order successor (min of RIGHT subtree), then delete THAT value.
    public static TreeNode deleteBstNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) root.left = deleteBstNode(root.left, key);
        else if (key > root.val) root.right = deleteBstNode(root.right, key);
        else {
            if (root.left == null) return root.right;       // 0 or 1 child
            if (root.right == null) return root.left;
            TreeNode succ = root.right;                      // in-order successor
            while (succ.left != null) succ = succ.left;
            root.val = succ.val;
            root.right = deleteBstNode(root.right, succ.val);
        }
        return root;
    }

    // Subsets / power set.
    // Forget-point: start with [[]] and for each num add it to a COPY of every subset.
    public static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());
        for (int x : nums) {
            int sz = res.size();
            for (int i = 0; i < sz; i++) {
                List<Integer> cur = new ArrayList<>(res.get(i));   // copy
                cur.add(x);
                res.add(cur);
            }
        }
        return res;
    }

    // Koko / min eating speed.
    // Forget-point: binary-search the SPEED (1..max pile); feasibility is monotonic.
    // hours per pile = ceil(pile/speed) = (pile + speed - 1) / speed.
    public static int minEatingSpeed(int[] piles, int h) {
        int lo = 1, hi = 0;
        for (int p : piles) hi = Math.max(hi, p);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            long hours = 0;
            for (int p : piles) hours += (p + mid - 1) / mid;
            if (hours <= h) hi = mid;                       // feasible - try slower
            else lo = mid + 1;
        }
        return lo;
    }

    // Subarray sum equals k (count).
    // Forget-point: seed {0: 1}; for each running total add prior prefixes equal to total - k.
    public static int subarraySum(int[] nums, int k) {
        int count = 0, total = 0;
        Map<Integer, Integer> seen = new HashMap<>();
        seen.put(0, 1);
        for (int x : nums) {
            total += x;
            count += seen.getOrDefault(total - k, 0);
            seen.put(total, seen.getOrDefault(total, 0) + 1);
        }
        return count;
    }

    // ████████████████████████████████████████████████████████████████████████
    // BONUS
    // ████████████████████████████████████████████████████████████████████████

    // Coin change (fewest coins).
    // Forget-point: dp[0]=0, rest = "infinity"; dp[a] = min over coins of dp[a-c]+1.
    public static int coinChange(int[] coins, int amount) {
        int INF = amount + 1;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;
        for (int a = 1; a <= amount; a++)
            for (int c : coins)
                if (c <= a) dp[a] = Math.min(dp[a], dp[a - c] + 1);
        return dp[amount] == INF ? -1 : dp[amount];
    }

    // Course schedule (can all finish?).   [topological sort / Kahn]
    // Forget-point: prereq [a, b] means b -> a. Peel in-degree-0 nodes; finish iff
    // you process ALL nodes.
    public static boolean courseSchedule(int numCourses, int[][] prerequisites) {
        int[] indeg = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        for (int[] p : prerequisites) { adj.get(p[1]).add(p[0]); indeg[p[0]]++; }
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) if (indeg[i] == 0) q.offer(i);
        int seen = 0;
        while (!q.isEmpty()) {
            int node = q.poll();
            seen++;
            for (int nxt : adj.get(node)) if (--indeg[nxt] == 0) q.offer(nxt);
        }
        return seen == numCourses;
    }

    // Unique paths in an m x n grid.   [2D DP]
    // Forget-point: each cell = above + left; first row/col all 1. Rolling row: dp[j] += dp[j-1].
    public static int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                dp[j] += dp[j - 1];
        return dp[n - 1];
    }

    // Diameter of a binary tree (edges on longest path).
    // Forget-point: update best DURING depth(). [Java] use a 1-element array as a
    // mutable holder since there are no nonlocal ints.
    public static int diameterOfBinaryTree(TreeNode root) {
        int[] best = {0};
        diameterDepth(root, best);
        return best[0];
    }
    private static int diameterDepth(TreeNode node, int[] best) {
        if (node == null) return 0;
        int l = diameterDepth(node.left, best);
        int r = diameterDepth(node.right, best);
        best[0] = Math.max(best[0], l + r);                 // path bending here
        return 1 + Math.max(l, r);
    }

    // ████████████████████████████████████████████████████████████████████████
    // DEPRECATED - already comfortable
    // ████████████████████████████████████████████████████████████████████████

    // Find the middle (second middle on even length).
    public static ListNode findMiddle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) { slow = slow.next; fast = fast.next.next; }
        return slow;
    }

    // Detect a cycle.
    public static boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next; fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}
