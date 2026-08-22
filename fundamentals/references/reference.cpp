// ============================================================================
// REFERENCE (C++) - the answer key. Open ONLY when stuck >90 seconds.
// Read until the missing piece clicks, then CLOSE this and retype the whole
// function from memory in your drill file. Don't copy-paste.
//
// Each solution has a one-line note on the part people forget, plus C++-specific
// gotchas flagged with [C++].
//
// C++ vs Python cheat notes:
//   - priority_queue is a MAX-heap by default (Python heapq is MIN). Use
//     greater<> for a min-heap.
//   - map[key] on a missing key INSERTS a default (0). Use .count()/.find().
//   - int overflows ~2.1e9 - use long long for sums; long bounds for BST.
//   - v[i] is NOT bounds-checked (no IndexError). Undefined behavior instead.
// ============================================================================

#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    Node* next;
    Node(int v = 0, Node* n = nullptr) : val(v), next(n) {}
};

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v = 0, TreeNode* l = nullptr, TreeNode* r = nullptr)
        : val(v), left(l), right(r) {}
};

// ----------------------------------------------------------------------------
// Reverse a linked list.
// Forget-point: save curr->next BEFORE you overwrite it.
Node* reverse_list(Node* head) {
    Node* prev = nullptr;
    Node* curr = head;
    while (curr) {
        Node* nxt = curr->next;   // save next
        curr->next = prev;            // flip pointer backward
        prev = curr;                  // advance prev
        curr = nxt;                   // advance curr
    }
    return prev;                      // prev is the new head
}

// Delete the middle node (floor(n/2)-th, 0-indexed).
// Forget-point: keep a `prev` one step behind slow to splice it out. Single node -> null.
Node* delete_middle_node(Node* head) {
    if (!head || !head->next) return nullptr;
    Node* prev = nullptr;
    Node* slow = head;
    Node* fast = head;
    while (fast && fast->next) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }
    prev->next = slow->next;          // skip the middle
    return head;
}

// Odd/Even linked list (group by POSITION, then reattach).
// Forget-point: stash even_head BEFORE rewiring; loop while (even && even->next).
Node* odd_even_list(Node* head) {
    if (!head || !head->next) return head;
    Node* odd = head;
    Node* even = head->next;
    Node* even_head = even;       // remember where evens start
    while (even && even->next) {
        odd->next = even->next;
        odd = odd->next;
        even->next = odd->next;
        even = even->next;
    }
    odd->next = even_head;            // odds, then evens
    return head;
}

// BFS.
// Forget-point: mark visited at ENQUEUE time, not dequeue.
vector<int> bfs(unordered_map<int, vector<int>>& graph, int start) {
    unordered_set<int> visited{start};
    queue<int> q;
    q.push(start);
    vector<int> order;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        order.push_back(node);
        for (int neighbor : graph[node]) {
            if (!visited.count(neighbor)) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
    return order;
}

// Recursive DFS.
// Forget-point: the visited set is shared across calls - pass it by reference.
static void dfs_go(unordered_map<int, vector<int>>& graph, int node,
                   unordered_set<int>& visited, vector<int>& order) {
    visited.insert(node);
    order.push_back(node);
    for (int neighbor : graph[node])
        if (!visited.count(neighbor))
            dfs_go(graph, neighbor, visited, order);
}
vector<int> dfs_recursive(unordered_map<int, vector<int>>& graph, int start) {
    unordered_set<int> visited;
    vector<int> order;
    dfs_go(graph, start, visited, order);
    return order;
}

// Iterative DFS.
// Forget-point: check visited AFTER popping (a node can be on the stack twice).
vector<int> dfs_iterative(unordered_map<int, vector<int>>& graph, int start) {
    unordered_set<int> visited;
    vector<int> stack{start};
    vector<int> order;
    while (!stack.empty()) {
        int node = stack.back(); stack.pop_back();
        if (visited.count(node)) continue;
        visited.insert(node);
        order.push_back(node);
        for (int neighbor : graph[node]) stack.push_back(neighbor);
    }
    return order;
}

// Top K largest, descending.
// Forget-point: [C++] default priority_queue is a MAX-heap; use greater<> for a
// size-k MIN-heap and evict the smallest.
vector<int> top_k(vector<int> nums, int k) {
    priority_queue<int, vector<int>, greater<int>> h;   // min-heap
    for (int n : nums) {
        h.push(n);
        if ((int)h.size() > k) h.pop();                 // drop the smallest
    }
    vector<int> res;
    while (!h.empty()) { res.push_back(h.top()); h.pop(); }
    reverse(res.begin(), res.end());                    // descending
    return res;
}

// Binary search.
// Forget-point: use lo <= hi so a single-element range is checked; mid+1 / mid-1.
// [C++] mid = lo + (hi-lo)/2 avoids overflow.
int binary_search(vector<int>& nums, int target) {
    int lo = 0, hi = (int)nums.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

// Leftmost insertion point (lower_bound). Named _idx to avoid std::lower_bound.
// Forget-point: half-open range hi = size, lo < hi, on the >= branch hi = mid.
int lower_bound_idx(vector<int>& nums, int target) {
    int lo = 0, hi = (int)nums.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] < target) lo = mid + 1;
        else hi = mid;                                   // keep mid - could be boundary
    }
    return lo;
}

// Fixed-size sliding window.
// Forget-point: seed the first window, then ADD nums[i] and SUBTRACT nums[i-k].
int max_window_sum(vector<int>& nums, int k) {
    int window = 0;
    for (int i = 0; i < k; i++) window += nums[i];
    int best = window;
    for (int i = k; i < (int)nums.size(); i++) {
        window += nums[i] - nums[i - k];
        best = max(best, window);
    }
    return best;
}

// Variable sliding window (longest substring w/o repeats).
// Forget-point: on a repeat, shrink from the LEFT in a while-loop.
int longest_unique_substring(string s) {
    unordered_set<char> seen;
    int left = 0, best = 0;
    for (int right = 0; right < (int)s.size(); right++) {
        while (seen.count(s[right])) {
            seen.erase(s[left]);
            left++;
        }
        seen.insert(s[right]);
        best = max(best, right - left + 1);
    }
    return best;
}

// Max depth of a binary tree.
// Forget-point: base case null -> 0, then 1 + max(children). The +1 = current node.
int max_depth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(max_depth(root->left), max_depth(root->right));
}

// Level-order traversal.
// Forget-point: snapshot q.size() BEFORE the inner loop = exactly this level.
vector<vector<int>> level_order(TreeNode* root) {
    vector<vector<int>> res;
    if (!root) return res;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int n = q.size();                               // fixed count = this level
        vector<int> level;
        for (int i = 0; i < n; i++) {
            TreeNode* node = q.front(); q.pop();
            level.push_back(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        res.push_back(level);
    }
    return res;
}

// Validate BST.
// Forget-point: pass DOWN a (low, high) range. [C++] use long bounds so int
// extremes don't false-fail.
static bool bst_ok(TreeNode* node, long low, long high) {
    if (!node) return true;
    if (!(low < node->val && node->val < high)) return false;
    return bst_ok(node->left, low, node->val) && bst_ok(node->right, node->val, high);
}
bool is_valid_bst(TreeNode* root) {
    return bst_ok(root, LONG_MIN, LONG_MAX);
}

// Search in a BST (return the subtree).
// Forget-point: use the ordering to pick ONE side each step (O(height)).
TreeNode* search_bst(TreeNode* root, int val) {
    while (root && root->val != val)
        root = (val < root->val) ? root->left : root->right;
    return root;
}

// Group anagrams.
// Forget-point: the key is the canonical form - sorted letters.
vector<vector<string>> group_anagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    for (string& w : strs) {
        string key = w;
        sort(key.begin(), key.end());
        groups[key].push_back(w);
    }
    vector<vector<string>> res;
    for (auto& [k, v] : groups) res.push_back(v);
    return res;
}

// Number of islands.
// Forget-point: SINK each visited cell (set to 0); bounds/zero-check at the TOP.
static void sink(vector<vector<int>>& grid, int r, int c) {
    int rows = grid.size(), cols = grid[0].size();
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != 1) return;
    grid[r][c] = 0;
    sink(grid, r + 1, c); sink(grid, r - 1, c);
    sink(grid, r, c + 1); sink(grid, r, c - 1);
}
int num_islands(vector<vector<int>> grid) {
    if (grid.empty()) return 0;
    int count = 0;
    for (int r = 0; r < (int)grid.size(); r++)
        for (int c = 0; c < (int)grid[0].size(); c++)
            if (grid[r][c] == 1) { count++; sink(grid, r, c); }
    return count;
}

// 3Sum (unique triplets summing to 0).
// Forget-point: sort first; fix i, two-pointer the rest. Skip duplicate i's AND
// after a hit skip duplicate lo/hi values.
vector<vector<int>> three_sum(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    int n = nums.size();
    for (int i = 0; i < n - 2; i++) {
        if (nums[i] > 0) break;
        if (i > 0 && nums[i] == nums[i - 1]) continue;   // skip duplicate anchor
        int lo = i + 1, hi = n - 1;
        while (lo < hi) {
            int total = nums[i] + nums[lo] + nums[hi];
            if (total < 0) lo++;
            else if (total > 0) hi--;
            else {
                res.push_back({nums[i], nums[lo], nums[hi]});
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
vector<int> daily_temperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    vector<int> res(n, 0);
    vector<int> stack;                                   // indices, temps decreasing
    for (int i = 0; i < n; i++) {
        while (!stack.empty() && temperatures[stack.back()] < temperatures[i]) {
            int j = stack.back(); stack.pop_back();
            res[j] = i - j;
        }
        stack.push_back(i);
    }
    return res;
}

// Merge intervals.
// Forget-point: SORT by start first; merge when next.start <= last.end,
// extending with max(last.end, next.end).
vector<vector<int>> merge_intervals(vector<vector<int>> intervals) {
    sort(intervals.begin(), intervals.end());            // by start
    vector<vector<int>> merged;
    for (auto& iv : intervals) {
        if (!merged.empty() && iv[0] <= merged.back()[1])
            merged.back()[1] = max(merged.back()[1], iv[1]);
        else
            merged.push_back(iv);
    }
    return merged;
}

// Delete a node in a BST.
// Forget-point: reassign left/right = recurse so links rebind. Two-child case:
// copy in-order successor (min of RIGHT subtree), then delete THAT value.
TreeNode* delete_bst_node(TreeNode* root, int key) {
    if (!root) return nullptr;
    if (key < root->val) root->left = delete_bst_node(root->left, key);
    else if (key > root->val) root->right = delete_bst_node(root->right, key);
    else {
        if (!root->left) return root->right;             // 0 or 1 child
        if (!root->right) return root->left;
        TreeNode* succ = root->right;                    // in-order successor
        while (succ->left) succ = succ->left;
        root->val = succ->val;
        root->right = delete_bst_node(root->right, succ->val);
    }
    return root;
}

// Subsets / power set.
// Forget-point: start with {{}} and for each num add it to a COPY of every subset.
vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> res{{}};
    for (int x : nums) {
        int sz = res.size();
        for (int i = 0; i < sz; i++) {
            vector<int> cur = res[i];                    // copy
            cur.push_back(x);
            res.push_back(cur);
        }
    }
    return res;
}

// Koko / min eating speed.
// Forget-point: binary-search the SPEED (1..max pile); feasibility is monotonic.
// hours per pile = ceil(pile/speed) = (pile+speed-1)/speed.
int min_eating_speed(vector<int>& piles, int h) {
    int lo = 1, hi = *max_element(piles.begin(), piles.end());
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        long hours = 0;
        for (int p : piles) hours += (p + mid - 1) / mid;
        if (hours <= h) hi = mid;                        // feasible - try slower
        else lo = mid + 1;
    }
    return lo;
}

// Subarray sum equals k (count).
// Forget-point: seed {0: 1}; for each running total add how many prior prefixes
// equal total - k.
int subarray_sum(vector<int>& nums, int k) {
    int count = 0, total = 0;
    unordered_map<int, int> seen{{0, 1}};                // prefix-sum -> frequency
    for (int x : nums) {
        total += x;
        if (seen.count(total - k)) count += seen[total - k];
        seen[total]++;
    }
    return count;
}

// ████████████████████████████████████████████████████████████████████████████
// BONUS
// ████████████████████████████████████████████████████████████████████████████

// Coin change (fewest coins).
// Forget-point: dp[0]=0, rest = INF; dp[a] = min over coins of dp[a-c]+1.
int coin_change(vector<int>& coins, int amount) {
    const int INF = 1e9;
    vector<int> dp(amount + 1, INF);
    dp[0] = 0;
    for (int a = 1; a <= amount; a++)
        for (int c : coins)
            if (c <= a) dp[a] = min(dp[a], dp[a - c] + 1);
    return dp[amount] == INF ? -1 : dp[amount];
}

// Course schedule (can all finish?).   [topological sort / Kahn]
// Forget-point: prereq [a, b] means b -> a. Peel in-degree-0 nodes; finish iff
// you process ALL nodes.
bool course_schedule(int num_courses, vector<vector<int>>& prerequisites) {
    vector<int> indeg(num_courses, 0);
    vector<vector<int>> adj(num_courses);
    for (auto& p : prerequisites) {
        adj[p[1]].push_back(p[0]);                       // b before a
        indeg[p[0]]++;
    }
    queue<int> q;
    for (int i = 0; i < num_courses; i++) if (indeg[i] == 0) q.push(i);
    int seen = 0;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        seen++;
        for (int nxt : adj[node]) if (--indeg[nxt] == 0) q.push(nxt);
    }
    return seen == num_courses;                          // all reached => acyclic
}

// Unique paths in an m x n grid.   [2D DP]
// Forget-point: each cell = above + left; first row/col all 1. Rolling row: dp[j] += dp[j-1].
int unique_paths(int m, int n) {
    vector<int> dp(n, 1);
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[j] += dp[j - 1];
    return dp[n - 1];
}

// Diameter of a binary tree (edges on longest path).
// Forget-point: update best DURING depth(): best = l + r; RETURN 1 + max(l, r).
static int diameter_depth(TreeNode* node, int& best) {
    if (!node) return 0;
    int l = diameter_depth(node->left, best);
    int r = diameter_depth(node->right, best);
    best = max(best, l + r);                             // path bending here
    return 1 + max(l, r);
}
int diameter_of_binary_tree(TreeNode* root) {
    int best = 0;
    diameter_depth(root, best);
    return best;
}

// ████████████████████████████████████████████████████████████████████████████
// DEPRECATED - already comfortable
// ████████████████████████████████████████████████████████████████████████████

// Find the middle (second middle on even length).
// Forget-point: the loop condition (fast && fast->next) makes slow land right.
Node* find_middle(Node* head) {
    Node* slow = head;
    Node* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

// Detect a cycle.
// Forget-point: same fast/slow skeleton; they collide iff there's a loop.
bool has_cycle(Node* head) {
    Node* slow = head;
    Node* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}
